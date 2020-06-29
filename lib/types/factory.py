from abc import ABCMeta, abstractmethod


class FactoryType(metaclass=ABCMeta):
    @abstractmethod
    def create(self, *args, **kwargs):
        raise NotImplementedError
