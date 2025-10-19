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


class IExportStructure:
    """
    Base class to be derived from in order to populate an ExportStructureViewer widget, such as the one used in the Export dialog box. IExportStructure objects provides access to a root node, which has to be an object derived from IExportStructureElement, which the ExportStructureViewer widget then uses to determine the tree structure to display to the user. For an example of how to derive from this class, see Plugins/site-packages/hiero/core/FnExportStructure.py. For an example use of a derived IExportStructure object, see Plugins/site-packages/hiero/exporters/FnShotProcessor.py. It will often be more than sufficient to just use an ExportStructure2 object, instead of subclassing IExportStructure directly.
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

    def childElement(self, path: str) -> IExportStructureElement:
        """
        self.childElement(path) -> should return an object derived from IExportStructureElement, representing a child with the path specified.

        @param path: the path to the new (or existing) child element
        @return: IExportStructureElement derived object
        """
        ...

    def exportRootPath(self,) -> str:
        """
        self.exportRootPath() -> retrieves the root path for the export structure.

        @return: string
        """
        ...

    def rootElement(self,) -> IExportStructureElement:
        """
        self.rootElement() -> should return a IExportStructureElement super class object, representing the root of the export file structure.

        @return: IExportStructureElement derived object
        """
        ...

    def setExportRootPath(self, path: str) -> str:
        """
        self.setExportRootPath(path) -> called when the user has modified the export root path, to inform the object of the new path.

        @param path: the new user supplied path to export to.
        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...
