import threading
import traceback

from hiero.core import executeInMainThread
from PySide2.QtCore import Qt, Signal, QObject

from . import messages
from .log import logMessage, logException


class MessageDispatcher(QObject):
    """ Receives messages from a connected session and forwards them to registered
    callbacks. Also allows for sending messages back.
    """

    _handleReceivedMessages = Signal()

    def __init__(self, eventLoop, messageClient):
        super(MessageDispatcher, self).__init__()
        self._eventLoop = eventLoop
        self._messageClient = messageClient
        self._messageClient.setMessageReceivedCallback(self._onMessageReceivedInNetworkThread)
        self._messageLock = threading.Lock()
        self._dispatchMessagesPending = False
        self._handleReceivedMessages.connect(
            self._dispatchReceivedMessagesInMainThread, Qt.QueuedConnection)
        self._messagesFromNetwork = []
        self._messagesForDispatch = []
        self._handlingIncomingMessages = False
        self._messageCallbacks = {}

    def _registerCallback(self, msgType, callback):
        """ Register a callback for a particular message type """
        if msgType not in self._messageCallbacks:
            self._messageCallbacks[msgType] = list()
        self._messageCallbacks[msgType].append(callback)

    def _onMessageReceivedInNetworkThread(self, msg):
        """ Callback when a message is received from the network connection. Queues messages for handling on the main thread.
        """
        with self._messageLock:
            logMessage('MessageDispatcher._onMessageReceivedInNetworkThread: {}'.format(msg))
            self._messagesFromNetwork.append(msg)
            if not self._dispatchMessagesPending:
                self._dispatchMessagesPending = True
                self._handleReceivedMessages.emit()

    def _dispatchReceivedMessagesInMainThread(self):
        """ Process any received messages on the main thread. """
        with self._messageLock:
            self._messagesForDispatch.extend(self._messagesFromNetwork)
            self._messagesFromNetwork = []
            self._dispatchMessagesPending = False

        self._messagesForDispatch = messages.applyMessageFilters(self._messagesForDispatch)

        # In certain situations (e.g. when loading a project) more messages can be received while the current one is still
        #  being processed. This makes the sync logic more complex, so return early if this is called recursively.
        if self._handlingIncomingMessages:
            return

        self._handlingIncomingMessages = True
        while self._messagesForDispatch:
            msg = self._messagesForDispatch.pop(0)
            try:
                callbacks = self._messageCallbacks.get(type(msg), [])
                for callback in callbacks:
                    callback(msg)
            except:
                logException(
                    'MessageDispatcher._dispatchReceivedMessagesInMainThread: Error handling message {}'.format(msg))
        self._handlingIncomingMessages = False

    def sendMessage(self, msg):
        """ Send a message back to the connected session """
        logMessage('MessageDispatcher.sendMessage: {}'.format(msg))
        self._eventLoop.callInThread(self._messageClient.sendMessage, msg)

    def shutdown(self):
        self._messageCallbacks.clear()
        self._messageClient.setMessageReceivedCallback(None)
        self._messageClient = None
