from .engine import SimulationEngine

__all__ = ()


class SimulationEngineFactory:
    @classmethod
    def create_new(cls, interface):
        return SimulationEngine({})
