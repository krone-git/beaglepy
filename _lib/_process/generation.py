from .process import SimulationProcess
from ..handler import ObjectHandler


class GenerationProcess(SimulationProcess):
    def __init__(self, generations=1000, **kwargs):
        self._generations = generations
        self._history = dict()
        SimulationProcess.__init__(self, **kwargs)

    @property
    def generations(self):
        return self._generations

    @property
    def history(self):
        return self._history

    def execute(self, state, console):
        for generation in self._generations:
            GenerationStateHandler.set_generation(state, generation)
            for process in self._processes:
                process.execute(state, console)
            self._history[generation] = state.copy()

    def operation(self, state, history, console):
        pass


class GenerationStateHandler(ObjectHandler):
    @classmethod
    def set_generation(cls, obj, value):
        cls.set_value(obj, "generation", value)
        return cls
