from .trait import TraitComponentFactory
from .factory import IdTrackerType

__all__ = ()


class BiomeFactory(IdTrackerType, ComponentFactory):
    def _create_blank_component(self):
        return dict()

    def _initialize_component_traits(self, organism):
        pass
