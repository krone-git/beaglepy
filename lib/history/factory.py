from ..types.factory import FactoryType
from .handler import HistoryHandler


class HistoryHandlerFactory(FactoryType):
    @classmethod
    def create(cls, *args, **kwargs):
        return HistoryHandler(*args, **kwargs)
