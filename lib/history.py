

class SimulationHistoryFactory:
    def create(self, *args, **kwargs):
        return SimulationHistory(*args, **kwargs)


class SimulationHistory:
    def __init__(self, *args, **kwargs):
        self._history = dict()

    @property
    def history(self):
        self._history.copy()

    def add(self, state_id, state):
        self._history[state_id] = state
        
