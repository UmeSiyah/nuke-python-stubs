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


class IExporterUIRegistry:
    """
    IExporterUIRegistry provides a simple interface for our C++ Application to access the Python instance of TaskUIRegistry.

    This class should not be used directly; use hiero.ui.TaskUIRegistry instead.
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

    def aquireProcessorUI(self, ) -> TaskPreset:
        """
        self.aquireProcessorUI() -> Called from Hiero Application to aquire a reference to an instance of the ProcessorUI object related to the specified hiero.core.TaskPreset.

        @param preset: hiero.core.ITaskPreset
        """
        ...

    def getProcessorUI(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def getProcessorUIForPreset(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def getTaskUI(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def getTaskUIForPreset(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def numProcessorUIs(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def numTaskUIs(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def registerme(self,) -> TaskUIRegistry:
        """
        self.registerme() -> Called from python implimentation of TaskUIRegistry to register instance as the Application TaskUI Registry.
        """
        ...

    def releaseProcessorUI(self, ) -> IProcessorUI:
        """
        self.releaseProcessorUI() -> Called from Hiero Application to release the reference to a IProcessorUI object previously aquired using IExporterUIRegistry.aquireProcessorUI.

        @param processorUI: hiero.ui.IProcessorUI
        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...
