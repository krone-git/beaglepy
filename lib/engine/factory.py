from ..types.factory import FactoryType
from .engine import Engine


class EngineFactory(FactoryType):
    @classmethod
    def create(cls, *args, suite=None, **kwargs):
        engine = Engine(*args, **kwargs)
        if suite is not None:
            suite.build_engine(engine)
        return engine
