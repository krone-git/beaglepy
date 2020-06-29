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

    @abstractmethod
    def bool(self):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        return self.call(*args, **kwargs)

    def __bool__(self):
        return self.bool()


class AbsoluteProbabilityCurve(ProbabilityCurve):
    def call(self, *args, **kwargs):
        return self._weight

    def bool(self):
        return bool(self._weight)


class FlatProbabilityCurve(ProbabilityCurve):
    def call(self, value, **kwargs):
        return randint(0, value)

    def bool(self):
        return randint(0, 1)


class GaussianProbabilityCurve(ProbabilityCurve):
    def call(self, value, variance=None, **kwargs):
        variance = variance if variance else self._weight
        return gauss(round(value / 2), variance)

    def bool(self):
        value = abs(self.call(0, 0.5))
        while values > 1:
            value = abs(self.call(0, 0.5))
        weight = int(bool(self._weight))
        return abs(weight - value) > 0.5


class TriangularProbabilityCurve(ProbabilityCurve):
    def call(self, value, **kwargs):
        return round(triangular(0, value, round(self._weight * value)))

    def bool(self):
        return self.call(1) > 0.5
