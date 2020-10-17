from ..attribute import AttributeHandler
from .attribute import GENERATION_LIMIT, CURRENT_GENERATION

__all__ = ()


class GenerationHandler:
    _current = AttributeHandler(CURRENT_GENERATION)
    _limit = AttributeHandler(GENERATION_LIMIT)

    @classmethod
    def get_generation_limit(cls, simulation):
        return cls._limit.get(simulation)

    @classmethod
    def set_generation_limit(cls, simulation, value):
        cls._limit.set(cls, simulation, value)

    @classmethod
    def get_current_generation(cls, simulation):
        return cls._current.get(simulation)

    @classmethod
    def set_current_generation(cls, simulation, value):
        cls._current.set(simulation, value)

    @classmethod
    def next_generation(cls, simulation):
        setter = cls._current.assign(simulation)
        setter += 1

    @classmethod
    def handle(cls, simulation):
        pass
