from ..component.collection import ComponentCollection, \
                                    ComponentCollectionFactory
from .interface import Event

__all__ = ()


class EventCollection(ComponentCollection):
    def create_new_component(self, *args, **kwargs):
        return Event(*args, **kwargs)


class EventCollectionFactory(ComponentCollectionFactory):
    @classmethod
    def create_new_instance(cls):
        return EventCollection()
