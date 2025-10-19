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


class BackgroundRenderObserver:
    """
    Observer of background renders.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
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

    def isNull(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def onFrameRenderCancelled(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def onFrameRenderError(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def onFrameRenderInProgress(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def onFrameRenderQueued(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def onFrameRendered(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def onRenderQueued(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...
