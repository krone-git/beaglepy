from ..probablity import ProbabilityCurveFactory
from .subtrait import TraitSubHandler
from random import randint
from statistics import mean
from math import floor


class TraitInheritanceHandler(TraitSubHandler):
    def __init__(self, probability_curve=None, **kwargs):
        if probability_curve is None:
            probability_curve = ProbabilityCurveFactory(**kwargs)
        self._probability_curve = probability_curve


class DominanceInheritanceHandler(InheritanceHandler):
    def handle(self, parent_a, parent_b):
        #... currently only favors position in parenting pair
        if self._probability_curve.call(1) > 0:
            return parent_a
        else:
            return parent_b


class RandomInheritanceHandler(InheritanceHandler):
    def handle(self, parent_a, parent_b):
        return randint(
            min(parent_a, parent_b),
            max(parent_a, parent_b)
            )


class AverageInheritanceHandler(InheritanceHandler):
    def handle(self, parent_a, parent_b):
        diff = abs(parent_a - parent_b)
        mod = self._probability_curve.call(diff) - round(diff / 2)
        return floor(mean(parent_a, parent_b)) + mod
