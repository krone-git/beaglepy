from ..component.collection import NamedComponentCollection, \
                                    ComponentCollectionFactory, \
                                    SimulationComponentCollection
from .interface import Biome
from .biomes import INIT_BIOMES

__all__ = ()


class BiomeCollection(NamedComponentCollection,
                        SimulationComponentCollection):
    def __init__(self, *args, **kwargs):
        NamedComponentCollection.__init__(self, *args, **kwargs)
        SimulationComponentCollection.__init__(self, *args, **kwargs)

    def create_new_component(self, *args, **kwargs):
        return Biome(*args, **kwargs)


class BiomeCollectionFactory(ComponentCollectionFactory):
    @classmethod
    def create_new_instance(cls):
        return BiomeCollection()

    @classmethod
    def instantiate(self, collection, *args, **kwargs):
        collection.add_many(INIT_BIOMES)
        super().instantiate(collection, *args, **kwargs)
