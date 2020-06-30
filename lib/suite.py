from abc import ABCMeta, abstractmethod


class Suite(SuiteType):
    pass


class SuiteType(metaclass=ABCMeta):
    @abstractmethod
    def build_engine(self, engine):
        raise NotImplementedError
