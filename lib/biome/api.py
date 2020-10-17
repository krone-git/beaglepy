from ..component.interface import NamedComponent, DescribedComponent, \
                                    SimulationComponent

__all__ = (
    "Biome",
    )


class Biome(NamedComponent, DescribedComponent, SimulationComponent):
    def __init__(self, *args, **kwargs):
        NamedComponent.__init__(self, *args, **kwargs)
        DescribedComponent.__init__(self, *args, **kwargs)
        SimulationComponent.__init__(self, *args, **kwargs)
