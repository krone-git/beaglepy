

class HistoryHandler:
    __slots__ = (
        "_history",
        "_buffer"
        )

    def __init__(self):
        self._history = list()
        self._buffer = list()

    def get(self):
        return self._history

    def reset(self):
        self.reset_history()
        self.reset_buffer()

    def reset_history(self):
        self._history.clear()

    def reset_buffer(self):
        self._buffer.clear()

    def revert(self):
        if self._history:
            state = self._history.pop()
            self._buffer.append(state)
            return state

    def revert_all(self):
        self._buffer.extende(self._history)
        self.reset_history()

    def restore(self):
        if self._buffer:
            state = self._buffer.pop()
            self._history.append(state)
            return state

    def restore_all(self):
        self._history.extend(self._buffer)
        self.reset_buffer()

    def add(self, state):
        if self._buffer:
            self.reset_buffer()
        self._history.append(state)
