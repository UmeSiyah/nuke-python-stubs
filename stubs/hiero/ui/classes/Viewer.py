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


class Viewer(QObject):
    """
    Object for manipulating viewers in Hiero. Get the currently active viewer by calling hiero.ui.currentViewer().
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
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

    def ROITool(self,) -> Any:
        """
        self.ROITool() -> return the ROI tool for this viewer
        """
        ...

    def annotationTool(self,) -> Any:
        """
        self.annotationTool() -> return the annotation tool for this viewer.
        """
        ...

    def availableGuideOverlayNames(self,) -> Any:
        """
        self.availableGuideOverlayNames() -> returns the names of all the guide overlays available in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The names of all the guide overlays available in the viewer
        """
        ...

    def cachedFrames(self,) -> Any:
        """
        self.cachedFrames() -> get the frames which are currently cached in the viewer.

        @return: set containing the indices of the cached frames
        """
        ...

    def channels(self,) -> Viewer:
        """
        self.channels() -> returns the current channels in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's current channels
        """
        ...

    def compareMode(self,) -> Viewer:
        """
        self.compareMode() -> returns the compare mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer.CompareMode object
        """
        ...

    def currentLayerName(self,) -> str:
        """
        self.currentLayerName() -> returns the name of the current channels layer the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's channels layer name
        """
        ...

    def cursorTool(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def displayDropFrames(self,) -> bool:
        """
        self.displayDropFrames() -> True if the drop frames are beingdisplayed on the time format (when timecode is displayed)

        @return: True if the display frames are being displayed
        """
        ...

    def displayTimecode(self,) -> bool:
        """
        self.displayTimecode() -> True if the timecode is being displayed on the time format

        @return: True if the timecode is being displayed
        """
        ...

    def enterFullScreen(self,) -> Any:
        """
        self.enterFullScreen() -> puts the viewer into full screen mode. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        ...

    def exitFullScreen(self,) -> Any:
        """
        self.exitFullScreen() -> takes the viewer out of full screen mode. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        ...

    def flushCache(self,) -> Any:
        """
        self.flushCache() -> flush the cache on the viewer and pause caching.
        """
        ...

    def frameIncrement(self,) -> int | float:
        """
        self.frameIncrement() -> returns the frame increment for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: the number of frames to skip or nudge
        """
        ...

    def gain(self,) -> Viewer:
        """
        self.gain() -> returns the gain value for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's gain value
        """
        ...

    def gamma(self,) -> Viewer:
        """
        self.gamma() -> returns the gamma value for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's gamma value
        """
        ...

    def getAchievedFPS(self,) -> float:
        """
        self.getAchievedFPS() -> returns the average fps achieved by the viewer.

        @return: floating point frames per second average
        """
        ...

    def goToNextEdit(self,) -> Any:
        """
        self.goToNextEdit() -> Move playhead to next edit. Can only be called from the user interface thread.
        """
        ...

    def goToNextTag(self,) -> Any:
        """
        self.goToNextTag() -> Move playhead to next tag. Can only be called from the user interface thread.
        """
        ...

    def goToPrevEdit(self,) -> Any:
        """
        self.goToPrevEdit() -> Move playhead to previous edit. Can only be called from the user interface thread.
        """
        ...

    def goToPrevTag(self,) -> Any:
        """
        self.goToPrevTag() -> Move playhead to previous tag. Can only be called from the user interface thread.
        """
        ...

    def image(self,) -> Any:
        """
        self.image() -> returns the contents of the viewer as an image, including all overlays. Can only be called from the user interface thread.

        @return: a PySide2.QtGui.QImage object
        """
        ...

    def isCachingPaused(self,) -> bool:
        """
        self.isCachingPaused() -> get whether caching is paused.

        @return: bool
        """
        ...

    def layoutMode(self,) -> Viewer:
        """
        self.layoutMode() -> returns the layout mode the viewer is currently in.

        @return: a Viewer.LayoutMode object
        """
        ...

    def maskOverlayName(self,) -> str:
        """
        self.maskOverlayName() -> returns the name of the current mask overlay in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The name of the mask overlay currently active in the viewer
        """
        ...

    def maskOverlayStyle(self,) -> Any:
        """
        self.maskOverlayStyle() -> returns the current mask overlay style set in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The current mask overlay style active in the viewer
        """
        ...

    def overlaysShown(self,) -> bool:
        """
        self.overlaysShown() -> get whether overlays are shown in the viewer.

        @return: bool
        """
        ...

    def pauseCaching(self,) -> Any:
        """
        self.pauseCaching() -> pause caching on the viewer.
        """
        ...

    def play(self,) -> Any:
        """
        self.play() -> starts playback in the viewer in the forward direction. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        ...

    def playBackwards(self,) -> Any:
        """
        self.playBackwards() -> starts playback in the viewer in the backwards direction. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        ...

    def playForwards(self,) -> Any:
        """
        self.playForwards() -> starts playback in the viewer in the forward direction. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        ...

    def playbackMode(self,) -> Viewer:
        """
        self.playbackMode() -> returns the compare mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer.PlaybackMode object
        """
        ...

    def playbackSpeed(self,) -> int:
        """
        self.playbackSpeed() -> Get the current playback speed, which will be 0 if playback is not currently in progress.
        """
        ...

    def player(self, index: int) -> Player:
        """
        self.player(index) -> returns the player object attached to this viewer, based on the input index.

        @param index: integer index of the player to retrieve
        @return: hiero.ui.Player object
        """
        ...

    def resumeCaching(self,) -> Any:
        """
        self.resumeCaching() -> resume caching on the viewer.
        """
        ...

    def saturation(self,) -> Viewer:
        """
        self.saturation() -> returns the saturation value for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's saturation value
        """
        ...

    def selectedGuideOverlayNames(self,) -> Any:
        """
        self.selectedGuideOverlayNames() -> returns the names of the current guide overlays in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The names of all the guide overlays currently active in the viewer
        """
        ...

    def setChannels(self, channels) -> Any:
        """
        self.setChannels(channels) -> Sets the channels in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param channels: the channels to be set in the viewer
        """
        ...

    def setCompareMode(self, mode) -> Any:
        """
        self.setCompareMode(mode) -> changes the compare mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param compareMode: a Viewer.CompareMode value
        """
        ...

    def setDisplayTimecode(self, displayTimecode) -> None:
        """
        self.setDisplayTimecode(displayTimecode) -> Sets the viewer to display Timecode if 'displayTimecode' is True, or Timeline Frame otherwise

        @return: None
        """
        ...

    def setExpandState(self, ) -> Any:
        """
        self.setExpandState() -> set the expanded state of the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param expanded: Expand viewer
        """
        ...

    def setFrameIncrement(self, frames: int | float) -> int:
        """
        self.setFrameIncrement(frames) -> changes the frame increment for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param frames: the number of frames to skip or nudge
        """
        ...

    def setGain(self, gain) -> Any:
        """
        self.setGain(gain) -> changes the gain for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param gain: a gain value to be set in the viewer
        """
        ...

    def setGamma(self, gamma) -> Any:
        """
        self.setGamma(gamma) -> changes the gamma for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param gamma: a gamma value to be set in the viewer
        """
        ...

    def setGuideOverlayFromRemote(self, ) -> Any:
        """
        self.setGuideOverlayFromRemote() -> Sets the guide overlays in the viewer from a remote source. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param overlayNames: the names of the overlays to be set
        @param remoteOverlaysAvailable: the names of the overlays that are available to the remote client
        """
        ...

    def setLayer(self, layerName: str) -> Any:
        """
        self.setLayer(layerName) -> Sets the channels layer in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param layerName: the name of the channels layer to be set in the viewer
        """
        ...

    def setLayoutMode(self, mode) -> Any:
        """
        self.setLayoutMode(mode) -> changes the layout mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param layoutMode: a Viewer.LayoutMode value indicating what layout to set the viewer to
        """
        ...

    def setMaskOverlayFromRemote(self, ) -> Any:
        """
        self.setMaskOverlayFromRemote() -> Sets the guide overlays in the viewer from a remote source. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param remoteOverlayName: the name of the overlay to be set
        """
        ...

    def setMaskOverlayStyle(self, ) -> Any:
        """
        self.setMaskOverlayStyle() -> Sets the channels in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param pyStyle: the mask style to be set in the viewer
        """
        ...

    def setOverlaysShown(self, show: bool) -> Any:
        """
        self.setOverlaysShown(show) -> set whether overlays are shown in the viewer.

        @param show: bool
        """
        ...

    def setCompareMode(self, mode: Viewer) -> Any:
        """
        self.setCompareMode(mode) -> changes the playback mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param mode: a Viewer.PlaybackMode value
        """
        ...

    def setPlaybackSpeed(self, speed) -> int:
        """
        self.setPlaybackSpeed(speed) -> Set the current playback speed. Setting to 0 will stop, -1 play in reverse, etc.
        """
        ...

    def setPlayer(self, index: int) -> int:
        """
        self.setPlayer(index) -> sets the active player if index is a valid player index.

        @param index: integer index of the player to set as the active player
        """
        ...

    def setSaturation(self, saturation) -> Any:
        """
        self.setSaturation(saturation) -> changes the saturation for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param saturation: a saturation value to be set in the viewer
        """
        ...

    def setSequence(self, ) -> Iterable:
        """
        self.setSequence() -> set the sequence for this viewer

        @param sequence: the sequence to set on this viewer
        @param indexOfPlayer: index to specify which of the players the sequence should be set on
        """
        ...

    def setTime(self, time: int) -> int | float:
        """
        self.setTime(time) -> seeks the play head of the viewer to the time parameter. Works the same as scrubbing the timeline in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param time: frame to set the play head to
        """
        ...

    def setTimeDisplayFormat(self, ) -> int | float:
        """
        self.setTimeDisplayFormat() -> Change the current time display format of the viewer

        @param displayTimecode: Display timecode
        @param displayDropFrames: Display drop frames
        """
        ...

    def setTracksMask(self, ) -> Any:
        """
        self.setTracksMask() -> modify the status of the tracks of one of the buffers. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param indexOfPlayer: integer index of the player
        @param tracksMask: TracksMask instance
        """
        ...

    def setView(self, name: str, viewIndex: Optional[int] = None) -> str:
        """
        setView(name, viewIndex) -> If name matches an existing view then the Viewers's active view for viewIndex is set to the view given by name.
        @param name: string
        @param viewIndex: optional; integer (for example in stereo a viewIndex of 0 corresponds to the primary view and 1 to the secondary view)
        """
        ...

    def stop(self,) -> Any:
        """
        self.stop() -> stops playback in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        ...

    def syncShuttleTargetFPS(self, ) -> int:
        """
        self.syncShuttleTargetFPS() -> Syncs the current target frame rate of the shuttle target frame rate

        @param fps: Target frame rate for the shuttle tool
        """
        ...

    def syncTargetFrameRate(self, ) -> int:
        """
        self.syncTargetFrameRate() -> Syncs the target frame rate of the viewer when it is modifiedby other client during a sync review

        @param numerator: Numerator of the target frame rate
        @param denominator: Denominator of the target frame rate
        """
        ...

    def time(self,) -> int:
        """
        self.time() -> returns the current frame of the viewer.
        """
        ...

    def toggleFullScreen(self,) -> Any:
        """
        self.toggleFullScreen() -> toggles full screen mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        ...

    def toggleFullScreen1_1(self,) -> int:
        """
        self.toggleFullScreen1_1() -> toggles 1:1 full screen mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        ...

    def tracksMask(self, ) -> TracksMask:
        """
        self.tracksMask() -> returns status of the tracks of one of the buffers. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param indexOfPlayer: integer index of the player
        @return: TracksMask instance
        """
        ...

    def view(self, viewIndex: Optional[int] = None) -> str:
        """
        view(viewIndex) -> Returns the name of the active view for viewIndex.
        @param viewIndex: optional; integer (for example in stereo a viewIndex of 0 corresponds to the primary view and 1 to the secondary view)
        """
        ...

    def window(self,) -> Any:
        """
        self.window() -> Return the viewer window
        """
        ...

    def wipeTool(self,) -> Any:
        """
        self.wipeTool() -> return the wipe tool for this viewer
        """
        ...

    LayoutMode: Any = None
    eLayoutWipe: Any = None
    eLayoutStack: Any = None
    eLayoutHorizontal: Any = None
    eLayoutVertical: Any = None
    eLayoutGrid: Any = None
    eLayoutFree: Any = None
    CompareMode: Any = None
    eCompareNoBlend: Any = None
    eCompareOver: Any = None
    eCompareUnder: Any = None
    eCompareOnionSkin: Any = None
    eCompareDifference: Any = None
    eCompareInvertAndAdd: Any = None
    eCompareMinus: Any = None
    PlaybackMode: Any = None
    ePlaybackRepeat: Any = None
    ePlaybackBounce: Any = None
    ePlaybackStop: Any = None
    ePlaybackContinue: Any = None
    timeChanged = Signal()
    compareModeChanged = Signal()
    timeDisplayFormatChanged = Signal()
    saturationChanged = Signal()
    channelsChanged = Signal()
    playbackSpeedChanged = Signal()
    shuttleTargetFPSChanged = Signal()
    frameDisplayed = Signal()
    maskOverlayChanged = Signal()
    layoutModeChanged = Signal()
    guideOverlayChanged = Signal()
    playbackModeChanged = Signal()
    targetFrameRateChanged = Signal()
    transformChanged = Signal()
    sequenceChanged = Signal()
    gammaChanged = Signal()
    gainChanged = Signal()
    playheadStateChanged = Signal()
    trackSelectionChanged = Signal()
    currentLayerChanged = Signal()
    maskOverlayStyleChanged = Signal()
    staticMetaObject: Any = None

    def _goToTag(self, tag: str) -> None:
        """
        Move playhead to Tag.
        If Tag (Tag Object or Tag name) does not exists on the Viewer's Sequence/Clip
        a KeyError is raised.

        @param tag: a Tag object or the name of the desired tag.
        """
        ...

    def _goToInTime(self) -> None:
        """
        Move playhead to In point
        """
        ...

    def _goToOutTime(self) -> None:
        """
        Move playhead to Out point
        """
        ...

    def _goToTrackItemStart(self, trackItem: Iterable) -> None:
        """
        Move playhead to start of the trackItem.

        @param trackItem: sequence's track item.
        """
        ...

    def _goToTrackItemEnd(self, trackItem: Iterable) -> None:
        """
        Move playhead to end of the trackItem.

        @param trackItem: sequence's track item.
        """
        ...

    def _goToTrackItemMiddle(self, trackItem: Iterable) -> None:
        """
        Move playhead to middle of the trackItem.

        @param trackItem: sequence's track item.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
