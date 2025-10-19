"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Gsv_Knob(Knob):
    """
    A knob which supports the interaction with Graph Scope Variables
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

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def getValue(self,) -> dict:
        """
        getValue() -> dict

        Return the Gsv sets as a dictionary.
        @return dict.
        Example:
        r = nuke.root()
        k = r['gsv']
        k.getValue()
        """
        ...

    def getValue(self,) -> dict:
        """
        getValue() -> dict

        Return the Gsv sets as a dictionary.
        @return dict.
        Example:
        r = nuke.root()
        k = r['gsv']
        k.getValue()
        """
        ...

    def setValue(self, dict: dict) -> None:
        """
        self.setValue(dict) -> None.
        Set the gsv sets as a dictionary for the current node.
        @param dict: Dictionary of Gsv entries.
        @return: None.
        Example:
        r = nuke.root()
        k = r['gsv']
        k.setValue({'Default': {'dk1': 'dv1', 'dk2': 'dv2'}, 'Custom': {'ck1': 'cv1', 'ck2': 'cv2'}})
        """
        ...

    def getGsvValue(self, path) -> str:
        """
        getGsvValue(path) -> string

        Return value of the Graph Scope Variable.
        @return String.
        Example:
        value = nuke.root()['gsv'].getGsvValue('Default.var')
        """
        ...

    def setGsvValue(self, path: str, value: str) -> None:
        """
        setGsvValue(path, value) -> None.
        Set the current value for the given path.
        @param path: String.
        @param value: String.
        @return: None.
        Example:
        nuke.root()['gsv'].setGsvValue('Default.var', 'value')
        """
        ...

    def removeGsv(self, path: str) -> bool:
        """
        removeGsv(path) -> Bool.
        Removes a GSV with the given path from it's GsvSet.
        @param path: String.
        @return: Bool.
        Example:
        nuke.root()['gsv'].removeGsv('Default.var')
        """
        ...

    def addGsvSet(self, path: str) -> bool:
        """
        addGsvSet(path) -> bool.
        Adds a GsvSet with the given path relative to the Node.
        @param path: String.
        @return: bool.
        Example:
        nuke.root()['gsv'].addGsvSet('Character')
        """
        ...

    def removeGsvSet(self, path: str) -> bool:
        """
        removeGsvSet(path) -> Bool.
        Removes a GsvSet with the given path from it's Group node entry.
        @param path: String.
        @return: Bool.
        Example:
        nuke.root()['gsv'].removeGsvSet('Custom')
        """
        ...

    def renameGsv(self, path: str, name: str) -> bool:
        """
        renameGsv(path, name) -> Bool.
        Renames a GSV with the given path.
        @param path: String.
        @param name: String.
        @return: Bool.
        Example:
        nuke.root()['gsv'].renameGsv('Default.var', 'variable')
        """
        ...

    def renameGsvSet(self, path: str, name: str) -> bool:
        """
        renameGsvSet(path, name) -> Bool.
        Renames a GsvSet with the given path.
        @param path: String.
        @param name: String.
        @return: Bool.
        Example:
        nuke.root()['gsv'].renameGsvSet('Custom', 'Other')
        """
        ...

    def contains(self, path: str) -> bool:
        """
        contains(path) -> Bool.
        Returns True if the path exist relative to the GsvKnob.
        This function does not make distinction between the element types for
        the given path i.e. the path must include the GsvSet name when checking
        for a variable in the Default variable set.
        @param path: String.
        @return: Bool.
        Example:
        nuke.root()['gsv'].contains('Group1.Custom.variable')
        """
        ...
