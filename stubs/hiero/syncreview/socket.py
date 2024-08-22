import random
import asyncio
import collections
from datetime import datetime

import foundry.zmq as zmq
from hiero.core.util import asBytes

from .log import logDebug


class Socket:
    """
    Class which wraps around a zmq socket and allows for integration into an asyncio event loop.
    """

    def __init__(self):
        self._socket = None
        self._dataReceivedCallback = None
        self._eventLoop = asyncio.get_event_loop()
        self._sendQueue = collections.deque()

    def close(self):
        """ Close the socket and reset its state """
        if not self._socket:
            return
        socket = self._socket
        self._socket = None
        self._eventLoop.remove_writer(socket.FD)
        self._eventLoop.remove_reader(socket.FD)

        # Send any remaining messages left in the queue
        while socket.EVENTS & zmq.POLLOUT and self._sendQueue:
            data = self._sendQueue.popleft()
            socket.send_multipart(data)

        while self._sendQueue:
            data = self._sendQueue.popleft()
            logDebug(f"Socket.close failed to send message: {data[0]}")

        socket.close()

    def socketId(self):
        """ Get the zmq socket id. If the socket was not yet created returns an
        empty string
        """
        return self._socket.getsockopt(zmq.IDENTITY) if self._socket is not None else ''

    def _createSocket(self, type_):
        """ Create socket with specified type.
        """
        self._socket = zmq.Context.instance().socket(type_)
        # The last part of the ID is the time elapsed since the day started in UTC.
        # For the unlikely case of clients connecting at the same millisecond, a random prefix is added.
        strId = '{:x}-{}'.format(random.randint(0x0, 0x100),
                                 datetime.utcnow().strftime('%H:%M:%S.%f')[:-3])
        self._socket.setsockopt_string(zmq.IDENTITY, strId)

        self._eventLoop.add_reader(self._socket.FD, self._handleSocketEvents)
        self._eventLoop.add_writer(self._socket.FD, self._handleSocketEvents)

    def _handleSocketEvents(self):
        if not self._socket:
            return

        if self._socket.EVENTS & zmq.POLLIN:
            try:
                data = self._socket.recv_multipart(zmq.NOBLOCK)
                self._onDataReceived(data)
            except zmq.ZMQError as e:
                if e.errno == zmq.EAGAIN:
                    pass
            if not self._socket:
                return

        if self._socket.EVENTS & zmq.POLLOUT and self._sendQueue:
            data = self._sendQueue.popleft()
            self._socket.send_multipart(data)
            if not self._socket:
                return

        # Trigger another callback if there is more data to handle
        if self._socket.EVENTS & (zmq.POLLIN | zmq.POLLOUT):
            self._eventLoop.call_soon(self._handleSocketEvents)

    def _send(self, data):
        """ Send a list of data frames to the ZMQ socket.
        """
        if not self._socket:
            return
        self._sendQueue.append(data)

    def setDataReceivedCallback(self, callback):
        self._dataReceivedCallback = callback


class ServerSocket(Socket):
    """
    Socket which binds on a port and uses a ROUTER socket which can route messages
    to multiple clients.
    """

    def __init__(self):
        super(ServerSocket, self).__init__()

    def bind(self, url):
        """ Create the socket and bind on the specified url.
        """
        self._createSocket(zmq.ROUTER)
        self._socket.bind(url)

    def _onDataReceived(self, data):
        # Call the dataReceived callback for each message received
        sender = data[0]
        payload = data[2:]  # Strip the sender and empty frame
        if self._dataReceivedCallback:
            self._dataReceivedCallback(sender, payload)

    def send(self, receiver, frames):
        """ Send message frames to a given receiver. """
        logDebug('{}.send {}'.format(type(self), frames[0]))
        frames = [asBytes(receiver), b''] + frames
        self._send(frames)


class ClientSocket(Socket):
    """
    Socket which connects to a port and uses a DEALER socket for communications
    with a server.
    """

    def __init__(self):
        super(ClientSocket, self).__init__()

    def connectToHost(self, url):
        self._createSocket(zmq.DEALER)
        self._socket.connect(url)

    def _onDataReceived(self, data):
        # Emit all the received data, which may contain multiple messages
        # Our messages follow the zmq REQ/REP pattern of each address being followed by an empty frame.
        # DEALER sockets (unlike REQ) don't remove this when you receive, so we need to do it here.
        data = data[1:]
        if self._dataReceivedCallback:
            self._dataReceivedCallback(data)

    def send(self, frames):
        logDebug('{}.send {}'.format(type(self), frames[0]))
        frames = [b''] + frames
        self._send(frames)
