from ..component.collection import NamedComponentCollection, \
                                    ComponentCollectionFactory
from .interface import Trait
from .traits import INIT_TRAITS

__all__ = ()


class TraitCollection(NamedComponentCollection):
    def create_new_component(self, *args, **kwargs):
        return Trait(*args, **kwargs)


class TraitCollectionFactory(ComponentCollectionFactory):
    @classmethod
    def create_new_instance(cls,):
        return TraitCollection()

    @classmethod
    def instantiate(cls, collection, *args, **kwargs):
        collection.add_many(INIT_TRAITS)
        super().instantiate(collection, *args, **kwargs)
