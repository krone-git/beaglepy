

class Engine:
    __slots__ = (
        "_history_handler",
        "_console_handler",
        "_state_handler",
        "_process_handler"
        )

    def __init__(self, history_handler, console_handler,
                    state_handler, process_handler):
        _history_handler = None
        _console_handler = None
        _state_handler" = None
        _process_handler = None
        self.set_history_handler(history_handler)
        self.set_console_handler(console_handler)
        self.set_state_handler(state_handler)
        self.set_process_handler(process_state)

    @property
    def history(self):
        return self._history_handler.get()

    @property
    def state(self):
        return self._state_handler.get()

    @property
    def console(self):
        return self._console_handler

    def set_history_handler(self, handler):
        self._history_handler = history_handler

    def set_console_handler(self, handler):
        self._console_handler = console_handler

    def set_state_handler(self, handler):
        self._state_handler = state_handler

    def set_process_handler(self, state):
        self._process_handler = process_handler

    def execute(self):
        self._process_handler.execute(
            self._history_handler,
            self._state_handler,
            self._console_handler
            )
        return self
