
__all__ = ()


class StateHandler:
    def __init__(self):
        self._state = dict()

    @property
    def state(self):
        return self._state
