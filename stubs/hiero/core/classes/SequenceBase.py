"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class SequenceBase:
    """
    Base class for Sequence and Clip objects. Has some methods common to both of those objects. Most likely never used directly.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def __lt__(self, value, ) -> None:
        """
        Return self<value.
        """
        ...

    def __le__(self, value, ) -> None:
        """
        Return self<=value.
        """
        ...

    def __eq__(self, value, ) -> None:
        """
        Return self==value.
        """
        ...

    def __ne__(self, value, ) -> None:
        """
        Return self!=value.
        """
        ...

    def __gt__(self, value, ) -> None:
        """
        Return self>value.
        """
        ...

    def __ge__(self, value, ) -> None:
        """
        Return self>=value.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def __bool__(self) -> bool:
        """
        True if self else False
        """
        ...

    def activePlayhead(self,) -> int:
        """
        activePlayhead() -> Returns the index of the active playhead.
        """
        ...

    def addTag(self, tag) -> Tag:
        """
        self.addTag(tag) -> adds a hiero.core.Tag object to the Clip or Sequence.

        @param tag: the tag object to add
        @return: hiero.core.Tag object
        """
        ...

    def addTagToRange(self, tag, inTime: int | float, outTime: int | float) -> Tag:
        """
        self.addTagToRange(tag, inTime, outTime) -> adds a hiero.core.Tag object to the specified range of the Clip or Sequence.

        @param tag: the tag object to add
        @param inTime: the first time at which the tag is valid
        @param outTime: the last time at which the tag is valid
        @return: hiero.core.Tag object
        """
        ...

    def autoDiskCacheMode(self,) -> Iterable:
        """
        self.autoDiskCacheMode() -> returns the auto disk cache mode of the Sequence or Clip.

        @return: hiero.core.SequenceAutoDiskCacheMode
        """
        ...

    def binItem(self,) -> Optional[BinItem]:
        """
        self.binItem() -> returns the parent BinItem this Sequence or Clip belongs to, if any.

        @return: BinItem
        """
        ...

    def clearInTime(self, t) -> None:
        """
        self.clearInTime(t) -> clear the 'in' point for the clip to Time t.

        @return: None
        """
        ...

    def clearInTime(self, t) -> None:
        """
        self.clearInTime(t) -> clear the 'out' point for the clip to Time t.

        @return: None
        """
        ...

    def clearPlayheadInTime(self, index: int) -> None:
        """
        clearPlayheadInTime(index) -> Clear the in marker time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @return: None
        """
        ...

    def clearPlayheadOutTime(self, index: int) -> None:
        """
        clearPlayheadOutTime(index) -> Clear the out marker time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @return: None
        """
        ...

    def clearRange(self, start: int | float, end: int | float, ripple: bool) -> Iterable:
        """
        self.clearRange(start, end, ripple) -> Clears a time range out of the sequence; effectively a razor on any clips straddling the start and end, and a delete of everything else.

        @param start: the start of the range to clear
        @param end: the end of the range to clear
        @param ripple: set to True to shift the remaining track items to the left
        """
        ...

    def disableSoftTrims(self,) -> Any:
        """
        self.disableSoftTrims() -> disables soft trims on the object.
        """
        ...

    def dropFrame(self,) -> int:
        """
        self.dropFrame() -> get whether sequence timecode is displayed in drop frame format
        """
        ...

    def duration(self,) -> int:
        """
        self.duration() -> returns the duration of the Clip or Sequence.

        @return: int time value
        """
        ...

    def editFinished(self, trackItems=None) -> list:
        """
        self.editFinished(trackItems) -> this should be called after finishing editing the sequence to ensure that its internal state is updated properly and to send a signal to all objects listening to changes in this object (e.g. UI views).This function optionally takes a list of track items that is used to selectively rebuild only those sections of the timeline.This allows a faster update when the edited track items are known.

        @param trackItems: optional, the track items to be updated
        """
        ...

    def enableSoftTrims(self, inTime: int | float, outTime: int | float) -> Any:
        """
        self.enableSoftTrims(inTime, outTime) -> enables soft trims on the object.

        @param inTime: Time - soft trim in time
        @param outTime: Time - soft trim out time
        """
        ...

    def format(self,) -> Format:
        """
        self.format() -> returns the output Format object for this Sequence or Clip.

        @return: hiero.core.Format object
        """
        ...

    def framerate(self,) -> int | float:
        """
        self.framerate() -> returns the framerate of the Sequence or Clip.

        @return: hiero.core.TimeBase object
        """
        ...

    def getAnnotationsTrack(self,) -> Iterable:
        """
        self.getAnnotationsTrack() -> Returns the annotations track for the Clip or Sequence. If one does not already exist, it will be created.
        """
        ...

    def inOutEnabled(self,) -> bool:
        """
        self.inOutEnabled() -> Checks if the 'in' and 'out' points are enabled in the Sequence or Clip.

        @return: bool
        """
        ...

    def inTime(self,) -> int:
        """
        self.inTime() -> returns the 'in' point set on the clip.

        @return: frame
        """
        ...

    def isNull(self,) -> Union[True, False]:
        """
        self.isNull() -> returns False if this is a valid Sequence or Clip object, True otherwise.

        @return: True or False
        """
        ...

    def metadata(self,) -> DataCollection:
        """
        self.metadata() -> returns a collection of metadata for the object.

        @return: hiero.core.DataCollection object
        """
        ...

    def name(self,) -> str:
        """
        self.name() -> returns the name of the object.

        @return: string
        """
        ...

    def outTime(self,) -> int:
        """
        self.outTime() -> returns the 'out' point set on the clip.

        @return: frame
        """
        ...

    def playheadCount(self, index) -> Iterable:
        """
        playheadCount(index) -> Returns the number of playheads in the sequence.
        """
        ...

    def playheadInTime(self, index: int) -> Iterable:
        """
        playheadInTime(index) -> Returns the in marker time position of the playhead in the sequence.
        @param index: The index of the playhead.
        """
        ...

    def playheadOutTime(self, index: int) -> Iterable:
        """
        playheadOutTime(index) -> Returns the out marker time position of the playhead in the sequence.
        @param index: The index of the playhead.
        """
        ...

    def playheadState(self, index: int) -> int:
        """
        playheadState(index) -> The state of the given playhead index.
        The available states are:  ePlayheadActive : is the active playhead
          ePlayheadEnabled : is not the active playhead but is editable
          ePlayheadDisabled : has been removed.
          ePlayheadInvalid : index does not reference a valid playhead.@param index: The index of the playhead to be queried.
        """
        ...

    def playheadTime(self, index: int) -> Iterable:
        """
        playheadTime(index) -> Returns the time position of the playhead in the sequence.
        @param index: The index of the playhead.
        """
        ...

    def posterFrame(self,) -> int:
        """
        self.posterFrame() -> get the frame in the sequence used for thumbnails
        """
        ...

    def project(self) -> hiero.core.Project:
        """
        self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        ...

    def rawView(self,) -> str:
        """
        self.rawView() -> returns a string representing the raw view of this sequence or clip.

        @return: string
        """
        ...

    def razorAt(self, time: list) -> int | float:
        """
        self.razorAt(time) -> Creates razor cuts on all of the unlocked tracks for the parameter time(s).

        @param time: if a single (integer) value, indicates the razor cut time; if a tuple or list of integer values, then the times to create multiple cuts at
        """
        ...

    def refreshInOutEnabled(self,) -> None:
        """
        self.refreshInOutEnabled() -> Automatically set the sequence in/out enabled based on the current in/out values.

        @return: None
        """
        ...

    def removeTag(self, tag: Tag) -> Any:
        """
        self.removeTag(tag) -> removes the tag from the track.

        @param tag: hiero.core.Tag object
        """
        ...

    def setActivePlayhead(self, index: int) -> int:
        """
        setActivePlayhead(index) -> The given playhead index is made active.
        There can only be one active playhead, the previous playhead will be made inactive.
        @param index: The index of the playhead to be made active.
        """
        ...

    def setAutoDiskCacheMode(self, autoDiskCacheMode: Iterable) -> Iterable:
        """
        self.setAutoDiskCacheMode(autoDiskCacheMode) -> set the auto disk cache mode of the Sequence or Clip.

        @param autoDiskCacheMode: the selected hiero.core.SequenceAutoDiskCacheMode
        """
        ...

    def setDropFrame(self, drop) -> int:
        """
        self.setDropFrame(drop) -> set whether sequence timecode is displayed in drop frame format
        """
        ...

    def setFormat(self, format: Iterable) -> Iterable:
        """
        self.setFormat(format) -> set the format of the Sequence or Clip.

        @param format: a hiero.core.Format object to set for the Clip or Sequence.

        Example: myClipSequence.setFormat( hiero.core.Format(2048, 400, 2.37, 'MyFormat') )
        """
        ...

    def setFramerate(self, framerate) -> Iterable:
        """
        self.setFramerate(framerate) -> set the framerate of the Sequence or Clip.

        @param framerate: framerate value to set
        """
        ...

    def setInOutEnabled(self, enable) -> None:
        """
        self.setInOutEnabled(enable) -> Enable/Disable the 'in' and 'out' points.

        @return: None
        """
        ...

    def setInTime(self, t) -> None:
        """
        self.setInTime(t) -> set the 'in' point for the clip to Time t.
        This will also enable the In/Out lock.

        @return: None
        """
        ...

    def setName(self, ) -> str:
        """
        self.setName() -> set the name of the object.

        @param: string new name
        """
        ...

    def setOutTime(self, t) -> None:
        """
        self.setOutTime(t) -> set the 'out' point for the clip to Time t.
        This will also enable the In/Out lock.

        @return: None
        """
        ...

    def setPlayheadEnabled(self, index: int, enabled: bool) -> Any:
        """
        setPlayheadEnabled(index, enabled) -> Put the given playhead into the enabled state. The playheadis not active but is visible and editable in the UI. Otherwise the playhead will be disabled, which means thatit will not be visible in the UI.
        The current active playhead cannot be changed by this function.
        @param index: The index of the playhead to be changed.
        @param enabled: True if the playhead is enabled.
        """
        ...

    def setPlayheadInTime(self, index: int, time: int | float) -> int:
        """
        setPlayheadInTime(index, time) -> Set the in marker time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @param time: The new in time position to be set.
        """
        ...

    def setPlayheadOutTime(self, index: int, time: int | float) -> int:
        """
        setPlayheadOutTime(index, time) -> Set the out marker time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @param time: The new in time position to be set.
        """
        ...

    def setPlayheadTime(self, index: int, time: int | float) -> int:
        """
        setPlayheadTime(index, time) -> Set the time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @param time: The new time position to be set.
        """
        ...

    def setPosterFrame(self, frame) -> int:
        """
        self.setPosterFrame(frame) -> set the frame in the sequence used for thumbnails
        """
        ...

    def setSoftTrimsInTime(self, inTime: int) -> int | float:
        """
        self.setSoftTrimsInTime(inTime) -> sets the in time for the soft trims. Note: this method does not enable soft trims if they are disabled.

        @param inTime: in frame value for the soft trims
        """
        ...

    def setSoftTrimsOutTime(self, outTime: int) -> int | float:
        """
        self.setSoftTrimsOutTime(outTime) -> sets the out time for the soft trims. Note: this method does not enable soft trims if they are disabled.

        @param outTime: out frame value for the soft trims
        """
        ...

    def setTimecodeStart(self, time: int) -> int:
        """
        self.setTimecodeStart(time) -> sets the value of the start timecode by frame. To convert times to frame values, use TimeCode.HMSFToFrames or TimeCode.stringToTime.
        self.setTimecodeStart(timecodeValue, hasDropFrames) -> sets the value of the start timecode by formatted string, using the framerate of the Sequence or Clip as the time base. If just passing in a framerate, pass it in as an integer.

        @param time: frame value to set the time code to
        @param timecodeValue: string of the format "hh:mm:ss:ff"
        @param hasDropFrames: True if the timecode includes drop frames, False otherwise
        """
        ...

    def softTrimsEnabled(self,) -> Union[True, False]:
        """
        self.softTrimsEnabled() -> returns True if soft trims are enabled, False otherwise.

        @return: True or False
        """
        ...

    def softTrimsInTime(self,) -> int:
        """
        self.softTrimsInTime() -> returns the in time set for the soft trims.

        @return: frame
        """
        ...

    def softTrimsOutTime(self,) -> int:
        """
        self.softTrimsOutTime() -> returns the out time set for the soft trims.

        @return: frame
        """
        ...

    def tags(self) -> tuple[hiero.core.Tag, ...]:
        """
        self.tags() -> returns a tuple of all of the tags applied to this object.

        @return: tuple of hiero.core.Tag objects
        """
        ...

    def thumbnail(self, index: int = 0, layer: str = None) -> PySide2.QtGui.QImage:
        """
        self.thumbnail(frame, layer) -> returns a thumbnail of the frame specified as a QImage object.

        @param frame: the frame to get the thumbnail for (defaults to 0)
        @param layer: the layer to get the thumbnail for (defaults to colour)
        @return: QImage object
        """
        ...

    def timecodeStart(self,) -> int:
        """
        self.timecodeStart() -> returns the frame value of the start timecode. To convert this to a time code string, use TimeCode.timeToString.

        @return: frame
        """
        ...

    def timelineOffset(self,) -> int:
        """
        self.timelineOffset() -> returns the timeline offset value.

        @return: frame
        """
        ...

    def toString(self,) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def writeAudioToFile(self, ) -> str:
        """
        self.writeAudioToFile() -> Bounce down audio tracks and write to wav file at specified location. File will be created or overwritten.

        @param filepath: the filepath of file to be written
        @param inTime: in point of the timeline to write
        @param outTime: out point of the timeline to write
        @param numChannels: number of audio channels
        @param sampleRate: the sample rate to export to
        @param bitDepth: sample bit depth (PCM only)
        @param bitRate: audio bitrate in bits (compressed formats only)
        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    PlayheadState: Any = None
    ePlayheadActive: Any = None
    ePlayheadEnabled: Any = None
    ePlayheadDisabled: Any = None
    ePlayheadInvalid: Any = None
