from abc import ABCMeta, abstractmethod


class StateProperty(StatePropertyType):
    pass


class StatePropertyType(metaclass=ABCMeta):
    def __init__(self, name, namespace=[], **kwargs):
        self._name = name
        self._namespace = namespace

    @property
    def name(self):
        return self._name

    @property
    def namespace(self):
        return self._namespace.copy()

    def get_value(self, state):
        return state.get_value(self._name, namespace=self._namespace)

    def set_value(self, state, value):
        state.set_value(self._name, value, namespace=self._namespace)
        return self
