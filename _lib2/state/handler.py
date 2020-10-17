from abc import ABCMeta, abstractmethod


class StateHandler(StateHandlerType):
    pass


class StateHandlerType(metaclass=ABCMeta):
    def __init__(self):
        self._state = None
        self.new()

    def get(self):
        return self._state

    def new(self):
        self._state = dict()

    def get_value(self, key, namespace=[]):
        return self.get_item(namespace=namespace)[key]

    def set_value(self, key, value, namespace=[]):
        obj = self.get_item(namespace=namespace)[key] = value

    def get_item(self, namespace=[]):
        item = self._state
        for key in namespace:
            item = item[key]
        return item
