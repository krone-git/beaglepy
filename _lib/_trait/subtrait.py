from abc import ABCMeta, abstractmethod


class TraitSubHandler(metaclass=ABCMeta):
    def __init__(self, name=None):
        self._name = name

    @abstractmethod
    def handle(self, value, target):
        raise NotImplementedError

    def get_value(self, target):
        return ObjectHandler.get_value(target, self._name)

    def set_value(self, target, value):
        ObjectHandler.set_value(target, self._name, value)
        return self
