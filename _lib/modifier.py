from abc import ABCMeta, abstractmethod


class ModifierHandler:
    def __init__(self, function, probability_handler=None):
        self._function = function
        self._probability_handler = probability_handler

    def handle(self, value):
        if self._probability_handler:
            _value = self._probability_handler.handle(value)
        else:
            _value = value
        return self._function(value, _value)


class ModifierFunction(metaclass=ABCMeta):
    @abstractmethod
    def call(value, default_value):
        raise NotImplementedError

    __call__ = call
