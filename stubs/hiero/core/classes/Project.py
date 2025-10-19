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


class Project:
    """
    Object for manipulating projects. Can be created using hiero.core.newProject() or by the following code:
    hiero.core.openProject(projectPath)
    project = hiero.core.projects()[-1]
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __repr__(self, ) -> None:
        """
        Return repr(self).
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

    def addView(self, name: str, color: Optional[list] = None) -> Union[True, False]:
        """
        addView(name, color) -> Appends a view to this project's list of views. Returns False if name is empty or a view already exists with the same name.

        @param name: string
        @param color: optional; string in the format #RGB, #RRGGBB, #RRRGGGBBB, #RRRRGGGGBBBB or a name from the list of colors defined in the list of SVG color keyword names
        @return: True or False
        """
        ...

    def autosave(self,) -> str:
        """
        self.autosave() -> if the project has been modified create an autosave file
        """
        ...

    def beginUndo(self, name) -> UndoGroup:
        """
        self.beginUndo(name) -> starts a new undo action, which will group all other undo actions until self.endUndo() is called. Be aware that this method only works on the main thread, and will throw an exception otherwise.
        Note that for operations inside the undo to work Project.endUndo() must be called.  It is recommended that you use this in a with block to ensure that this happens.  For example:
          with project.beginUndo('My Undo'):
            // Undoable edits

        @return: UndoGroup object
        """
        ...

    def buildTrackName(self,) -> str:
        """
        buildTrackName() -> get default track name used when building vfx trackthis can be configured in the project settings dialog
        """
        ...

    def cancelUndo(self,) -> Any:
        """
        self.cancelUndo() -> cancels an undo action started previously by a call to self.beginUndo().
        """
        ...

    def clearUnusedLocalFiles(self,) -> str:
        """
        clearUnusedLocalFiles() -> clear all localised files that are not in any currently open project. This requires localisation to be enabled
        """
        ...

    def clipsBin(self,) -> Bin:
        """
        self.clipsBin() -> returns the bin object containing the top level clips, sequences and bins for this project.

        @return: hiero.core.Bin object
        """
        ...

    def close(self,) -> Any:
        """
        self.close() -> closes the project. Be aware that this method will not save the project, even if changes have been made since the last save of the project.
        """
        ...

    def createExportWriteNode(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def customExportDirectory(self,) -> str:
        """
        self.customExportDirectory() -> Get the custom directory used for exports if useCustomExportDirectory() is set to True.

        @return: string
        """
        ...

    def deletable(self,) -> Union[True, False]:
        """
        self.deletable() -> returns True if the project can be deleted.

        @return: True or False
        """
        ...

    def deleteView(self, name: str) -> Union[True, False]:
        """
        deleteView(name) -> Removes the view with the matching name from this project's list of views. Returns False if no matching view is found or if the view to be deleted is the only view in the project.
        @param name: string
        @return: True or False
        """
        ...

    def editable(self,) -> Union[True, False]:
        """
        self.editable() -> returns True if the project can be edited.

        @return: True or False
        """
        ...

    def endUndo(self,) -> Undo:
        """
        self.endUndo() -> ends an undo action started previously by a call to self.beginUndo(). This will put a new item into the Edit > Undo/Redo menu items.
        """
        ...

    def exportRootDirectory(self,) -> str:
        """
        self.exportRootDirectory() -> The root directory to use for exports. This will return either self.projectDirectory(True) or self.customExportDirectory() depending on the self.useCustomExportDirectory() setting.

        @return: string
        """
        ...

    def framerate(self,) -> int | float:
        """
        framerate() -> project's default framerate for new sequences

        @return: TimeBase
        """
        ...

    def guid(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def heroView(self,) -> str:
        """
        heroView() -> Get the name of the hero view set on the project
        @return: str
        """
        ...

    def isLocalisationEnabled(self,) -> Any:
        """
        isLocalisationEnabled() -> return whether localisation is enabled

        @return: whether localisation is enabled
        """
        ...

    def isNull(self,) -> Union[True, False]:
        """
        self.isNull() -> returns False if this is a valid Project object, True otherwise.

        @return: True or False
        """
        ...

    def isRestricted(self,) -> Union[True, False]:
        """
        self.isRestricted() -> returns whether or not access to the project is restricted.

        @return: True or False
        """
        ...

    def lutSetting16Bit(self,) -> str:
        """
        self.lutSetting16Bit() -> returns the project's 16 bit lut setting name.

        @return: string
        """
        ...

    def lutSetting8Bit(self,) -> str:
        """
        self.lutSetting8Bit() -> returns the project's 8 bit lut setting name.

        @return: string
        """
        ...

    def lutSettingFloat(self,) -> str:
        """
        self.lutSettingFloat() -> returns the project's float lut setting name.

        @return: string
        """
        ...

    def lutSettingLog(self,) -> str:
        """
        self.lutSettingLog() -> returns the project's log lut setting name.

        @return: string
        """
        ...

    def lutSettingMonitorOut(self,) -> str:
        """
        self.lutSettingMonitorOut() -> returns the project's Monitor Out lut setting name.

        @return: string
        """
        ...

    def lutSettingThumbnail(self,) -> str:
        """
        self.lutSettingThumbnail() -> returns the project's Thumbnail lut setting name.

        @return: string
        """
        ...

    def lutSettingsViewer(self,) -> str:
        """
        self.lutSettingsViewer() -> returns the project's viewer lut setting name.

        @return: string
        """
        ...

    def lutSettingWorkingSpace(self,) -> str:
        """
        self.lutSettingWorkingSpace() -> returns the project's Working Space lut setting name.

        @return: string
        """
        ...

    def lutUseOCIOForExport(self,) -> bool:
        """
        self.lutUseOCIOForExport() -> returns the project setting for using OCIO in nuke script export.

        @return: bool
        """
        ...

    def modifiedSinceLastSave(self,) -> Any:
        """
        self.modifiedSinceLastSave() -> Check if the project has been modified since it was last saved
        """
        ...

    def name(self,) -> str:
        """
        self.name() -> returns the name of the project.

        @return: string
        """
        ...

    def ocioConfigName(self,) -> str:
        """
        self.ocioConfigName() -> returns the ocio config name loaded by NukeStudio. When using a custom ocio config an empty string is returned.

        @return: string
        """
        ...

    def ocioConfigPath(self,) -> str:
        """
        self.ocioConfigPath() -> returns the project settings for the ocio config path.

        @return: string
        """
        ...

    def outputFormat(self,) -> Format:
        """
        outputFormat() -> gets project's default outputFormat for new sequences.

        @return: Format
        """
        ...

    def path(self,) -> str:
        """
        self.path() -> returns the path to the project.

        @return: string
        """
        ...

    def posterFrameSettings(self,) -> tuple:
        """
        posterFrameSettings() -> Get the poster frame settings used for clips added to the project.
        @return: tuple of poster frame setting and custom frame number
        """
        ...

    def projectDirectory(self, ) -> str:
        """
        self.projectDirectory() -> Get the project directory used for resolving relative paths and the exportRootDirectory() (if useCustomExportDirectory() is False).

        @param expanded: whether expressions in the path are expanded
        @return: string
        """
        ...

    def redo(self,) -> Any:
        """
        self.redo() -> triggers a redo of the next item in the redo stack. Only works on the main thread. If called from any other thread, throws an exception.
        """
        ...

    def redoItemText(self,) -> str:
        """
        self.redoItemText() -> returns the text of the next item on the redo stack. Only works on the main thread. Can be useful for testing that undo/redo works.

        @return: string
        """
        ...

    def save(self,) -> Any:
        """
        self.save() -> saves a previously saved project to disk.
        """
        ...

    def saveAs(self, filename: str) -> str:
        """
        self.saveAs(filename) -> saves the project to the path specified by the filename parameter. Throws an exception if the project couldn't be saved for any reason.

        @param filename: path to save the project to
        """
        ...

    def setCustomExportDirectory(self, ) -> bool:
        """
        self.setCustomExportDirectory() -> Set the custom directory used for exports if useCustomExportDirectory() is set to True.

        @param path: path
        """
        ...

    def setDeletable(self, deletable: Union[True, False]) -> Any:
        """
        self.setDeletable(deletable) -> sets whether or not a project can be deleted.

        @param deletable: True or False
        """
        ...

    def setEditable(self, editable: Union[True, False]) -> Any:
        """
        self.setEditable(editable) -> sets whether or not a project can be edited.

        @param editable: True or False
        """
        ...

    def setFramerate(self, TimeBase) -> Iterable:
        """
        setFramerate(TimeBase) -> sets project's default framerate for new sequences.This will persist when the application is restarted

        @param: TimeBase
        """
        ...

    def setHasMigratedSequenceProperties(self,) -> Iterable:
        """
        setHasMigratedSequenceProperties() -> Mark the project as having had deprecated sequence properties converted into soft effects.
        """
        ...

    def setLocalisationEnabled(self, ) -> Any:
        """
        setLocalisationEnabled() -> set whether localisation is enabled. This will persist when the application is restarted.

        @param isEnabled: whether localisation should be enabled
        """
        ...

    def setModified(self,) -> Any:
        """
        self.setModified() -> Set the project as modified even if just saved or loaded
        """
        ...

    def setOcioConfigPath(self, path) -> Any:
        """
        self.setOcioConfigPath(path) -> set the ocio config for the project
        """
        ...

    def setOutputFormat(self, format: hiero.core.Format) -> None:
        """
        setOutputFormat(Format) -> sets project's default output format for new sequences.
        setOutputFormat(width, height, pixelAspect, name) -> sets project's default output format for new sequences. This will persist when the application is restarted

        @param width: width for the output format
        @param height: height for the output format
        @param pixelAspect: float for pixel aspect ratio
        @param name: string for the format name
        """
        ...

    def setPath(self, path) -> str:
        """
        self.setPath(path) -> set the path a project saves to without saving it
        """
        ...

    def setPosterFrameSettings(self, ) -> int:
        """
        setPosterFrameSettings() -> Set the poster frame settings used for clips added to the project.
        @param setting: the mode for setting poster frames
        @param customFrame: the frame number if mode is set to ePosterFrameCustom
        """
        ...

    def setProjectDirectory(self, string) -> bool:
        """
        self.setProjectDirectory(string) -> Set the project directory used for resolving relative paths and the exportRootDirectory() (if useCustomExportDirectory() is False).

        @param path: the path or expression to set
        """
        ...

    def setShotPresetName(self,) -> str:
        """
        self.setShotPresetName() -> set the name of Shot Preset which is usedwhen sending to nuke or creating a comp.

        @param name:
        """
        ...

    def setShowViewColors(self,) -> Any:
        """
        setShowViewColors() -> Set if colors set for views are shown in the UI.
        """
        ...

    def setStartTimecode(self, Time) -> Iterable:
        """
        setStartTimecode(Time) -> sets project's default start timecode for new sequences. This will persist when the application is restarted

        @param startTime: TimeBase start timecode for sequence
        """
        ...

    def setTimeDisplayFormat(self, ) -> Iterable:
        """
        setTimeDisplayFormat() -> sets project's default displayType for new sequences.  This will persist when the application is restarted

        @param displayType: DisplayType to use
        """
        ...

    def setTrackItemReformatState(self,) -> ReformatState:
        """
        setTrackItemReformatState() -> Set the default ReformatState for new TrackItems created in this project
        """
        ...

    def setTrackItemVersionsLinkedToBin(self, linked) -> Any:
        """
        setTrackItemVersionsLinkedToBin(linked) -> Set whether track item versions are linked by default
        """
        ...

    def setUseCustomExportDirectory(self,) -> Any:
        """
        self.setUseCustomExportDirectory() -> Set if the export root directory should be a custom directory, or use the project directory.

        @param custom:
        """
        ...

    def setViews(self, views: list) -> Any:
        """
        setViews(views) -> Set the project's views.
        @param views: this can be either a list of view names, or a list of tuples with (name, color)
        """
        ...

    def setViewsForStereo(self,) -> Any:
        """
        setViewsForStereo() -> Replaces the project's views with two views named "left" and "right".
        """
        ...

    def shotPresetName(self,) -> str:
        """
        self.shotPresetName() -> get the name of Shot Preset which is usedwhen sending to nuke or creating a comp.

        @return: string
        """
        ...

    def showViewColors(self,) -> Any:
        """
        showViewColors() -> Get if colors set for views are shown in the UI.
        """
        ...

    def startTimecode(self,) -> int | float:
        """
        startTimecode() -> gets project's default start frame for new sequences.

        @return: Time
        """
        ...

    def tagsBin(self,) -> Bin:
        """
        self.tagsBin() -> returns the bin object containing the top level tags for this project.

        @return: hiero.core.Bin object
        """
        ...

    def timeDisplayFormat(self,) -> Iterable:
        """
        timeDisplayFormat() -> gets project's default displayType for new sequences. @return: DisplayType
        """
        ...

    def toString(self,) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def trackItemReformatState(self,) -> ReformatState:
        """
        trackItemReformatState() -> Get default ReformatState for new TrackItems created in this project
        """
        ...

    def trackItemVersionsLinkedToBin(self,) -> Any:
        """
        trackItemVersionsLinkedToBin() -> Get whether track item versions are linked by default
        """
        ...

    def undo(self,) -> Any:
        """
        self.undo() -> triggers an undo on the last item previously added to the undo stack. Only works on the main thread. If called from any other thread, throws an exception.
        """
        ...

    def undoItemText(self,) -> str:
        """
        self.undoItemText() -> returns the text of the last item on the undo stack. Only works on the main thread. Can be useful for testing that undo/redo works.

        @return: string
        """
        ...

    def useCustomExportDirectory(self,) -> bool:
        """
        self.useCustomExportDirectory() -> Get if the export root directory should be a custom directory, or use the project directory.

        @return: bool
        """
        ...

    def staticmethod(self, function) -> Any:
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, ...):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
        ...

    def views(self,) -> list:
        """
        views() -> Returns a list of this project's views.
        @return: list of strings
        """
        ...

    def viewsAndColors(self,) -> list:
        """
        viewsAndColors() -> Returns a list of this project's views and corresponding colors.
        @return: list of (str, PySide2.QtGui.QColor) tuples
        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    OpenFlags: Any = None
    kProjectOpenNoFlags: Any = None
    kProjectOpenStartup: Any = None
    kProjectOpenDontAddToRecent: Any = None
    SaveFlags: Any = None
    kProjectSaveNoFlags: Any = None
    kProjectSaveKeepName: Any = None
    kProjectSaveDontAddToRecent: Any = None
    kProjectSaveAsShowFileDialog: Any = None
    kProjectSaveDontChangeProjectPath: Any = None
    PosterFrameSetting: Any = None
    eFirst: Any = None
    eMiddle: Any = None
    eLast: Any = None
    eCustom: Any = None
    kAllProjects = 0
    kUserProjects = 1
    kStartupProjects = 2

    def extractSettings(self) -> dict[str, str]:
        """
        self.extractSettings() -> returns a dict of the project's settings.     @return: dict

        """
        ...

    def sequences(self, partialNam: Optional[str] = None) -> list[core.Sequence]:
        """
        self.sequences(partialName) -> returns all sequences in a project. User can filter by by partial name.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.
        @return: an array of hiero.core.Sequence objects.

        Example: finds all sequences in a project with 30Sec in the name:

        sequences = myProject.sequences('30Sec')
        """
        ...

    def bins(self, partialName: Optional[str] = None) -> list[core.Bin]:
        """
        self.bins(partialName) -> returns all bins in a project. Searches recursively, so will return bins within other bins in the list.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.Bin objects.

        Example: finds all bins in a project with MyBin in the name:

        bins = myProject.bins('MyBin')
        """
        ...

    def clips(self, partialName: Optional[str] = None) -> list[core.Clip]:
        """
        self.clips(partialName) -> returns all clips in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.Clip objects.

        Example: finds all clips in a project with 30Sec in the name:

        clips = myProject.clips('30Sec')
        """
        ...

    def tracks(self, partialName: Optional[str] = None) -> list[core.Track]:
        """
        self.tracks(partialName) -> returns all tracks in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.VideoTrack and hiero.core.AudioTrack objects.

        Example: finds all tracks in a project with 30Sec in the name:

        tracks = myProject.tracks('30Sec')
        """
        ...

    def videoTracks(self, partialName: Optional[str] = None) -> list[core.VideoTrack]:
        """
        self.videoTracks(partialName) -> returns all video tracks in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.VideoTrack objects.

        Example: finds all video tracks in a project with 30Sec in the name:

        tracks = myProject.videoTracks('30Sec')
        """
        ...

    def audioTracks(self, partialName: Optional[str] = None) -> list[core.AudioTrack]:
        """
        self.audioTracks(partialName) -> returns all audio tracks in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.AudioTrack objects.

        Example: finds all audio tracks in a project with 30Sec in the name:

        tracks = myProject.audioTracks('30Sec')
        """
        ...

    def trackItems(self, partialName: Optional[str] = None) -> list[core.TrackItem]:
        """
        self.trackItems(partialName) -> returns all track items in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.TrackItem objects.

        Example: finds all track items in a project with 30Sec in the name:

        trackItems = myProject.trackItems('30Sec')
        """
        ...

    def videoTrackItems(self, partialName: Optional[str] = None) -> list[core.TrackItem]:
        """
        self.videoTrackItems(partialName) -> returns all video track items in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.TrackItem objects.

        Example: finds all video track items in a project with 30Sec in the name:

        trackItems = myProject.videoTrackItems('30Sec')
        """
        ...

    def audioTrackItems(self, partialName: Optional[str] = None) -> list[core.TrackItem]:
        """
        self.audioTrackItems(partialName) -> returns all audio track items in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.TrackItem objects.

        Example: finds all audio track items in a project with 30Sec in the name:

        trackItems = myProject.audioTrackItems('30Sec')
        """
        ...
