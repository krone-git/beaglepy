from ..types.factory import FactoryType
from abc import ABCMeta, abstractmethod


class ProcessIteratorFactory(FactoryType):
    def create(self, *args, **kwargs):
        return ProcessIterator(*args, **kwargs)


class ProcessIterator(ProcessIteratorType):
    def is_active(self):
        return False

    def next(self, state):
        pass

    def feed(self, state):
        pass


class RepetitionProcessIterator(ProcessIteratorType):
    def __init__(self, repetitions):
        self._repetitions = repetitions
        self._counter = 0

    def is_active(self):
        return self._repetitions > self._counter

    def next(self, state):
        self._counter += 1
        return self._counter

    def feed(self, state):
        #...
        pass


class ProcessIteratorType(metaclass=ABCMeta):
    @abstractmethod
    def is_active(self):
        raise NotImplementedError

    @abstractmethod
    def next(self, state):
        raise NotImplementedError

    @abstractmethod
    def feed(self, state):
        raise NotImplementedError
