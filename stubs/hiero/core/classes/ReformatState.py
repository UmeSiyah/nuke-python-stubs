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


class ReformatState:
    """
    Object representing a the reformatting settings for a track item.  This corresponds to the Nuke 'Reformat' node.
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

    def boxForceShape(self,) -> bool:
        """
        self.boxForceShape() -> returns the box 'force shape' flag.

        @return: bool
        """
        ...

    def boxPAR(self,) -> Any:
        """
        self.boxPAR() -> returns the box pixel aspect ratio.

        @return: double
        """
        ...

    def boxSize(self,) -> Any:
        """
        self.boxSize() -> returns the box size.

        @return: QSize
        """
        ...

    def copyFrom(self,) -> ReformatState:
        """
        self.copyFrom() -> Copy the properties from another ReformatState.

        @param: ReformatState
        """
        ...

    def isNull(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def originalResizeFlip(self,) -> bool:
        """
        self.originalResizeFlip() -> returns the original resize flip flag, which may be a deprecated value if it was loaded from an old project.

        @return: bool
        """
        ...

    def originalResizeFlop(self,) -> bool:
        """
        self.originalResizeFlop() -> returns the original resize flop flag, which may be a deprecated value if it was loaded from an old project.

        @return: bool
        """
        ...

    def originalResizeTurn(self,) -> bool:
        """
        self.originalResizeTurn() -> returns the original resize turn flag, which may be a deprecated value if it was loaded from an old project.

        @return: bool
        """
        ...

    def originalType(self,) -> str:
        """
        self.originalType() -> returns the original reformat type of the state, which may be a deprecated value if it was loaded from an old project.

        @return: string
        """
        ...

    def resizeCenter(self,) -> bool:
        """
        self.resizeCenter() -> returns the resize center flag.

        @return: bool
        """
        ...

    def resizeFlip(self,) -> bool:
        """
        self.resizeFlip() -> returns the resize flip flag. Note: the flip option has been removed, this method should not be called.

        @return: bool
        """
        ...

    def resizeFlop(self,) -> bool:
        """
        self.resizeFlop() -> returns the resize flop flag. Note: the flop option has been removed, this method should not be called.

        @return: bool
        """
        ...

    def resizeTurn(self,) -> bool:
        """
        self.resizeTurn() -> returns the resize turn flag. Note: the turn option has been removed, this method should not be called.

        @return: bool
        """
        ...

    def resizeType(self,) -> str:
        """
        self.resizeType() -> returns the resize type.

        @return: string
        """
        ...

    def scale(self,) -> int | float:
        """
        self.scale() -> returns the scaling factor. Note: the scale option has been removed, this method should not be called.

        @return: double
        """
        ...

    def setBoxForceShape(self, ) -> Any:
        """
        self.setBoxForceShape() -> sets the box 'force shape' flag if the reformat type is set to 'to box'.

        @param setBoxForceShape: bool
        """
        ...

    def setBoxPAR(self, ) -> Any:
        """
        self.setBoxPAR() -> sets the box pixel aspect ratio if the reformat type is set to 'to box'.

        @param PAR: double
        """
        ...

    def setBoxSize(self, ) -> Any:
        """
        self.setBoxSize() -> sets the box size if the reformat type is set to 'to box'.

        @param size: QSize
        """
        ...

    def setResizeCenter(self, ) -> Any:
        """
        self.setResizeCenter() -> sets the resize center flag on the track item.

        @param center: bool
        """
        ...

    def setResizeFlip(self,) -> Any:
        """
        self.setResizeFlip() -> the flip option has been removed, this method exists only for compatibility reasons
        """
        ...

    def setResizeFlop(self,) -> Any:
        """
        self.setResizeFlop() -> the flop option has been removed, this method exists only for compatibility reasons
        """
        ...

    def setResizeTurn(self,) -> Any:
        """
        self.setResizeTurn() -> the turn option has been removed, this method exists only for compatibility reasons
        """
        ...

    def setResizeType(self, ) -> Any:
        """
        self.setResizeType() -> sets the resize type of the state.

        @param newResizeType: string
        """
        ...

    def setScale(self,) -> int | float:
        """
        self.setScale() -> the scale option has been removed, this method exists only for compatibility reasons
        """
        ...

    def setType(self, ) -> Any:
        """
        self.setType() -> sets the reformat type of the state.

        @param newType: string
        """
        ...

    def toString(self,) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def type(self,) -> str:
        """
        self.type() -> returns the reformat type of the state.

        @return: string
        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...
