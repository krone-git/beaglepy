from ..types.factory import FactoryType
from .engine import Engine


class EngineFactory(FactoryType):
    @classmethod
    def create(cls, *args, **kwargs):
        return Engine(*args, **kwargs)
