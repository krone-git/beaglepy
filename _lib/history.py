

class SimulationHistoryFactory:
    def create(self, *args, **kwargs):
        return SimulationHistory(*args, **kwargs).to_dict()


class SimulationHistory:
    def __init__(self, *args, **kwargs):
        self._history = dict()

    def to_dict(self):
        return self._history
