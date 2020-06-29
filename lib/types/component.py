from abc import ABCMeta, abstractmethod


class ComponentType(metaclass=ABCMeta):
    def __init__(self, parent=None):
        self.set_parent(parent)

    @property
    def parent(self):
        return self._parent

    @property
    def master(self):
        if self._parent is None:
            return self
        else:
            return self._parent.master

    def set_parent(self, parent):
        self._parent = parent
