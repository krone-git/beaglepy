from abc import ABCMeta, abstractmethod


class FitnessHandler(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def handle(self, value, target):
        pass

    def fitness(self, organism, target):
        return abs(target - self.get_trait(organism))
