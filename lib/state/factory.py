from ..types.factory import FactoryType
from .handler import StateHandler


class StateHandlerFactory(FactoryType):
    @classmethod
    def create(cls, *args, **kwargs):
        return StateHandler(*args, **kwargs)
