

class Engine:
    __slots__ = (
        "_history_handler",
        "_console_handler",
        "_state_handler",
        "_process_handler"
        )

    def __init__(self, history_handler, console_handler,
                    state_handler, process_handler):
        self._history_handler = history_handler
        self._console_handler = console_handler
        self._state_handler = state_handler
        self._process_handler = process_handler

    @property
    def history(self):
        return self._history_handler.get()

    @property
    def state(self):
        return self._state_handler.get()

    @property
    def console(self):
        return self._console_handler

    def execute(self):
        self._process_handler.execute(
            self._history_handler,
            self._state_handler,
            self._console_handler
            )
        return self
