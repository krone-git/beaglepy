from ..type.factory import FactoryType
from .process import Process
from .handler import ProcessHandler


class ProcessFactory(FactoryType):
    @classmethod
    def create(cls, *args, **kwargs):
        #...
        return Process(*args, **kwargs)


class ProcessHandlerFactory(FactoryType):
    @classmethod
    def create(cls, *args, **kwargs):
        #...
        return ProcessHandler(*args, **kwargs)
