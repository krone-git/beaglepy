from abc import ABCMeta, abstractmethod


class ComponentType(metaclass=ABCMeta):
    pass


class NameComponent(ComponentType):
    def __init__(self, name, *args, **kwargs):
        self._name = str(name)

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"{self.__class__.__name__} '{self._name}'"

    def __repr__(self):
        return str(self)


class DescriptionComponent(ComponentType):
    def __init__(self, *args, *, description="", **kwargs):
        self._description = ""
        self.description = description

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = str(value)


class SimulationComponent(ComponentType):
    def __init__(self, *args, *, _simulation=None, **kwargs):
        self._simulation = _simulation
