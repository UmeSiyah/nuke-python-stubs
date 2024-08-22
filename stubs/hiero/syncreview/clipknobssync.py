from hiero.core import Clip, events, findItemByGuid

from . import messages
from .log import logMessage
from .synctool import SyncTool, localCallback, remoteCallback

messages.defineMessageType('ClipKnobChanged', ('itemGuid', str),
                           ('knobName', str), ('knobScript', str))


class SyncClipKnobsTool(SyncTool):
    """
    Tool for syncing the knob values of clips
    """

    def __init__(self, messageDispatcher):
        super(SyncClipKnobsTool, self).__init__(messageDispatcher)
        self.registerEventCallback(events.EventType.kClipKnobChanged, self.onLocalClipKnobChanged)
        self.messageDispatcher._registerCallback(
            messages.ClipKnobChanged, self.onRemoteClipKnobChanged)

    @localCallback
    def onLocalClipKnobChanged(self, event):
        """ Process a knob changed callback """
        # The event has the knob name, not the object, look it up on the node
        knob = event.item.readNode().knob(event.knobName)

        # It is valid for there not to be a knob here, there are some special callbacks
        # with knobs which do not actually belong to the node. These don't need to be synced
        if not knob:
            return
        value = knob.toScript()
        msg = messages.ClipKnobChanged(itemGuid=event.item.guid(),
                                       knobName=event.knobName,
                                       knobScript=knob.toScript())
        self.messageDispatcher.sendMessage(msg)

    @remoteCallback
    def onRemoteClipKnobChanged(self, msg):
        """ Process a remote knob changed message """
        item = findItemByGuid(msg.itemGuid, filter=(Clip))
        if not item:
            logMessage('onRemoteClipKnobChanged Clip {} not found!'.format(msg.itemGuid))
            return
        knob = item.readNode().knob(msg.knobName)
        if not knob:
            logMessage('onRemoteClipKnobChanged knob {} not found!'.format(msg.knobName))
            return
        knob.fromScript(msg.knobScript)
