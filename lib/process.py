from abc import ABCMeta, abstractmethod


class SimulationProcess(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, state, history):
        raise NotImplementedError
