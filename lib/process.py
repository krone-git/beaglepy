from abc import ABCMeta, abstractmethod


class SimulationProcess(metaclass=ABCMeta):
    def __init__(self, *args, processes=(), **kwargs):
        self._processes = list(processes)

    def execute(self, state, history):
        self.operation(state, history)
        [p.execute(state, history) for p in self._processes]
        return self

    @abstractmethod
    def operation(self, state, history):
        raise NotImplementedError

