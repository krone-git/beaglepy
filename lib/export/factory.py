from ..types.factory import FactoryType
from .handler import ExportHandler


class ExportHandlerFactory(FactoryType):
    @classmethod
    def create(cls, *args, **kwargs):
        return ExportHandler(*args, **kwargs)
