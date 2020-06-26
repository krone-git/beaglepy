from .trait import TraitSubHandler
from ..probability import ProbabilityCurveFactory


class TraitMutationHandler(TraitSubHandler):
    def __init__(self, chance_probability_curve=None,
                 modifier_probability_curve=None, **kwargs):
        self._chance_probability_curve = chance_probability_curve
        self._modifier_probability_curve = modifier_probability_curve

    def handle(self, value):
        if self._chance_probability_curve.bool():
            
