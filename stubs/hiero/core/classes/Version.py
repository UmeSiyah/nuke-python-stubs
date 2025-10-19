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


class Version:
    """
    Object representing a version of a clip or sequence. Can be created with a Clip or Sequence object.
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

    def guid(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def isHidden(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def isNull(self,) -> Union[True, False]:
        """
        self.isNull() -> returns True if the object is invalid, False otherwise.

        @return: True or False
        """
        ...

    def item(self,) -> Iterable:
        """
        self.item() -> returns the clip or sequence stored with this version.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
        ...

    def name(self,) -> str:
        """
        self.name() -> returns the name of this version.

        @return: string
        """
        ...

    def parent(self,) -> BinItem:
        """
        self.parent() -> returns the bin item that contains this version.

        @return: hiero.core.BinItem object
        """
        ...

    def serialize(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def setHidden(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def toString(self,) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def versionIndex(self, *args, **kwargs) -> str:
        """
        self.versionIndex() -> returns a string containing the version's index.

        @return: string

        WARNING - DEPRECATED ( versionIndex ): This method is deprecated and will not be present in future versions of the Python API.
        Version indices are no longer unique identifiers and should not be used as such.
        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...
