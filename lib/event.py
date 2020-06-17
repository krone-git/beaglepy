

class Event:
    def __init__(self, func, duration=1):
        self._func = func
        self._duration = duration

    @property
    def active(self):
        return self._duration > 0

    def execute(self, state):
        if self.active:
            self._func(state, self._duration)
            self._duration -= 1
