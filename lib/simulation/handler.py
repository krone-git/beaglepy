
__all__ = ()


class SimulationEngineHandler:
    def __init__(self):
        self._state = dict()

        self._biomes = list()
        self._traits = list()
        self._events = list()

    @property
    def biomes
