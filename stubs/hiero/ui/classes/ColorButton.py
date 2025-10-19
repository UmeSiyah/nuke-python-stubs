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


class ColorButton(QPushButton):
    """
    QPushButton(self, icon: PySide2.QtGui.QIcon, text: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QPushButton(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QPushButton(self, text: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
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

    def canBeInvalid(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def color(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None:
        """
        dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None
        """
        ...

    def dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None:
        """
        dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None
        """
        ...

    def mouseMoveEvent(self, e: PySide2.QtGui.QMouseEvent) -> None:
        """
        mouseMoveEvent(self, e: PySide2.QtGui.QMouseEvent) -> None
        """
        ...

    def mousePressEvent(self, e: PySide2.QtGui.QMouseEvent) -> None:
        """
        mousePressEvent(self, e: PySide2.QtGui.QMouseEvent) -> None
        """
        ...

    def paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None:
        """
        paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None
        """
        ...

    def setCanBeInvalid(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def setColor(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def setValidColor(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def sizeHint(self) -> Any:
        """
        sizeHint(self) -> PySide2.QtCore.QSize
        """
        ...

    def validColor(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    colorChanged = Signal()
    staticMetaObject: Any = None
