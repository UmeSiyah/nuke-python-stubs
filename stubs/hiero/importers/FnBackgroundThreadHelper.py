# Copyright (c) 2024 The Foundry Visionmongers Ltd. All Rights Reserved.

from PySide2.QtCore import (Qt, Signal, QObject, QRunnable, QEventLoop,
                            QThreadPool)


class BackgroundFuncCallRunnable(QObject, QRunnable):
    """ Helper class for executing function in a thread belonging to a QThreadPool.
    Emits the _finished signal when the executions is completed. """

    _finished = Signal()

    def __init__(self, func, args):
        QObject.__init__(self)
        QRunnable.__init__(self)
        self._func = func
        self._args = args
        self._result = None
        self._exception = None

    def run(self):
        try:
            self._result = self._func(*self._args)
        except Exception as exception:
            self._result = None
            self._exception = exception
        self._finished.emit()


def runFunctionInBackgroundThread(func, *args):
    """ Execute the function with the given args in one of the threads owned by QThreadPool.globalInstance() but
    block until completed and return the result. The blocking is done in such a way that it
    allows the Qt event loop to run i.e. ensuring that the UI is responsive if called from the main thread.
    If an exception is thrown when running the function, it will be raised after the function is executed"""

    eventLoop = QEventLoop()
    backgroundFuncCallRunnable = BackgroundFuncCallRunnable(func, args)

    backgroundFuncCallRunnable._finished.connect(eventLoop.quit, Qt.QueuedConnection)
    QThreadPool.globalInstance().start(backgroundFuncCallRunnable)

    eventLoop.exec_()

    if backgroundFuncCallRunnable._exception:
        raise backgroundFuncCallRunnable._exception

    return backgroundFuncCallRunnable._result
