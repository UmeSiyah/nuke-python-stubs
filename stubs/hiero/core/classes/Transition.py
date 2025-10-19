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


class Transition(TrackItemBase):
    """
    Object representing a transition between two clips.
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

    def __bool__(self) -> bool:
        """
        True if self else False
        """
        ...

    def alignment(self,) -> Transition:
        """
        self.alignment() -> returns the alignment mode of this transition. Either kFadeIn, kDissolve, kFadeOut or kUnknown.

        @return: alignment type (hiero.core.Transition.Alignments)
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

    def dissolveNode(self,) -> Node:
        """
        self.dissolveNode() -> Returns the Dissolve node which controls the transition curve.

        @return: nuke.Node
        """
        ...

    def guid(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def inTrackItem(self,) -> Any:
        """
        self.inTrackItem() -> Get the in track item for this transition.

        return: hiero.core.TrackItem
        """
        ...

    def outTrackItem(self,) -> Any:
        """
        self.outTrackItem() -> Get the out track item for this transition.

        return: hiero.core.TrackItem
        """
        ...

    def parent(self,) -> AudioTrack:
        """
        self.parent() -> returns the AudioTrack or VideoTrack that contains this transition.

        @return: hiero.core.AudioTrack or hiero.core.VideoTrack object
        """
        ...

    def project(self,) -> Project:
        """
        self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        ...

    def setAlignment(self, alignment: Transition) -> Any:
        """
        self.setAlignment(alignment) -> sets the alignment mode on this transition.

        @param alignment: alignment type (hiero.core.Transition.Alignments), either kFadeIn, kDissolve, or kFadeOut
        """
        ...

    def setTimelineIn(self, inTime: int) -> Any:
        """
        self.setTimelineIn(inTime) -> sets the in point for this transition. Note that this trims the duration of the transition.

        @param inTime: frame for the new in point
        """
        ...

    def setTimelineOut(self, outTime: int) -> Any:
        """
        self.setTimelineOut(outTime) -> sets the out point for this transition. Note that this trims the duration of the transition.

        @param outTime: frame for the new out point
        """
        ...

    def toString(self,) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    Alignments: Any = None
    kFadeIn: Any = None
    kDissolve: Any = None
    kFadeOut: Any = None
    kUnknown: Any = None
