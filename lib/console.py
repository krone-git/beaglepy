from abc import ABCMeta, abstractmethod

class Output(metaclass=ABCMeta):
    def print(self, *args, **kwargs):
        raise NotImplementedError
