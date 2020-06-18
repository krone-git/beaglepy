

class SimulationStateFactory:
    def create(self, *args, **kwargs):
        return SimulationState(*args, **kwargs)


class SimulationState:
    def __init__(self, *args, **kwargs):
        self.state = dict()

