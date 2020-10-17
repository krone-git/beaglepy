from abc import ABCMeta, abstractmethod
from string import ascii_letters, ascii_digits
from functools import wraps

from .component import ComponentType, NameComponent, SimulationComponent


_allowable_component_name_chars = ascii_letters + ascii_digits + "_ "
def format_component_name(name):
    name = str(name)
    if name[0] in ascii_digits or not in _allowable_component_name_chars:
        raise ValueError(
            "'name' must begin with '_' or an alphabetic character: " \
            f"'{name[0]}' found"
            )

    table = {
        c: "" for c in name if c not in _allowable_component_name_chars
        }
    trans = str.maketrans({**table, " ":"_"})
    return name.translate(trans).lower()


class ComponentCollection(metaclass=ABCMeta):
    def __init__(self, *args, *, components=[], **kwargs):
        self._collection = tuple(components)

    def get(self, index):
        return self._collection[index]

    __getitem__ = get


class MutableComponentCollection(ComponentCollection):
    def __init__(self, *args, *, components=[], **kwargs):
        self._collection = list()
        self.add_many(components)

    @abstractmethod
    def create_new(self, *args, **kwargs):
        raise NotImplementedError

    def is_valid_member(self, component):
        return isinstance(component, self._component_type)

    def add(self, component):
        self._collection.append(component)
        return self

    def add_new(self, *args, **kwargs):
        component = self.create_new(*args, **kwargs)
        self.add(component)
        return component

    def add_many(self, components):
        for component in components:
            self.add(component)
        return self

    def pop(self, index):
        return self._collection.pop(index)

    def remove(self, component):
        self._collection.remove(component)
        return self

    def remove_many(self, components):
        for component in components:
            self.remove(component)
        return self


class NameComponentCollection(metaclass=ABCMeta):
    def __init__(self, *args, *, components=[], **kwargs):
        self._collection = dict()
        self._collection.update(
            {_format_component_name(component.name): component
                for component in components}
            )

    def get(self, name):
        name = _format_component_name(name)
        return self._collection[name]

    __getitem__ = get


class MutableNameComponentcollection(NameComponentCollection):
    def __init__(self, *args, *, components=[], **kwargs):
        self._collection = dict()
        self.add_many(components)

    @abstractmethod
    def create_new(self, *args, **kwargs):
        raise NotImplementedError

    def is_valid_member(self, component):
        return isinstance(component, self._component_type)

    def add(self, component):
        name = _format_component_name(component.name)
        self._collection[name] = component
        return self

    def add_new(self, *args, **kwargs):
        component = self.create_new(*args, **kwargs)
        self.add(component)
        return component

    def add_many(self, components):
        for component in components:
            self.add(component)
        return self

    def remove(self, name):
        name = _format_component_name(name)
        return self._collections.pop(name)

    def remove_many(self, names):
        return {
            name: self.remove(name) for name in names
            }


class ConstantComponentCollection:
    def __new__(metacls, cls, bases, namespace, **kwargs):
        def getattributemethod(func):
            @wraps(func)
            def _getattributemethod(self, name):
                name = str(name)
                try:
                    collection = object.__getattribute__(self, "_collection")
                except AttributeError as e:
                    collection = dict()
                if name.isupper() \
                and fmt_name := format_component_name(name) in collection:
                    return fmt_name
                else:
                    return func(self, name)
            return _getattribute

        def setattributemethod(func):
            @wraps(func)
            def _setattributemethod(self, name, value):
                name = str(name)
                try:
                    collection = object.__getattribute__(self, "_collection")
                except AttributeError as e:
                    collection = dict()
                if name.isupper() \
                and fmt_name := format_component_name(name) in collection:
                    raise AttributeError(
                        f"Cannot set attribute '{name}'"
                        )
                else:
                    return func(self, name, value)
            return _setattribute

        cls.__getattribute__ = getattributemethod(cls.__getattribute__)
        cls.__stetattr__ = setattributemethod(cls.__setattr__)
        return super(cls).__new__(cls)


class PropertyComponentCollection:
    def __new__(metacls, cls, bases, namespace, **kwargs):
        def getattributemethod(func):
            @wraps(func)
            def _getattributemethod(self, name):
                name = str(name)
                try:
                    collection = object.__getattribute__(self, "_collection")
                except AttributeError as e:
                    collection = dict()
                if name.islower() \
                and fmt_name := format_component_name(name) in collection:
                    return collection[name]
                else:
                    return func(self, name)
            return _getattribute

        def setattributemethod(func):
            @wraps(func)
            def _setattributemethod(self, name, value):
                name = str(name)
                try:
                    collection = object.__getattribute__(self, "_collection")
                except AttributeError as e:
                    collection = dict()
                if name.islower() \
                and fmt_name := format_component_name(name) in collection:
                    raise AttributeError(
                        f"Cannot set attribute '{name}'"
                        )
                else:
                    return func(self, name, value)
            return _setattribute

        cls.__getattribute__ = getattributemethod(cls.__getattribute__)
        cls.__stetattr__ = setattributemethod(cls.__setattr__)
        return super(cls).__new__(cls)


class SimulationComponentComponent(SimulationComponent):
    def __new__(metacls, cls, bases, namespace, **kwargs):
        cls = super().__new__(metacls, name, bases, namespace, **kwargs)
        cls.add = addsimulationmethod(cls.add)
        cls.remove = removesimulationmethod(cls.remove)
        return cls
