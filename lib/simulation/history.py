
__all__ = ()


class HistoryHandler:
    def __init__(self):
        self._history = []

    def record_state(self, state):
        self._history.append(state.copy())
