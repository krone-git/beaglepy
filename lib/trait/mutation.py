
__all__ = (
    "MutationHandler",
    )

class MutationHandler:
    def __init__(self, probability=(lambda self: 1),
                    range=(lambda self: 1), **kwargs):
        self._propability_function = probability
        self._range_function = range
        for k, v in kwargs.items():
            if getattr(k, None) is None:
                setattr(self, k, v)

    def handle(self, trait_value, state):
        if self._probability_function(self) == 1:
            trait_value += self._range_function(self)
        return trait_value
