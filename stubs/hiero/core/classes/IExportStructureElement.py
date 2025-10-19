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


class IExportStructureElement:
    """
    Base class to be derived from and used in conjunction with a custom implementation of IExportStructure. For an example of how to derive from this class, see Plugins/site-packages/hiero/core/FnExportStructure.py.
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

    def addChild(self, newChild: IExportStructureElement) -> Any:
        """
        self.addChild(newChild) -> should append the new child item to this node's children, and set the parent on the child to this node.

        @param newChild: hiero.core.IExportStructureElement object
        """
        ...

    def child(self, index: int) -> IExportStructureElement:
        """
        self.child(index) -> should return the child of this node, based on the index.

        @param index: int index of the child to return
        @return: hiero.core.IExportStructureElement object
        """
        ...

    def childCount(self,) -> int:
        """
        self.childCount() -> should return the number of child nodes on this item.

        @return: int
        """
        ...

    def childIndex(self, exportElementChild: IExportStructureElement) -> int:
        """
        self.childIndex(exportElementChild) -> if the parameter is a child of this node, then this method should return the index of that child amongst the node's other children.

        @param exportElementChild: hiero.core.IExportStructureElement object
        @return: int
        """
        ...

    def clearChildren(self,) -> Any:
        """
        self.clearChildren() -> clears all of the children nodes from this node.
        """
        ...

    def createChildFolder(self, path: str) -> IExportStructureElement:
        """
        self.createChildFolder(path) -> create a child folder, including any needed intermediate folders, for the given path. If the named folder already exists, returns it.

        @param path: the path to the new folder
        @return: hiero.core.IExportStructureElement object
        """
        ...

    def createChildTask(self, path: str) -> IExportStructureElement:
        """
        self.createChildTask(path) -> create a child task, including any needed intermediate folders, for the given path.

        @param path: the path to the new element
        @return: hiero.core.IExportStructureElement object
        """
        ...

    def fromXml(self, xmlText: str) -> str:
        """
        self.fromXml(xmlText) -> should reinitialize the node from the xml text, and recreate the preset and all child nodes as well. If initialized using taskRegistry._savePresetElement, taskRegistry._loadPresetElement can be used to get data back out.

        @param xmlText: xml formatted text, as a result of a call in the past to the toXml method
        """
        ...

    def isLeaf(self,) -> Union[True, False]:
        """
        self.isLeaf() -> should return True if this is a node with no children, otherwise it should return False.

        @return: True or False
        """
        ...

    def name(self,) -> str:
        """
        self.name() -> should return the name of this element.

        @return: string
        """
        ...

    def parent(self,) -> IExportStructureElement:
        """
        self.parent() -> should return the parent node of this object.

        @return: hiero.core.IExportStructureElement object
        """
        ...

    def path(self,) -> str:
        """
        self.path() -> should return the full path to this node, including the path of any parents of this node.

        @return: string
        """
        ...

    def preset(self,) -> TaskPreset:
        """
        self.preset() -> should return an object derived from TaskPreset, representing the task associated with this element of the export structure.

        @return: hiero.core.TaskPreset derived object
        """
        ...

    def removeChild(self, child: IExportStructureElement) -> list:
        """
        self.removeChild(child) -> should remove the child from the node's list of children

        @param child: hiero.core.IExportStructureElement child object to remove
        """
        ...

    def setName(self, name: str) -> str:
        """
        self.setName(name) -> called to tell the node it's name.

        @param name: string
        """
        ...

    def setPreset(self, preset: TaskPreset) -> Any:
        """
        self.setPreset(preset) -> tells the object that the user has selected a new preset for this particular export element.

        @param preset: a hiero.core.TaskPreset derived object, which can be used to create a task to process later on during an export.
        """
        ...

    def setPresetType(self, presetType: str) -> str:
        """
        self.setPresetType(presetType) -> called to tell the object to set the task preset type by name. The taskRegistry can be used with this 'type' to create the preset to store.

        @param presetType: the name of the task preset to create/use.
        """
        ...

    def toXml(self,) -> str:
        """
        self.toXml() -> should return a string of formatted xml which can be sent to the fromXml method later to read it back. The xml should include the preset data for this node, as well as the children, and should be in proper xml format. This can be done easily with xml.etree.ElementTree, especially because the taskRegistry has methods to write out xml for presets and other objects (taskRegistry._savePresetElement)

        @return: string
        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...
