import sys
import asyncio
import datetime
import threading

from . import log

# Need to override the default event loop type on Windows for the socket code to work
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class EventLoop:
    """ Wrapper around ayncio IOLoop, with some helpers for integrating it into the application. """

    def __init__(self):
        self._eventLoop = None
        self._startedEvent = threading.Event()

    def start(self):
        """ Start the event loop. Should be run in a thread. """
        self._eventLoop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._eventLoop)
        self._startedEvent.set()
        self._eventLoop.run_forever()
        self._eventLoop.close()
        self._startedEvent.clear()
        self._eventLoop = None

    def exit(self):
        """ Exit the event loop. """
        self.callInThread(self._eventLoop.stop)

    def waitForStart(self):
        """ Wait for the loop to start in another thread. """
        self._startedEvent.wait()

    def callInThread(self, callback, *args):
        """ Add a callback in the thread the event loop is running in.
        Can only be called once the event loop is running.
        """
        self._eventLoop.call_soon_threadsafe(callback, *args)


class Timer:
    """ Timer class for use with EventLoop. Somewhat mimics the QTimer interface. """

    def __init__(self):
        self._callback = None
        self._singleShot = False
        self._interval = datetime.timedelta()
        self._handle = None

    def setCallback(self, callback):
        """ Set the callback when the timer fires. """
        self._callback = callback

    def setSingleShot(self, singleShot):
        """ Set whether the timer should only fire once. """
        self._singleShot = singleShot

    def setInterval(self, interval):
        """ Set the timer interval, as a datetime.timedelta """
        self._interval = interval

    def start(self):
        """ Start or restart the timer. """
        if self._handle is not None:
            self.stop()
        self._handle = asyncio.get_event_loop().call_later(self._interval.total_seconds(), self._onTimeout)

    def stop(self):
        """ Stop the timer if it was running. """
        if self._handle is not None:
            self._handle.cancel()
            self._handle = None

    def _onTimeout(self):
        if self._callback:
            self._callback()
        self._handle = None
        if not self._singleShot:
            self.start()
