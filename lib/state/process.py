from ..process.process import ProcessType
from .property import StatePropertyType


class StateProcess(StatePropertyType, ProcessType):
    def __init__(self, name, *args, **kwargs):
        StateProperty.__init__(self, name, *args, **kwargs)
        ProcessType.__init__(self, *args, **kwargs)

    @property
    def namespace(self):
        if self._parent is None:
            return self._namespace.copy()
        else:
            return self._parent.namespace.extend(self._namespace)
