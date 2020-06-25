from abc import ABCMeta, abstractmethod



class SimulationProcessFactory:
    @classmethod
    def create(cls, **kwargs):
        return SimulationProcess(**kwargs)


class SimulationProcess(metaclass=ABCMeta):
    def __init__(self, processes=(), **kwargs):
        self._processes = list(processes)

    def execute(self, state, history, console):
        self.operation(state, history, console)
        [p.execute(state, history, console) for p in self._processes]
        return self

    @abstractmethod
    def operation(self, state, history, console):
        raise NotImplementedError
