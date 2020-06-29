from .handler import ObjectHandler
from abc import ABCMeta, abstractmethod


class TraitHandlerFactory:
    def create(self, **kwargs):
        pass


class TraitHandler(ObjectHandler):
    def __init__(self, name, inheritance_handler, mutation_handler,
                    fitness_handler, upkeep_handler, collection_handler):
        self._name = name
        self._inheritance_handler = inheritance_handler
        self._mutation_handler = mutation_handler
        self._fitness_handler = fitness_handler
        self._upkeep_handler = upkeep_handler

        for handler in (inheritance_handler, mutation_handler,
                        fitness_handler, upkeep_handler):
            if handler._name is None:
                handler._name = name

    def get_trait(self, obj):
        return self.get_value(obj, self._name)

    def set_trait(self, obj, value):
        self.set_value(obj, self._name, value)
        return self

    def inheritance(self, obj, parents):
        value = self._inheritance_handler.handle(
            self.get_trait(parents[0]),
            self.get_trait(parents[1])
            )
        value = self._mutation_handler.handle(value)
        self.set_trait(obj, value)
        return self

    def fitness(self, obj, target):
        value = self.get_trait(obj)
        return self.fitness_handler.handle(value, target)

    def upkeep(self, obj):
        self._upkeep_handler.handle(obj)
        return self

    def collect(self, handler, obj):
        value = self.get_trait(obj)
        handler.add(value, obj)
        return self


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
