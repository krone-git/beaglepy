from abc import ABCMeta, abstractmethod
from random import randint, triangular, gauss


class ProbabilityCurveFactory:
    @classmethod
    def create(cls, skew=None, variance=None):
        if skew is None and variance is None:
            return FlatProbabilityCurve()
        elif skew:
            return TriangularProbabilityCurve(skew)
        else:
            return GaussianProbabilityCurve(variance)


class ProbabilityCurve(metaclass=ABCMeta):
    def __init__(self, weight):
        self._weight = weight

    @abstractmethod
    def call(self, value):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        return self.call(*args, **kwargs)


class FlatProbabilityCurve(ProbabilityCurve):
    def __init__(self, *args):
        pass

    def call(self, value, **kwargs):
        return randint(0, value)


class GaussianProbabilityCurve(ProbabilityCurve):
    def call(self, value, variance=None, **kwargs):
        variance = variance if variance else self._weight
        return gauss(round(value / 2), variance)


class TriangularProbabilityCurve(ProbabilityCurve):
    def call(self, value, **kwargs):
        return round(triangular(0, value, round(self._weight * value)))
