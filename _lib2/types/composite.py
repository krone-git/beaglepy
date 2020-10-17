from abc import ABCMeta, abstractmethod


class CompositeType(metaclass=ABCMeta):
    def __init__(self, *args, elements=(), accepts_element_types=None,
                    unique=False, **kwargs):
        self._elements = list()
        self.add_many(elements)
        self._acceptable_types = accepts_element_types
        self._unique = bool(unique)

    @property
    def elements(self):
        return tuple(self._elements)

    @property
    def acceptable_element_types(self):
        return self._acceptable_types

    def contains(self, element):
        return element in self._elements

    def accepts(self, element):
        if self._acceptable_type is None:
            return True
        else:
            return isinstance(element, self._acceptable_types)

    def is_unique(self):
        return self._unique

    def add(self, element, index=-1):
        if not self.accepts(element):
            raise TypeError
        if not self._unique or not element in self._elements:
            if element.parent is not None:
                element.parent.remove(element)
            element.set_parent(self)
            self._elements.insert(index, element)
        return self

    def add_many(self, elements):
        for element in elements:
            self.add(element)
        return self

    def remove(self, element):
        self._elements.remove(element)
        element.set_parent(None)
        return self

    def remove_all(self, element):
        while element in self._elements:
            self._elements.remove(element)
        element.set_parent(None)
        return self

    def clear(self):
        for element in self._elements.copy():
            self.remove(element)
        return self
