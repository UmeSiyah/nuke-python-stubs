import os

import hiero.ui
import hiero.core
import hiero.core.log
import opentimelineio as otio
from PySide2.QtCore import QUrl, QCoreApplication
from hiero.core.FnEffectHelpers import reformatStateToDict
from hiero.core.FnOtioMarkerColorMapping import \
    kOtioMarkerColorMappedToHieroTagIcons

from .FnBackgroundThreadHelper import runFunctionInBackgroundThread


class TransitionType:
    FADE_IN = 0
    FADE_OUT = 1
    DISSOLVE = 2


def _readOpenTimelineIOFile(filePath):
    otioTimeline = None
    try:
        otioTimeline = otio.adapters.read_from_file(filePath)
        # read_from_file returns an object that is not an otio.schema.Timeline instance in some cases, such as after reading
        # a valid JSON file that does not conform to the OpenTimelineIO file format specification documentation.
        if not isinstance(otioTimeline, otio.schema.Timeline):
            hiero.core.log.error(
                'File {} does not contain an OpenTimelineIO timeline.'.format(filePath))
            otioTimeline = None
    except ValueError:
        # read_from_file raises a ValueError exception when filePath is not a valid JSON file.
        hiero.core.log.error('File {} is not a JSON file'.format(filePath))
    except KeyError as e:
        # OpenTimelineIO raises KeyError exceptions when an object being read is missing an attribute of its schema.
        # From this point onwards it can be assumed that all OTIO objects have all expected attributes.
        hiero.core.log.error('{} import error {}'.format(filePath, e))
    except:
        # Unknown exception type.
        hiero.core.log.exception('Unknown exception raised while importing {}.'.format(filePath))

    return otioTimeline


def _getFrameRateFromClips(otioTimeline):
    # This function assumes that the OpenTimelineIO TimeRange rate values of all clips are the same.
    # Returns the first valid frame rate found in the timeline.
    for otioTrack in otioTimeline.tracks:
        for otioClip in otioTrack.each_clip():
            try:
                # trimmed_range may raise exceptions for clips that lack both a source_range and an available_range().
                if otioClip.trimmed_range() is not None:
                    return hiero.core.TimeBase(otioClip.trimmed_range().duration.rate)
            except otio.exceptions.CannotComputeAvailableRangeError:
                pass

    return hiero.core.TimeBase(24)


def _getSequenceProperties(otioTimeline):
    """
    Obtain the Hiero sequence's starting timecode and frame rate from the OpenTimelineIO data.
    :param timeline: OpenTimelineIO sequence
    :return: Tuple containing the starting timecode and frame rate.
    """
    globalStartTime = otioTimeline.global_start_time
    if globalStartTime is None:
        # If the global_start_time is missing, assume that the starting timecode is 00:00:00.
        sequenceTimecode = 0
        # Estimate the frame rate from the clips present in the timeline.
        frameRate = _getFrameRateFromClips(otioTimeline)
    else:
        sequenceTimecode = globalStartTime.value
        frameRate = hiero.core.TimeBase(globalStartTime.rate)

    return sequenceTimecode, frameRate


def _clipRetime(otioClip):
    retime = 1.0
    for otioEffect in otioClip.effects:
        if isinstance(otioEffect, otio.schema.LinearTimeWarp):
            # Also handles otio.schema.FreezeFrame, derived from LinearTimeWarp. time_scalar should be 0.0 in that case.
            retime *= otioEffect.time_scalar
    return retime


def _getClipTimeData(otioClip):
    """ Get source time data from a clip. Returns (startTime, frameRate, duration) """
    try:
        availableRange = otioClip.available_range()
        mediaStartTime = availableRange.start_time.value
        mediaFrameRate = availableRange.duration.rate
        mediaDuration = availableRange.duration.value
    except otio.exceptions.CannotComputeAvailableRangeError:
        # The clip lacks an available_range entry in the OpenTimelineIO file.
        mediaStartTime = 0
        # At this point clip.trimmed_range() has already been checked before, and it is known it will return a valid value.
        mediaFrameRate = otioClip.trimmed_range().duration.rate
        mediaDuration = otioClip.trimmed_range().duration.value

    return int(mediaStartTime), hiero.core.TimeBase(mediaFrameRate), int(mediaDuration)


def _getMarkerTimeData(otioMarker, otioClipSourceStartTime):
    """ Get the start and end time of the marker in frames. For an otio.Schema.Clip object,
    the start time is relative to the media source start time. See _getClipTimeData"""
    start = int(otioMarker.marked_range.start_time.value)
    if otioClipSourceStartTime:
        start = start - int(otioClipSourceStartTime)
    end = int(start + otioMarker.marked_range.duration.value - 1)
    return start, end


def _getPathFromURL(urlString):
    url = QUrl(urlString)

    # The importer only needs to consider URLs with the 'file:' scheme or with no scheme at all. URLs without a scheme
    # are absolute or relative file system paths.
    # QUrl.toLocalFile() only returns valid paths when the scheme is set to file. Other cases are handled later.
    if url.isLocalFile():
        localFile = url.toLocalFile()
        # Remove leading '/' for local file path that begins with windows drive letter
        # Qt automatically does this on windows, so this is only required on linux and mac
        if len(localFile) > 2 and localFile[0] == '/' and localFile[2] == ':':
            return localFile[1:]
        return localFile
    elif url.scheme() == '':
        # Since the URL scheme is empty, the url string must be an absolute or relative file system path.
        return urlString
    else:
        # Prevent unsupported schemes from being considered as file system paths.
        raise ValueError(
            'OTIOImporter found a target_url with unsupported scheme: {}'.format(url.scheme()))


def _getMediaPath(otioMedia):
    if otioMedia is None or isinstance(otioMedia, otio.schema.MissingReference) or isinstance(otioMedia, otio.schema.GeneratorReference):
        return ''

    isImageSequence = hasattr(otioMedia, 'target_url_base')

    if isImageSequence:
        urlString = os.path.join(otioMedia.target_url_base, otioMedia.name_prefix)
    else:
        try:
            urlString = otioMedia.target_url
        except:
            raise ValueError('\'target_url\' not defined for media {}'.format(otioMedia.name))

    path = _getPathFromURL(urlString)

    if isImageSequence:
        padding = otioMedia.frame_zero_padding

        # Even with zero padding, frame numbers will need to use at least one digit.
        padding = max(1, padding)

        # Huge (and likely incorrect) padding values prevent the "Parsing sequence file" task from ever finishing.
        if padding > 20:
            hiero.core.log.error(
                'OTIOImporter parsed a frame_zero_padding value of {}, which is too large. 0 will be used instead.'.format(
                    padding))
            padding = 0

        path += ('#' * padding) + otioMedia.name_suffix

    return path


def _getTransitionType(otioTrackItems, index):
    if index == 0 or isinstance(otioTrackItems[index-1], otio.schema.Gap) or otioTrackItems[index].in_offset.value == 0:
        transitionType = TransitionType.FADE_IN
    elif index >= (len(otioTrackItems)-1) or isinstance(otioTrackItems[index+1], otio.schema.Gap) or otioTrackItems[index].in_offset.value == 0:
        transitionType = TransitionType.FADE_OUT
    else:
        transitionType = TransitionType.DISSOLVE
    return transitionType


def _createFadeInTransition(hieroTrackItem, duration, trackType):
    if trackType == hiero.core.TrackItem.kAudio:
        return hiero.core.Transition.createAudioFadeInTransition(hieroTrackItem, duration)
    else:
        return hiero.core.Transition.createFadeInTransition(hieroTrackItem, duration)


def _createFadeOutTransition(hieroTrackItem, duration, trackType):
    if trackType == hiero.core.TrackItem.kAudio:
        return hiero.core.Transition.createAudioFadeOutTransition(hieroTrackItem, duration)
    else:
        return hiero.core.Transition.createFadeOutTransition(hieroTrackItem, duration)


def _createDissolveTransition(hieroTrackItemOut, duration1, duration2):
    if duration1 == 0 or duration2 == 0:
        raise RuntimeError('Dissolve with ' + ('in_offset' if duration1 ==
                           0 else 'out_offset') + ' of 0 not supported')

    hieroTransition = hiero.core.Transition()
    hieroTransition.setAlignment(hiero.core.Transition.kDissolve)
    hieroTransition.setTimelineIn(hieroTrackItemOut.timelineIn() - duration1)
    hieroTransition.setTimelineOut(hieroTrackItemOut.timelineIn() + duration2 - 1)
    return hieroTransition


def _getNukeMetadata(otioObject, key, defaultValue=None):
    """ Try to get a value from the 'nuke' dict in the object's metadata. Return defaultValue if it doesn't exist. """
    if 'nuke' in otioObject.metadata:
        return otioObject.metadata['nuke'].get(key, defaultValue)
    else:
        return defaultValue


def _markersFromObject(otioObject):
    """ Try to get the markers from an OTIO object. If it has a markers property return that, otherwise try to fetch
    them from the nuke metadata.
    """
    if hasattr(otioObject, 'markers'):
        return otioObject.markers
    else:
        return _getNukeMetadata(otioObject, 'markers', list())


def _effectsFromObject(otioObject):
    """ Try to get the effects from an OTIO object. If it has the effects property return that, otherwise try to fetch
    them from the nuke metadata.
    """
    if hasattr(otioObject, 'effects'):
        return otioObject.effects
    else:
        return _getNukeMetadata(otioObject, 'effects', list())


def _setReformatStateFromDict(reformatState: hiero.core.ReformatState, reformatStateDict: dict):
    """ Set reformat state params from the given dictionary
    """
    reformatState.setType(reformatStateDict['type'])
    reformatState.setResizeType(reformatStateDict['resize_type'])
    reformatState.setResizeCenter(reformatStateDict['resize_center'])


def _getTimecodeString(hieroSequence, time):
    """ Get the timecode string for the given time in the sequence.
    """
    return hiero.core.Timecode.timeToString(time,
                                            hieroSequence.framerate(),
                                            hiero.core.Timecode.kDisplayTimecode,
                                            False,
                                            hieroSequence.timecodeStart())


def _formatMessage(hieroTrack, time, message):
    """ Format the message used for warnings about track items.
    """
    if time is not None:
        timecode = _getTimecodeString(hieroTrack.parent(), time)
        return f"Track '{hieroTrack.name()}' @ {timecode}: {message}"
    else:
        return f"Track '{hieroTrack.name()}': {message}"


class OTIOBackgroundImporterImpl:
    """ Imports aspects of the OpenTimelineIO timeline that can be done in a background thread.
    Only operations that are safe to be performed on a background thread should be done by this object.
    This means UI modifications, node creation and access to knobs should not be done by this object.
    """

    def __init__(self, existingClips, project):
        # Maps a tuple of media properties to a Clip object
        self._registeredMedia = dict()

        # A dictionary of existing clips in the project with MediaSource objects as keys
        self._existingClips = existingClips

        # A list of warning messages from the import
        self._warningMessages = list()

        # Maps link group ids to track items
        self._linkGroups = dict()

        # Map otio objects to equivalent hiero objects
        self._otioObjectMapToHieroObjects = dict()

        # List of clips created that have media present paired with corresponding otioMediaReference
        self._createdClips = []

        # Default sequence output format used if the information is not in the OTIO
        self._defaultOutputFormat = project.outputFormat()

        # Default reformat state used if the information is not in the OTIO
        self._defaultReformatState = reformatStateToDict(project.trackItemReformatState())

        self._linkTrackItemVersionsToBin = project.trackItemVersionsLinkedToBin()

    def importTimeline(self, otioTimeline):
        # Generate a Hiero sequence from the OTIO timeline.
        sequenceTimecode, frameRate = _getSequenceProperties(otioTimeline)
        sequenceName = otioTimeline.name if otioTimeline.name else 'Imported OTIO Sequence'
        if not otioTimeline.name:
            self.addWarning("Timeline \'name\' field is empty, so setting a default name")
        hieroSequence = hiero.core.Sequence(sequenceName)
        hieroSequence.changeFramerateKeepFrames(frameRate)
        hieroSequence.setTimecodeStart(int(sequenceTimecode))

        # Get and set the sequence format
        self._addSequenceFormat(hieroSequence, otioTimeline)

        self._addTagsFromMarkers(hieroSequence, otioTimeline.tracks)

        # Import all tracks of the sequence.
        for otioTrack in otioTimeline.video_tracks():
            self._importTrack(otioTrack, hiero.core.TrackItem.kVideo, hieroSequence)
        for otioTrack in otioTimeline.audio_tracks():
            self._importTrack(otioTrack, hiero.core.TrackItem.kAudio, hieroSequence)

        return hieroSequence

    def addWarning(self, message):
        """ Log a warning message """
        self._warningMessages.append('WARNING: ' + message)

    def getWarningMessages(self):
        return self._warningMessages

    def _importTrack(self, otioTrack, trackType, hieroSequence):
        hieroTrack = hiero.core.VideoTrack(
            otioTrack.name) if trackType == hiero.core.TrackItem.kVideo else hiero.core.AudioTrack(otioTrack.name)
        self._otioObjectMapToHieroObjects[otioTrack] = hieroTrack

        hieroSequence.addTrack(hieroTrack)

        otioTrackItems = list(otioTrack)
        prevHieroTrackItem = None
        itemIndex = 0
        while itemIndex < len(otioTrackItems):
            otioItem = otioTrackItems[itemIndex]
            if isinstance(otioItem, otio.schema.Transition):
                try:
                    # Importing a transition may require importing the next item in the list, so _importTransition will return the
                    # correct index.
                    itemIndex, prevHieroTrackItem = self._importTransition(otioItem,
                                                                           otioTrackItems,
                                                                           trackType,
                                                                           itemIndex,
                                                                           prevHieroTrackItem,
                                                                           hieroTrack)
                except Exception as exc:
                    self.addWarning(_formatMessage(hieroTrack,
                                                   int(otioItem.range_in_parent().start_time.value),
                                                   f"Failed to import {otioItem}\n{exc}"))
            elif isinstance(otioItem, otio.schema.Clip):
                prevHieroTrackItem = self._importClip(otioItem, hieroTrack)
            elif isinstance(otioItem, otio.schema.Stack):
                self.addWarning(_formatMessage(hieroTrack,
                                               int(otioItem.range_in_parent().start_time.value),
                                               'Nested sequences are not currently supported'))
            elif isinstance(otioItem, otio.schema.Gap):
                pass
            else:
                self.addWarning(_formatMessage(hieroTrack,
                                               None,
                                               f"Encountered unsupported object '{type(otioItem).__name__}'"))
            itemIndex = itemIndex + 1

        hieroTrack.setEnabled(otioTrack.enabled)

        if trackType == hiero.core.TrackItem.kAudio:
            hieroTrack.setVolume(_getNukeMetadata(otioTrack, 'volume', 1.0))
            channel = _getNukeMetadata(otioTrack, 'channel')
            if channel is not None:
                hieroTrack.setChannel(hiero.core.AudioTrack.Channel(channel))
        else:
            hieroTrack.setBlendEnabled(_getNukeMetadata(otioTrack, 'blend_mode_enabled', False))
            hieroTrack.setBlendMaskEnabled(_getNukeMetadata(otioTrack, 'blend_mask_enabled', False))
            hieroTrack.setBlendMode(_getNukeMetadata(otioTrack, 'blend_mode', 'over'))

        self._addTagsFromMarkers(hieroTrack, otioTrack)

    def _importTransition(self, otioTransition, otioTrackItems, trackType, index, prevHieroTrackItem, hieroTrack):
        transitionType = _getTransitionType(otioTrackItems, index)

        nextHieroTrackItem = None
        if transitionType is not TransitionType.FADE_OUT:
            nextHieroTrackItem = self._importClip(otioTrackItems[index+1], hieroTrack)

        otioTrackItem = otioTrackItems[index]
        hieroTransition = None
        inOffset = int(otioTrackItem.in_offset.value)
        outOffset = int(otioTrackItem.out_offset.value)
        if transitionType == TransitionType.FADE_IN:
            duration = outOffset - inOffset
            hieroTransition = _createFadeInTransition(nextHieroTrackItem, duration, trackType)
        elif transitionType == TransitionType.FADE_OUT:
            duration = inOffset - outOffset
            hieroTransition = _createFadeOutTransition(prevHieroTrackItem, duration, trackType)
        else:
            hieroTransition = _createDissolveTransition(nextHieroTrackItem,
                                                        inOffset,
                                                        outOffset)
        hieroTrack.addTransition(hieroTransition)

        # dissolve node must be created on main thread, so this is done later
        # when we call hieroTransition.dissolveNode to set the which knob
        self._otioObjectMapToHieroObjects[otioTransition] = hieroTransition

        if transitionType is not TransitionType.FADE_OUT:
            index = index + 1
            prevHieroTrackItem = nextHieroTrackItem
        return index, prevHieroTrackItem

    def _importClip(self, otioClip, hieroTrack):
        try:
            trimmed_range = otioClip.trimmed_range()
        except otio.exceptions.CannotComputeAvailableRangeError:
            hiero.core.log.error(
                'Found opentimelineio.schema.Clip instance without a valid TimeRange.')
            return

        hieroTrackItem = hieroTrack.createTrackItem(otioClip.name)
        hieroTrackItem.setTimes(int(otioClip.range_in_parent().start_time.value),
                                int(otioClip.range_in_parent().end_time_inclusive().value),
                                trimmed_range.start_time.value,
                                trimmed_range.end_time_inclusive().value)

        self._otioObjectMapToHieroObjects[otioClip] = hieroTrackItem

        # Need to call setSourceIn in order for clips to conform correctly.
        try:
            hieroTrackItem.setSourceIn(
                int((trimmed_range.start_time - otioClip.available_range().start_time).value))
        except otio.exceptions.CannotComputeAvailableRangeError:
            hieroTrackItem.setSourceIn(0)

        hieroTrackItem.setPlaybackSpeed(_clipRetime(otioClip))
        hieroTrack.addTrackItem(hieroTrackItem)

        # Try importing the media reference of this clip, and set the clip media if this operation succeeds.
        self._importMedia(otioClip, hieroTrackItem)

        hieroTrackItem.setVersionLinkedToBin(self._linkTrackItemVersionsToBin)

        # Set Hiero TrackItem properties. Currently can only do this if the TrackItem has any media
        if hieroTrackItem.mediaType() == hiero.core.TrackItem.kVideo and hieroTrackItem.source():
            # Set the reformat state from the otioClip metadata if it exists, otherwise from project.
            otioReformatStateDict = _getNukeMetadata(
                otioClip, 'reformat_state', self._defaultReformatState)
            _setReformatStateFromDict(hieroTrackItem.reformatState(), otioReformatStateDict)
        elif hieroTrackItem.mediaType() == hiero.core.TrackItem.kAudio and hieroTrackItem.source():
            volume = _getNukeMetadata(otioClip, 'volume', 1.0)
            hieroTrackItem.setVolume(volume)

        hieroTrackItem.setEnabled(otioClip.enabled)
        self._addTagsFromMarkers(hieroTrackItem, otioClip)

        # If part of a link group, link with the other track items in the link group.
        linkGroupId = _getNukeMetadata(otioClip, 'link_group')
        if linkGroupId:
            linkTrackItem = self._linkGroups.get(linkGroupId)
            if linkTrackItem:
                hieroTrackItem.link(linkTrackItem)
            else:
                # First item in the group, save it so the other items can be linked.
                self._linkGroups[linkGroupId] = hieroTrackItem

        return hieroTrackItem

    def _importMedia(self, otioClip, hieroTrackItem):
        """ Create a Hiero Clip and set it on the TrackItem.
        The application currently expects that a TrackItem will always reference a Clip.
        If a path can't be determined from the media reference, one will be created using the name and other relevant data.
        This can then be used during conform to connect to the correct media.
        """
        mediaPath = None
        mediaName = None
        # OTIO Clips are expected to have a media reference of some sort, but just in case, allow for this not being the
        # case and use the data available on the clip
        otioMediaReference = otioClip.media_reference
        if otioMediaReference:
            try:
                mediaPath = _getMediaPath(otioMediaReference)
            except ValueError as v:
                self.addWarning(_formatMessage(hieroTrackItem.parent(),
                                hieroTrackItem.timelineIn(), str(v)))
                hiero.core.log.error(v)

            mediaName = otioMediaReference.name

            if hasattr(otioMediaReference, 'frame_step') and otioMediaReference.frame_step != 1:
                hiero.core.log.error('Unsupported media reference frame_step={} value found. 1 will be used instead.'.format(
                    otioMediaReference.frame_step))
            elif isinstance(otioMediaReference, otio.schema.GeneratorReference):
                hiero.core.log.error(
                    'otio.schema.GeneratorReference are currently treated as missing media.')
        else:
            self.addWarning(_formatMessage(hieroTrackItem.parent(),
                                           hieroTrackItem.timelineIn(),
                                           f"Clip '{otioClip.name}' has no media reference"))

        if not mediaName:
            mediaName = otioClip.name

        if not mediaPath:
            mediaPath = mediaName

        mediaStartTime, mediaFrameRate, mediaDuration = _getClipTimeData(otioClip)

        # Properties used for checking if two media references should be imported as the same clip.
        mediaKey = mediaPath, mediaStartTime, mediaDuration, mediaFrameRate.toInt()

        hieroClip = self._registeredMedia.get(mediaKey)
        # If the media key is not present in the dictionary, register the media and add it to the dictionary.
        if hieroClip is None:
            hieroClip = self._createOrFindHieroClip(mediaName,
                                                    mediaPath,
                                                    mediaStartTime,
                                                    mediaDuration,
                                                    mediaFrameRate,
                                                    otioMediaReference)
            self._registeredMedia[mediaKey] = hieroClip

        hieroTrackItem.setSource(hieroClip)
        if not hieroTrackItem.name():
            hieroTrackItem.setName(hieroClip.name())

    def _createOrFindHieroClip(self, mediaName, mediaPath, mediaStartTime, mediaDuration, mediaFrameRate, otioMediaReference):
        """ First check if a clip referencing the media already exists in the project, otherwise, create a Clip. """
        hieroMedia = hiero.core.MediaSource.createOfflineVideoMediaSource(mediaPath,
                                                                          mediaStartTime,
                                                                          mediaDuration,
                                                                          mediaFrameRate,
                                                                          mediaStartTime)
        colorspace = _getNukeMetadata(
            otioMediaReference, 'colorspace') if otioMediaReference else None

        # Create clip if it doesn't already exists in the project
        hieroClip = self._existingClips.get(hieroMedia)
        if not hieroClip:
            hieroClip = hiero.core.Clip(hieroMedia)
            if otioMediaReference:
                self._addTagsFromMarkers(hieroClip, otioMediaReference)

            if mediaName:
                hieroClip.setName(mediaName)

            if hieroMedia.isMediaPresent():
                # hieroClip read node must be created on main thread, this is done later
                # when the clip is added to the conform bin. Only then can we set the colorspace
                self._createdClips.append((hieroClip, otioMediaReference))

        return hieroClip

    kDefaultHieroTagIcon = 'Tag.png'

    def _createAndAddTagFromMarker(self, hieroObject, otioMarker, otioClipSourceStartTime):
        """ Try to create a Tag from a Marker and add it to the given object. """
        otioMeta = otioMarker.metadata
        otioNukeMeta = otioMeta.get('nuke')

        # Handle markers not written by Nuke
        if not otioNukeMeta:
            tagVisibility = True
            tagIcon = 'icons:' + kOtioMarkerColorMappedToHieroTagIcons.get(otioMarker.color.upper(),
                                                                           self.kDefaultHieroTagIcon)
        else:
            tagVisibility = bool(otioNukeMeta['visible'])
            tagIcon = otioNukeMeta['icon']

        # Create the tag and add it to the object.
        # Need to add the tag then set the metadata on the returned object, otherwise things can go wrong if there are
        # multiple tags with the same name.
        hieroTag = hiero.core.Tag(otioMarker.name, tagIcon)
        markerHasDuration = otioMarker.marked_range.duration.value > 0
        if markerHasDuration:
            start, end = _getMarkerTimeData(otioMarker, otioClipSourceStartTime)
            hieroTag = hieroObject.addTagToRange(hieroTag, start, end)
        else:
            hieroTag = hieroObject.addTag(hieroTag)

        hieroTag.setVisible(tagVisibility)

        if otioNukeMeta:
            hieroMeta = hieroTag.metadata()
            for key, value in otioNukeMeta.items():
                if key.startswith('tag.'):
                    hieroMeta.setValue(key, str(value))

    def _addTagsFromMarkers(self, hieroObject, otioObject):
        otioMarkers = _markersFromObject(otioObject)
        otioClipSourceStartTime = _getClipTimeData(
            otioObject)[0] if isinstance(otioObject, otio.schema.Clip) else None
        for otioMarker in otioMarkers:
            self._createAndAddTagFromMarker(hieroObject, otioMarker, otioClipSourceStartTime)

    def _addSequenceFormat(self, hieroSequence, otioTimeline):
        sequenceFormat = self._defaultOutputFormat
        sequenceFormatString = _getNukeMetadata(otioTimeline, 'format')
        if sequenceFormatString:
            try:
                sequenceFormatFromString = hiero.core.Format(sequenceFormatString)
                if sequenceFormatFromString.isValid():
                    sequenceFormat = sequenceFormatFromString
            except:
                self.addWarning(
                    'Encountered an error while fetching the timeline format. The format will set to the project default.')
        hieroSequence.setFormat(sequenceFormat)


class OTIOImporterImpl:
    """ Imports an OpenTimelineIO timeline into Nuke. """

    def __init__(self, destBinItem):
        # Find existing clips in the project and create a dictionary with MediaSource objects as key
        existingClips = hiero.core.findItemsInProject(destBinItem.project(), hiero.core.Clip)
        self._existingClips = {
            clip.mediaSource(): clip for clip in existingClips if clip.mediaSource().isMediaPresent()}

        # Bin to place new clips and sequences into
        self._destBinItem = destBinItem

        # A list of warning messages from the import
        self._warningMessages = list()

        # Map otio objects to equivalent hiero objects
        self._otioObjectMapToHieroObjects = dict()

    def importTimeline(self, otioTimeline):
        # Generate a Hiero sequence from the OTIO timeline.
        backgroundImporter = OTIOBackgroundImporterImpl(self._existingClips,
                                                        self._destBinItem.project())
        hieroSequence = runFunctionInBackgroundThread(backgroundImporter.importTimeline,
                                                      otioTimeline)

        self._warningMessages = backgroundImporter.getWarningMessages()

        self._otioObjectMapToHieroObjects = backgroundImporter._otioObjectMapToHieroObjects

        # Update all tracks of the sequence.
        for otioTrack in otioTimeline.video_tracks():
            self._updateTrack(otioTrack)
        for otioTrack in otioTimeline.audio_tracks():
            self._updateTrack(otioTrack)

        # Handle clips to add to conform bin
        for hieroClip, otioMediaReference in backgroundImporter._createdClips:
            self._handleCreatedClips(hieroClip, otioMediaReference)

        return hieroSequence

    def importToNewSequence(self, otioTimeline):
        hieroSequence = self.importTimeline(otioTimeline)
        sequenceBinItem = hiero.core.BinItem(hieroSequence)
        self._destBinItem.addItem(sequenceBinItem)
        return hieroSequence

    def importToExistingSequence(self, otioTimeline, existingHieroSequence):
        newHieroSequence = self.importTimeline(otioTimeline)

        # Map imported track to track added to existing sequence.
        # Required to relink added track items.
        trackMapping = {}

        # Copy tracks to the existing sequence
        for hieroTrack in newHieroSequence.videoTracks():
            trackMapping[hieroTrack] = existingHieroSequence.addTrack(hieroTrack.copy())
        for hieroTrack in newHieroSequence.audioTracks():
            trackMapping[hieroTrack] = existingHieroSequence.addTrack(hieroTrack.copy())

        # Re-create track item links in the newly added tracks.
        # Go through the original imported track items and their linked items.
        for track in trackMapping:
            for trackItemIndex, trackItem in enumerate(track):
                for linkedItem in trackItem.linkedItems():
                    if isinstance(linkedItem, hiero.core.TrackItem):
                        # Get the added track item (in the existing sequence) that
                        # corresponds to the imported track item we're looking at.
                        addedTrack = trackMapping[track]
                        addedTrackItem = addedTrack[trackItemIndex]

                        # Now need to find the added item that corresponds to the linked item.
                        addedLinkTrack = trackMapping[linkedItem.parent()]
                        for addedLinkItem in addedLinkTrack:
                            if addedLinkItem.timelineIn() == linkedItem.timelineIn():
                                if not addedTrackItem.isLinked(addedLinkItem):
                                    addedTrackItem.link(addedLinkItem)
                                break

    def addWarning(self, message):
        """ Log a warning message """
        self._warningMessages.append('WARNING: ' + message)

    def getWarningMessages(self):
        return self._warningMessages

    def _updateTrack(self, otioTrack):
        hieroTrack = self._otioObjectMapToHieroObjects.get(otioTrack)

        otioTrackItems = list(otioTrack)
        for otioItem in otioTrackItems:
            if isinstance(otioItem, otio.schema.Transition):
                self._updateTransition(otioItem)
            elif isinstance(otioItem, otio.schema.Clip):
                self._updateClip(otioItem, hieroTrack)

        self._createAndAddTrackEffects(hieroTrack, None, otioTrack.effects)
        hieroTrack.setLocked(_getNukeMetadata(otioTrack, 'locked', False))

    def _updateTransition(self, otioTransition):
        hieroTransition = self._otioObjectMapToHieroObjects.get(otioTransition)
        whichKnobScript = _getNukeMetadata(otioTransition, 'which')
        if whichKnobScript:
            hieroTransition.dissolveNode()['which'].fromScript(whichKnobScript)

    def _updateClip(self, otioClip, hieroTrack):
        hieroTrackItem = self._otioObjectMapToHieroObjects.get(otioClip)
        self._handleExistingMedia(otioClip, hieroTrackItem)
        self._createAndAddTrackEffects(hieroTrack, hieroTrackItem, otioClip.effects)

    def _handleExistingMedia(self, otioClip, hieroTrackItem):
        """ Check if the media source set on the hieroTrackItem already existed in the project
        and warn the user if the otioMediaReference in the otioClip has conflicting colourspace or metadata. """
        source = hieroTrackItem.source()

        if source and source.mediaSource():
            hieroMedia = source.mediaSource()
            otioMediaReference = otioClip.media_reference

            # Check if the clip already exists in the project
            hieroClip = self._existingClips.get(hieroMedia)
            if hieroClip:
                existingClipWarnings = []
                if _markersFromObject(otioMediaReference):
                    existingClipWarnings.append('Ignoring markers from OTIO media reference')
                if _effectsFromObject(otioMediaReference):
                    existingClipWarnings.append('Ignoring effects from OTIO media reference')

                existingColorspace = hieroClip.readNode()['colorspace'].toScript()
                colorspace = _getNukeMetadata(
                    otioMediaReference, 'colorspace') if otioMediaReference else None

                mediaPath = hieroClip.mediaSource().fileinfos()[0].filename()
                if colorspace and existingColorspace != colorspace:
                    existingClipWarnings.append(f"Clip has colorspace '{
                                                existingColorspace}', OTIO media reference has colorspace '{colorspace}'")
                if existingClipWarnings:
                    existingClipWarnings.insert(0,
                                                _formatMessage(hieroTrackItem.parent(),
                                                               hieroTrackItem.timelineIn(),
                                                               f"Found existing clip for path '{mediaPath}':"))
                    self.addWarning('\n'.join(existingClipWarnings))

    def _handleCreatedClips(self, hieroClip, otioMediaReference):
        """ Add created Clips to the 'Conform' bin if the media can be found.
        This will cause the clip to be attached to the project and readNode created.
        After which, the colorspace can be set. """

        colorspace = _getNukeMetadata(
            otioMediaReference, 'colorspace') if otioMediaReference else None

        if hieroClip.mediaSource().isMediaPresent():
            # Add the "Conform" bin if it doesn't already exist.
            if 'Conform' in self._destBinItem:
                conformBin = self._destBinItem['Conform']
            else:
                conformBin = hiero.core.Bin('Conform')
                self._destBinItem.addItem(conformBin)

            # Add to bin
            clipBinItem = hiero.core.BinItem(hieroClip)
            conformBin.addItem(clipBinItem)

            if colorspace:
                hieroClip.readNode()['colorspace'].fromScript(colorspace)

            otioEffects = _effectsFromObject(otioMediaReference)
            for otioEffect in otioEffects:
                hieroEffect = hieroClip.createEffect(otioEffect.effect_name)
                self._configureEffect(hieroEffect, otioEffect)

            QCoreApplication.processEvents()

    def _createAndAddTrackEffects(self, hieroTrack, hieroTrackItem, otioEffects):
        """ Try to create track effects from an OTIO effects """
        subTrackIndex = 0
        for otioEffect in otioEffects:
            # Ignore LinearTimeWarp effects, they are handled as retimes
            if isinstance(otioEffect, otio.schema.LinearTimeWarp):
                continue
            otioMeta = otioEffect.metadata
            otioNukeMeta = otioMeta.get('nuke')
            # Ignore effects not written by Nuke for now
            if not otioNukeMeta:
                self.addWarning(_formatMessage(hieroTrack,
                                               hieroTrackItem.timelineIn() if hieroTrackItem else 0,
                                               f"Effect '{otioEffect.name}': Import of effect not exported from Nuke is not yet supported"))
                continue

            if hieroTrackItem:
                # Create track item effect
                hieroEffect = hieroTrack.createEffect(effectType=otioEffect.effect_name,
                                                      trackItem=hieroTrackItem,
                                                      subTrackIndex=subTrackIndex)
                subTrackIndex += 1
            else:
                # Create track effect
                timelineRange = otioNukeMeta['timeline_range']
                timelineIn = int(timelineRange.start_time.value)
                timelineOut = int(timelineRange.end_time_inclusive().value)
                hieroEffect = hieroTrack.createEffect(effectType=otioEffect.effect_name,
                                                      subTrackIndex=otioNukeMeta['sub_track_index'],
                                                      timelineIn=timelineIn,
                                                      timelineOut=timelineOut)

            self._configureEffect(hieroEffect, otioEffect)

        if otioEffects:
            QCoreApplication.processEvents()

    def _configureEffect(self, hieroEffect, otioEffect):
        """ Set the knob values on a hiero effect based on the properties of an OTIO effect"""
        otioNukeMeta = otioEffect.metadata.get('nuke')

        hieroEffect.setName(otioEffect.name)

        # Set enabled if disabled state is false.
        hieroEffect.setEnabled(_getNukeMetadata(otioEffect, 'disable', 'false') == 'false')

        # Set the knob values
        hieroEffectNode = hieroEffect.node()
        for key, value in otioNukeMeta.items():
            if key in hieroEffectNode.knobs():
                hieroEffectNode[key].fromScript(value)


class OtioImporter:
    """
    Implements the member functions required for an importer.
    """

    def __init__(self):
        self._warningMessages = list()

    def displayName(self):
        return 'Foundry OpenTimelineIO Importer'

    def isOptionRequired(self, _):
        return False

    def isValidFile(self, filePath):
        if not os.path.isfile(filePath):
            return False
        _, extension = os.path.splitext(filePath)
        return extension.lower() == '.otio'

    def importToNewSequence(self, filePath, destBinItem):
        otioTimeline = self._getOtioTimeline(filePath)
        if otioTimeline:
            importerImpl = OTIOImporterImpl(destBinItem)
            hieroSequence = importerImpl.importToNewSequence(otioTimeline)
            self._warningMessages = importerImpl.getWarningMessages()
            return hieroSequence

    def importToExistingSequence(self, filePath, hieroSequence):
        otioTimeline = self._getOtioTimeline(filePath)
        if otioTimeline:
            proj = hieroSequence.project()
            bin = proj.clipsBin()
            importerImpl = OTIOImporterImpl(bin)
            importerImpl.importToExistingSequence(otioTimeline, hieroSequence)
            self._warningMessages = importerImpl.getWarningMessages()

    def getWarningMessages(self):
        return self._warningMessages

    def _getOtioTimeline(self, filePath):
        return runFunctionInBackgroundThread(_readOpenTimelineIOFile,
                                             filePath)
