

class SimulationStateFactory:
    def create(self, *args, **kwargs):
        return SimulationState(*args, **kwargs).to_dict()


class SimulationState:
    def __init__(self, *args, **kwargs):
        self._state = dict()

    def to_dict(self):
        return self._state

