from abc import ABCMeta, abstractmethod
from .trait import TraitSubHandler


class TraitFitnessHandler(TraitSubHandler):
    def __init__(self, threshold=None, **kwargs):
        TraitSubHandler.__init__(self, **kwargs)
        self._threshold = threshold

    def fitness(self, value, target):
        return abs(target - value)


class ThresholdFitnessHandler(FitnessHandler):
    def handle(self, value, target):
        _target = self.get_value(target)
        return self.fitness(value, _target) < threshold


class DepletionFitnessHandler(FitnessHandler):
    def handle(value, target):
        _target = self.get_value(target)
        _target -= value
        self.set_value(target, _target)
        return _target < self._threshold
