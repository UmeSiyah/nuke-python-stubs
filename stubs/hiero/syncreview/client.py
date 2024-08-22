from . import config, messages
from .log import logDebug, logMessage, logException
from .socket import ClientSocket
from .eventloop import Timer
from .connectionstate import ConnectionState


def allowClientTimeout(clientId):
    """ Check if the client should time out, this does not happen for the client
    object used by the host.
    """
    return clientId != config.HOST_ID


class Client:
    """
    Class representing a client in the sync. Maintains a connection to the server
    and allows for sending and receiving messages.
    """

    # Initialise with a ConnectionState object which may be shared with other classes,
    # and an id which is used to identify this client across connections
    def __init__(self, connectionState, clientId):
        self._connectionState = connectionState
        self._clientId = clientId
        self._allowTimeout = allowClientTimeout(clientId)
        self._socket = None
        self._heartbeatSendTimer = None
        self._heartbeatTimeoutTimer = None
        self._numberOfClientsChangedCallback = None
        self._messageReceivedCallback = None

    def connectionState(self):
        """ Get the client's connection state """
        return self._connectionState

    def socketId(self):
        """ Get the socket Id used by this client. """
        return self._socket.socketId()

    def connectToHost(self, host, port, clientData):
        """ Try to connect on the given host and port. May raise an exception if the
        host isn't valid.
        """
        logMessage("Client.connectToHost host: '{}' port: {}".format(host, port))
        try:
            self._connectionState.setState(ConnectionState.CLIENT_CONNECTING)
            self._socket = ClientSocket()
            self._socket.setDataReceivedCallback(self._onDataReceived)
            self._socket.connectToHost('tcp://{}:{}'.format(host, port))
            message = messages.Connect(protocolVersion=config.PROTOCOL_VERSION,
                                       applicationVersion=config.APPLICATION_VERSION,
                                       clientData=clientData)
            logMessage('Client.connectToHost sending connect message '
                       'clientId: {} socketId: {} message: {}'.format(
                           self._clientId, self.socketId(), message))
            self.sendMessage(message)
            if self._allowTimeout:
                self._createHeartbeatTimers()
                self._heartbeatTimeoutTimer.start()
        except:
            self._connectionState.setError(ConnectionState.ERROR_CONNECT_INVALID_HOST)
            raise

    def _createHeartbeatTimers(self):
        if self._allowTimeout:
            self._heartbeatSendTimer = Timer()
            self._heartbeatSendTimer.setInterval(config.HEARTBEAT_INTERVAL)
            self._heartbeatSendTimer.setCallback(self._onHeartbeatSendTimeout)
            self._heartbeatTimeoutTimer = Timer()
            self._heartbeatTimeoutTimer.setSingleShot(True)
            self._heartbeatTimeoutTimer.setInterval(config.HEARTBEAT_TIMEOUT)
            self._heartbeatTimeoutTimer.setCallback(self._onServerTimeout)

    def disconnectFromHost(self):
        """ Close the connection. If a connection had been successfully established
        with the host, a disconnect message is sent, otherwise just close the socket
        etc
        """
        if self._connectionState == ConnectionState.CLIENT_CONNECTED:
            logMessage('Client.disconnectFromHost')
            self.sendMessage(messages.Disconnect())
        self._disconnected()

    def _disconnected(self):
        if not self._socket:
            return
        self._connectionState.setState(ConnectionState.DISCONNECTED)
        self._socket.close()
        self._socket = None
        if self._allowTimeout:
            self._heartbeatTimeoutTimer.stop()
            self._heartbeatSendTimer.stop()

    def _onDataReceived(self, data):
        if self._allowTimeout:
            self._heartbeatTimeoutTimer.start()

        # data may contain multiple messages. deserialize then apply filters before
        # handling them
        logDebug('Client._onDataReceived messages: {}'.format(data[0]))

        msg = messages.deserializeMessage(data)
        if self._connectionState == ConnectionState.CLIENT_CONNECTING:
            if isinstance(msg, messages.ConnectResponse):
                self._handleConnectResponse(msg)
        elif self._connectionState == ConnectionState.CLIENT_CONNECTED:
            if isinstance(msg, messages.Disconnect):
                logDebug('Client: received Disconnect message')
                self._disconnected()
            elif isinstance(msg, messages.Pong):
                pass
            elif isinstance(msg, messages.NumberOfPeers):
                if self._numberOfClientsChangedCallback:
                    self._numberOfClientsChangedCallback(msg.content)
            else:
                if self._messageReceivedCallback:
                    self._messageReceivedCallback(msg)

    def _handleConnectResponse(self, msg):
        if msg.result == ConnectionState.ERROR_NONE:
            self._connectionState.setState(ConnectionState.CLIENT_CONNECTED)
            if self._allowTimeout:
                self._heartbeatSendTimer.start()
        else:
            self._connectionState.setError(msg.result, msg.responseText)

    def sendMessage(self, msg):
        logDebug(f"Client.sendMessage {type(msg)} {id(msg)}")
        if not self._socket:  # Guard against this callback happening after the socket has closed
            return
        msg.sender = self._clientId
        self._socket.send(msg.serialize())

    def _onHeartbeatSendTimeout(self):
        logDebug('Client._onHeartbeatSendTimeout')
        self.sendMessage(messages.Ping())

    def _onServerTimeout(self):
        logMessage('Client: Connection to server timed out')
        # Set error state, with different codes if already connected vs trying to connect
        if self._connectionState == ConnectionState.CLIENT_CONNECTING:
            self._connectionState.setError(ConnectionState.ERROR_CONNECT_TIMEOUT)
        else:
            self._connectionState.setError(ConnectionState.ERROR_CONNECTION_LOST)

    def setNumberOfClientsChangedCallback(self, callback):
        self._numberOfClientsChangedCallback = callback

    def setMessageReceivedCallback(self, callback):
        self._messageReceivedCallback = callback
