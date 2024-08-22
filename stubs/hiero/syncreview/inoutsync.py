from hiero.core import Clip, Sequence, events, findItemByGuid

from . import messages
from .synctool import SyncTool, localCallback, remoteCallback

messages.defineMessageType('InOutChange', ('sequenceGuid', str),
                           ('inTime', int), ('outTime', int), ('playheadIndex', int))
messages.defineMessageType('InOutLockEnabledChange',
                           ('sequenceGuid', str), ('enabled', messages.Bool))


class SyncInOutTool(SyncTool):
    """ Tool for syncing changes to the 'in' and 'out' points. """

    def __init__(self, messageDispatcher):
        super(SyncInOutTool, self).__init__(messageDispatcher)
        self.messageDispatcher._registerCallback(messages.InOutChange, self._onRemoteInOutChanged)
        self.messageDispatcher._registerCallback(
            messages.InOutLockEnabledChange, self._remoteInOutLockEnabledChanged)
        self.registerEventCallback(events.EventType.kInOutPointsChanged, self._onLocalInOutChanged)
        self.registerEventCallback(events.EventType.kInOutLockEnabledChanged,
                                   self._onLocalInOutLockEnabledChanged)

    @localCallback
    def _onLocalInOutChanged(self, event):
        msg = messages.InOutChange(sequenceGuid=event.sequence.guid(),
                                   inTime=event.inTime,
                                   outTime=event.outTime,
                                   playheadIndex=event.playheadIndex)
        self.messageDispatcher.sendMessage(msg)

    @remoteCallback
    def _onRemoteInOutChanged(self, msg):
        sequence = findItemByGuid(msg.sequenceGuid, filter=(Sequence, Clip))
        if (msg.inTime >= 0):
            sequence.setPlayheadInTime(msg.playheadIndex, msg.inTime)
        else:
            sequence.clearPlayheadInTime(msg.playheadIndex)

        if (msg.outTime >= 0):
            sequence.setPlayheadOutTime(msg.playheadIndex, msg.outTime)
        else:
            sequence.clearPlayheadOutTime(msg.playheadIndex)

    @localCallback
    def _onLocalInOutLockEnabledChanged(self, event):
        msg = messages.InOutLockEnabledChange(sequenceGuid=event.sequence.guid(),
                                              enabled=int(event.enabled))
        self.messageDispatcher.sendMessage(msg)

    @remoteCallback
    def _remoteInOutLockEnabledChanged(self, msg):
        sequence = findItemByGuid(msg.sequenceGuid, filter=(Sequence, Clip))
        sequence.setInOutEnabled(msg.enabled)
