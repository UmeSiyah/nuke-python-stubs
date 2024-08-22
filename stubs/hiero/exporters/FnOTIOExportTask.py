# Copyright (c) 2022 The Foundry Visionmongers Ltd. All Rights Reserved.

import os
import uuid
import traceback

import hiero.core
import nuke_internal as nuke
import opentimelineio as otio
from PySide2.QtCore import QUrl
from hiero.core.FnEffectHelpers import reformatStateToDict
from hiero.core.FnCompSourceInfo import CompSourceInfo
from hiero.core.FnOtioMarkerColorMapping import \
    kOtioMarkerColorMappedToHieroTagIcons


def _addNukeMetadata(otioObject, **kwargs):
    """ Update the object's 'nuke' metadata dictionary with the data in **kwargs """
    if 'nuke' not in otioObject.metadata:
        otioObject.metadata['nuke'] = kwargs
    else:
        otioObject.metadata['nuke'].update(kwargs)


class OTIOTimelineBuilder:
    """ Helper class for creating an otio.schema.Timeline from a hiero.core.Sequence
    object.
    """

    # A list of all the knobs to be excluded from the export
    kKnobsToExclude = ['help', 'lifetimeStart', 'lifetimeEnd', 'useLifetime']

    def __init__(self, hieroSequence, writeCompRenderPaths, includeEffects):
        self._hieroSequence = hieroSequence
        self._warnings = []
        # Maps track items to link group ids
        self._linkGroupIds = dict()
        self._writeCompRenderPaths = writeCompRenderPaths
        self._includeEffects = includeEffects

    def buildTimeline(self):
        """ Create the timeline """
        otioTimeline = otio.schema.Timeline(name=self._hieroSequence.name())
        otioTimeline.global_start_time = self._makeTime(self._hieroSequence.timecodeStart())

        # Add some metadata about the Nuke version and sequence format
        _addNukeMetadata(otioTimeline, version=nuke.env['NukeVersionString'])
        _addNukeMetadata(otioTimeline, format=self._hieroSequence.format().toString())

        self._addMarkersToObject(otioTimeline.tracks, self._hieroSequence)

        for track in self._hieroSequence.videoTracks():
            otioTimeline.tracks.append(self._buildTrack(track))
        for track in self._hieroSequence.audioTracks():
            otioTimeline.tracks.append(self._buildTrack(track))
        return otioTimeline

    def warnings(self):
        """ Get the list of warnings from building the timeline """
        return self._warnings

    def _addWarning(self, msg):
        """ Add a warning """
        self._warnings.append(msg)

    def _makeTime(self, frame, framerate=None):
        # Create a RationalTime object, if framerate not given uses the sequence rate
        framerate = framerate or self._hieroSequence.framerate().toFloat()
        return otio.opentime.RationalTime(frame, framerate)

    def _makeRange(self, start, duration, framerate=None):
        # Create a TimeRange object from values or RationalTime objects.
        # If framerate not given uses the sequence rate
        if not isinstance(start, otio.opentime.RationalTime):
            start = self._makeTime(start, framerate)
        if not isinstance(duration, otio.opentime.RationalTime):
            duration = self._makeTime(duration, framerate)
        return otio.opentime.TimeRange(start_time=start, duration=duration)

    def _buildTrack(self, hieroTrack):
        # Create an OTIO Track from a Hiero one
        otioTrack = otio.schema.Track(name=hieroTrack.name())
        otioTrack.kind = 'Video' if isinstance(hieroTrack, hiero.core.VideoTrack) else 'Audio'
        otioTrack.enabled = hieroTrack.isEnabled()
        _addNukeMetadata(otioTrack, locked=hieroTrack.isLocked())

        if otioTrack.kind == 'Audio':
            _addNukeMetadata(otioTrack,
                             volume=hieroTrack.volume(),
                             channel=int(hieroTrack.channel()))
        else:
            _addNukeMetadata(otioTrack, blend_mode_enabled=hieroTrack.isBlendEnabled())
            _addNukeMetadata(otioTrack, blend_mask_enabled=hieroTrack.isBlendMaskEnabled())
            _addNukeMetadata(otioTrack, blend_mode=hieroTrack.blendMode())

        self._addMarkersToObject(otioTrack, hieroTrack)
        self._addTrackEffects(otioTrack, hieroTrack)
        prevHieroTrackItem = None
        for hieroTrackItem in hieroTrack:
            # Add gaps if needed
            gap = hieroTrackItem.timelineIn() if not prevHieroTrackItem else hieroTrackItem.timelineIn() - \
                (prevHieroTrackItem.timelineOut()+1)
            if gap:
                otioTrack.append(otio.schema.Gap(source_range=self._makeRange(0, gap)))

            inTransition = hieroTrackItem.inTransition()
            if inTransition:
                self._appendTransition(otioTrack, inTransition, prevHieroTrackItem)

            otioTrack.append(self._buildClip(hieroTrackItem))

            # Because a dissolve will be the inTransition of the next hieroTrackItem, ignore the current track item's
            # outTransition if it is a dissolve.
            outTransition = hieroTrackItem.outTransition()
            if outTransition and outTransition.alignment() != hiero.core.Transition.Alignments.kDissolve:
                self._appendTransition(otioTrack, outTransition, prevHieroTrackItem)

            prevHieroTrackItem = hieroTrackItem
        return otioTrack

    def _buildClip(self, hieroTrackItem):
        # Create an OTIO Clip from a Hiero TrackItem
        hieroClip = hieroTrackItem.source()
        # If the frame rates do not match, store the start in the source rate and the
        # duration at the sequence rate. Unsure if this is correct, but it seems the
        # only way for this to work
        if hieroClip.framerate() != self._hieroSequence.framerate():
            self._addWarning("Clip '{}' frame rate {} does not match sequence".format(
                hieroClip.name(), hieroClip.framerate()))
        srcStartTime = self._makeTime(hieroClip.timecodeStart(
        ) + hieroTrackItem.sourceIn(), framerate=hieroClip.framerate().toFloat())
        srcRange = self._makeRange(srcStartTime, hieroTrackItem.duration())
        otioMediaRef = self._buildMediaReference(hieroClip)
        otioClip = otio.schema.Clip(name=hieroTrackItem.name(),
                                    media_reference=otioMediaRef,
                                    source_range=srcRange)
        otioClip.enabled = hieroTrackItem.isEnabled()
        self._addMarkersToObject(otioClip, hieroTrackItem)
        self._addTrackItemProperties(otioClip, hieroTrackItem)
        self._addClipEffects(otioClip, hieroTrackItem)

        # If the track item is linked to other track items, record a unique id for
        # the link group.
        linkGroupId = self._linkGroupIds.get(hieroTrackItem)
        if linkGroupId:
            # Track item is part of an identified link group, use the link id.
            _addNukeMetadata(otioClip, link_group=linkGroupId)
        else:
            # Track item is not part of identified link group, if it is linked, find
            # the items and generate an id for the link group.
            linkGroupId = str(uuid.uuid4())
            hasLink = False
            for linkedHieroItem in hieroTrackItem.linkedItems():
                if isinstance(linkedHieroItem, hiero.core.TrackItem):
                    hasLink = True
                    self._linkGroupIds[linkedHieroItem] = linkGroupId
            if hasLink:
                _addNukeMetadata(otioClip, link_group=linkGroupId)

        return otioClip

    def _buildEffect(self, hieroEffect):
        effectNode = hieroEffect.node()
        otioKnobDict = {}
        for knobName, knobObj in effectNode.knobs().items():
            if knobObj.name() and not knobObj.getFlag(nuke.DO_NOT_WRITE) and not knobName in OTIOTimelineBuilder.kKnobsToExclude:
                if knobObj.notDefault():
                    otioKnobDict[knobName] = knobObj.toScript()
        otioEffect = otio.schema.Effect(name=hieroEffect.name(),
                                        effect_name=effectNode.Class())
        otioEffect.metadata['nuke'] = otioKnobDict
        return otioEffect

    def _appendTransition(self, otioTrack, hieroTransition, prevHieroTrackItem):
        duration = hieroTransition.timelineOut() - hieroTransition.timelineIn()
        if hieroTransition.alignment() == hiero.core.Transition.Alignments.kDissolve:
            inOffset = prevHieroTrackItem.timelineOut() - hieroTransition.timelineIn() + 1
            outOffset = duration - inOffset + 1
        elif hieroTransition.alignment() == hiero.core.Transition.Alignments.kFadeIn:
            inOffset = 0
            outOffset = duration + 1
            otioTrack.append(otio.schema.Gap(source_range=self._makeRange(0, 0)))
        elif hieroTransition.alignment() == hiero.core.Transition.Alignments.kFadeOut:
            inOffset = duration + 1
            outOffset = 0

        otioTransition = otio.schema.Transition(name='Transition',
                                                transition_type='SMPTE_Dissolve',
                                                in_offset=self._makeTime(inOffset),
                                                out_offset=self._makeTime(outOffset))
        whichKnob = hieroTransition.dissolveNode()['which']
        _addNukeMetadata(otioTransition, which=whichKnob.toScript())
        otioTrack.append(otioTransition)

        if hieroTransition.alignment() == hiero.core.Transition.Alignments.kFadeOut:
            otioTrack.append(otio.schema.Gap(source_range=self._makeRange(0, 0)))

    def _buildMediaReference(self, clip):
        # Create an OTIO MediaReference from a Hiero Clip
        mediaSource = clip.mediaSource()
        sourceRange = self._makeRange(mediaSource.timecodeStart(
        ), mediaSource.duration(), framerate=clip.framerate().toFloat())

        # If the clip is a comp container, check if the render path should be written instead of the nk path
        if self._writeCompRenderPaths:
            compInfo = CompSourceInfo(mediaSource)
            if compInfo.isComp():
                mediaSource = hiero.core.MediaSource(compInfo.writePath)

        if mediaSource.singleFile():
            # Single media file, create an ExternalReference
            path = mediaSource.firstpath()
            url = QUrl.fromLocalFile(path).toString(QUrl.FullyEncoded)
            otioMedia = otio.schema.ExternalReference(target_url=url, available_range=sourceRange)
        else:
            # Image file sequence, create an ImageSequenceReference
            fileInfo = mediaSource.fileinfos()[0]
            namePrefix = mediaSource.filenameHead()
            dirPath, _ = os.path.split(fileInfo.filename())
            _, nameSuffix = os.path.splitext(fileInfo.filename())
            otioMedia = otio.schema.ImageSequenceReference(
                available_range=sourceRange,
                start_frame=fileInfo.startFrame(),
                frame_step=1,
                rate=clip.framerate().toFloat(),
                target_url_base=QUrl.fromLocalFile(dirPath).toString(QUrl.FullyEncoded),
                name_prefix=namePrefix,
                name_suffix=nameSuffix,
                frame_zero_padding=mediaSource.filenamePadding())
        self._addMarkersToObject(otioMedia, clip)

        try:
            colorspaceKnob = clip.readNode()['colorspace']
            if colorspaceKnob.notDefault():
                _addNukeMetadata(otioMedia, colorspace=colorspaceKnob.toScript())
        except:
            pass  # If the clip doesn't have a Read node an exception will be raised, ignore it

        # Export clip level effects
        if self._includeEffects:
            otioEffects = []
            for hieroEffect in clip.effects():
                # For effects on disabled tracks, write the effect as disabled
                if not hieroEffect.parentTrack().isEnabled():
                    hieroEffect.setEnabled(False)
                otioEffects.append(self._buildEffect(hieroEffect))
            if otioEffects:
                _addNukeMetadata(otioMedia, effects=otioEffects)

        return otioMedia

    _tagMetadataKeysToSkip = set(('tag.start', 'tag.length'))

    kHieroTagIconsMappedToOtioMarkerColor = dict(
        ('icons:'+value, key) for key, value in kOtioMarkerColorMappedToHieroTagIcons.items())

    def _otioMarkersFromTags(self, hieroTags, tagStartTimeOffset):
        """ Create OTIO Marker objects from a list of tags. tagStartOffset will be
        added to the start time of tags that don't apply to the whole object.
        """
        otioMarkers = []
        for hieroTag in hieroTags:
            hieroMeta = hieroTag.metadata()
            if hieroTag.name() == 'Copy' and hieroMeta.hasKey('tag.guid'):  # Skip tags added by export code
                continue
            otioMarker = otio.schema.Marker(name=hieroTag.name())
            hieroMetaDict = hieroTag.metadata().dict()
            # Set the range if the tag has one, otherwise marked_range will be left at the default of 0 for start and duration
            if hieroMetaDict.get('tag.applieswhole') == '0':
                otioMarker.marked_range = self._makeRange(int(hieroMetaDict['tag.start']) + tagStartTimeOffset,
                                                          int(hieroMetaDict['tag.length']))

            otioColor = self.kHieroTagIconsMappedToOtioMarkerColor.get(hieroTag.icon(), None)
            if otioColor:
                otioMarker.color = otioColor

            otioMetaDict = {}
            otioMetaDict['icon'] = hieroTag.icon()
            otioMetaDict['visible'] = hieroTag.visible()
            for key, value in hieroMetaDict.items():
                if key not in OTIOTimelineBuilder._tagMetadataKeysToSkip:
                    otioMetaDict[key] = value
            _addNukeMetadata(otioMarker, **otioMetaDict)
            otioMarkers.append(otioMarker)
        return otioMarkers

    def _addMarkersToObject(self, otioObject, hieroObject):
        """ Add the tags for a Hiero object as markers on an OTIO object. Not all OTIO types currently have a markers property,
        in this case they will be added to the object's metadata under nuke/markers
        """
        clipTimeCodeStart = int(hieroObject.source().timecodeStart()) if isinstance(
            hieroObject, hiero.core.TrackItem) else 0
        otioMarkers = self._otioMarkersFromTags(hieroObject.tags(), clipTimeCodeStart)
        if otioMarkers:
            if hasattr(otioObject, 'markers'):
                otioObject.markers.extend(otioMarkers)
            else:
                _addNukeMetadata(otioObject, markers=otioMarkers)

    def _addTrackEffects(self, otioTrack, hieroTrack):
        """ Add Hiero track level effects to the OTIO track effects list.
        """
        # Only video tracks have track effects.
        if not isinstance(hieroTrack, hiero.core.VideoTrack):
            return

        # Effect tracks have no track items.
        if hieroTrack.numItems() != 0:
            return

        # Go through the subtracks and add any effects.
        if self._includeEffects:
            for hieroSubTrack in hieroTrack.subTrackItems():
                for hieroSubTrackItem in hieroSubTrack:
                    if not isinstance(hieroSubTrackItem, hiero.core.EffectTrackItem):
                        continue
                    # Create the OITO effect from the hiero effect.
                    otioEffect = self._buildEffect(hieroSubTrackItem)
                    # Add additional metadata that is required for track effects.
                    effectRange = self._makeRange(hieroSubTrackItem.timelineIn(),
                                                  (hieroSubTrackItem.timelineOut() - hieroSubTrackItem.timelineIn()) + 1)
                    _addNukeMetadata(otioEffect,
                                     timeline_range=effectRange,
                                     sub_track_index=hieroSubTrackItem.subTrackIndex())
                    otioTrack.effects.append(otioEffect)

    def _addClipEffects(self, otioClip, hieroTrackItem):
        """ Add hiero track item effects to the OTIO clip effects list.
        """
        if hieroTrackItem.mediaType() == hiero.core.TrackItem.kVideo:
            # Handle retimes
            speed = hieroTrackItem.playbackSpeed()
            if speed == 0.0:
                otioClip.effects.append(otio.schema.FreezeFrame())
            elif speed != 1.0:
                otioClip.effects.append(otio.schema.LinearTimeWarp(time_scalar=speed))

            # Handle soft effects
            if self._includeEffects:
                for linkedHieroItem in hieroTrackItem.linkedItems():
                    if isinstance(linkedHieroItem, hiero.core.EffectTrackItem):
                        if linkedHieroItem.parent() == hieroTrackItem.parent():
                            if linkedHieroItem.timelineIn() == hieroTrackItem.timelineIn():
                                otioEffect = self._buildEffect(linkedHieroItem)
                                otioClip.effects.append(otioEffect)

    def _addTrackItemProperties(self, otioClip, hieroTrackItem):
        """ Add Hiero TrackItem reformat state for video TrackItem or volume
        for audio TrackItem to the OTIO clip metadata.
        """
        if hieroTrackItem.mediaType() == hiero.core.TrackItem.kVideo:
            otioReformatStateDict = reformatStateToDict(hieroTrackItem.reformatState())
            _addNukeMetadata(otioClip, reformat_state=otioReformatStateDict)
        elif hieroTrackItem.mediaType() == hiero.core.TrackItem.kAudio:
            _addNukeMetadata(otioClip, volume=hieroTrackItem.volume())


class OTIOExportTask(hiero.core.TaskBase):
    """ Export task for exporting a Sequence as an OTIO file """

    def __init__(self, initDict):
        hiero.core.TaskBase.__init__(self, initDict)

    def startTask(self):
        pass

    def taskStep(self):
        return False

    def finishTask(self):
        try:
            # Create the OTIO Timeline structure and write to the target file
            builder = OTIOTimelineBuilder(self._sequence,
                                          self._preset.properties()['writeCompRenderPaths'],
                                          self._preset.properties()['includeEffects'])
            otioTimeline = builder.buildTimeline()
            if builder.warnings():
                self.setWarning('\n'.join(builder.warnings()))
            exportPath = self.resolvedExportPath()
            # check export root exists
            dir = os.path.dirname(exportPath)
            hiero.core.util.filesystem.makeDirs(dir)
            otio.adapters.write_to_file(otioTimeline, exportPath)
        except Exception as e:
            self.setError(traceback.format_exc())
        hiero.core.TaskBase.finishTask(self)


class OTIOExportPreset(hiero.core.TaskPresetBase):
    """ Export preset for OTIO file export """

    def __init__(self, name, properties):
        hiero.core.TaskPresetBase.__init__(self, OTIOExportTask, name)

        self.properties()['writeCompRenderPaths'] = True
        self.properties()['includeEffects'] = True

        # Update preset with loaded data
        self.properties().update(properties)

    def supportedItems(self):
        return hiero.core.TaskPresetBase.kSequence

    def addCustomResolveEntries(self, resolver):
        resolver.addResolver('{ext}', 'Extension of the file to be output',
                             lambda keyword, task: 'otio')

    def supportsAudio(self):
        return True

    def exportsAllTracks(self):
        return True


hiero.core.taskRegistry.registerTask(OTIOExportPreset, OTIOExportTask)
