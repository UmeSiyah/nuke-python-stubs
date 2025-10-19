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


class ExportStructureViewer(QWidget):
    """
    QWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
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

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def addFile(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def addFolder(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def allowNodeDelete(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def clearResolveEntries(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def copy(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def cut(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def exportRootChanged(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def filenameField(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def getWidget(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def handleSelectionChanged(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def initUI(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def itemTypes(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None:
        """
        keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None
        """
        ...

    def paste(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def refresh(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def refreshContentField(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def removeNode(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def selectFileIfOnlyOne(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def selectFirstFile(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def selection(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def selectionAnchor(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def selectionRect(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def setAllowNodeDelete(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def setExportStructure(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def setItemTypes(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def setProject(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def setResolveEntry(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    EditMode: Any = None
    Full: Any = None
    Limited: Any = None
    ReadOnly: Any = None
    structureModified = Signal()
    selectionChanged = Signal()
    kAddFolderToolTip = 'Adds a new directory to your export structure'
    kAddFileToolTip = 'Adds new file entry to the export structure'
    kRemoveToolTip = 'Deletes the selected file entry from the export structure'
    kStructurePathToolTip = 'This structure defines the path into which the exported content will be written. See the tokens listed within the tooltip to build unique paths for each item exported.'
    kStructureContentToolTip = 'The content written into the structure is defined by the export task selected here.'
    staticMetaObject: Any = None
