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


class AudioTrack(TrackBase):
    """
    Object for manipulating audio tracks.
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

    def __len__(self, ) -> None:
        """
        Return len(self).
        """
        ...

    def __getitem__(self, key, ) -> None:
        """
        Return self[key].
        """
        ...

    def addTrackItem(self, clip: TrackItem, audioChannel: int, position: int) -> TrackItem:
        """
        self.addTrackItem(clip, audioChannel, position) -> if the first parameter is a Clip object, the second and third parameters must be specified and this method creates a new track item with the specified audio channel and adds it to this audio track at the given position.
        If the first parameter is a TrackItem, then this method just adds the track item specified.
        This method will cut or delete track items that overlap with the one being added.
        This method can only be called if the track has already been added to a Sequence.

        @param clip: a hiero.core.Clip object or a hiero.core.TrackItem object, to add to this audio track.
        @param audioChannel: int; audio channel that will be associated with the track item. Do not specify if clip is a TrackItem.
        @param position: int; insert position. Do not specify if clip is a TrackItem.
        @return: hiero.core.TrackItem object
        """
        ...

    def channel(self,) -> str:
        """
        self.channel() -> returns the channel of the audio track.

        @return: String
        """
        ...

    def clone(self, *args, **kwargs) -> AudioTrack:
        """
        self.clone() -> returns a deep copy of this object.

        @return: hiero.core.AudioTrack object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
        ...

    def copy(self,) -> AudioTrack:
        """
        self.copy() -> returns a deep copy of this object.

        @return: hiero.core.AudioTrack object
        """
        ...

    def createTrackItem(self, name: str) -> TrackItem:
        """
        self.createTrackItem(name) -> creates a new track item.

        @param name: the name of the new track item
        @return: hiero.core.TrackItem object
        """
        ...

    def items(self,) -> tuple:
        """
        self.items() -> returns a tuple with all of the track items contained by this track.

        @return: tuple of hiero.core.TrackItem objects
        """
        ...

    def parent(self,) -> Iterable:
        """
        self.parent() -> returns the sequence that contains this track.

        @return: hiero.core.Sequence object
        """
        ...

    def setChannel(self, ) -> Any:
        """
        self.setChannel() -> Sets the channel of an audio track.

        @param: channel to set
        """
        ...

    def setVolume(self, ) -> int:
        """
        self.setVolume() -> Sets the volume of an audio track (0 - 1).

        @param: volume to set
        """
        ...

    def toString(self,) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def trackIndex(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def volume(self,) -> Any:
        """
        self.volume() -> returns the volume of the audio track.

        @return: double
        """
        ...

    def __copy__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    Channel: Any = None
    kUnknown: Any = None
    kMono: Any = None
    kFrontLeft: Any = None
    kFrontRight: Any = None
    kCentre: Any = None
    kSub: Any = None
    kSideLeft: Any = None
    kSideRight: Any = None
    kRearLeft: Any = None
    kRearRight: Any = None
