from abc import ABCMEta, abstractmethod
from ..types.node import NodeType


class Process(ProcessType):
    def call(self, state, console):
        return state


class ProcessType(NodeType, metaclass=ABCMeta):
    def __init__(self, *args, execution_order=None, **kwargs):
        NodeType.__init__(self, *args, **kwargs)
        self._execution_method = ProcessExecutionMethod.call(execution_order)

    def execute(self, state, console):
        return self._execution_method(self, state, console)

    def execute_ascending(self, state, console):
        for element in self._elements:
            element.execute_ascending(state, console)
        self.call(state, console)
        return state

    def execute_descending(self, state, console):
        self.call(state, console)
        for element in self._elements:
            element.execute(state, console)
        return state

    def execute_elements(self, state, console):
        for element in self._elements:
            element.execute(self, state, console)
        return state

    def execute_call(self, state, console):
        self.call(self, state, console)
        return state

    @abstractmethod
    def call(self, state, console):
        raise NotImplementedError


class ProcessExecutionMethod:
    ASCENDING = "ascending"
    DESCENDING = "descending"
    ASCENDING_KEYS = ("1", "a", "ascend", ASCENDING)
    DESCENDING_KEYS = ("0", "d", "descend", DESCENDING)

    @classmethod
    def call(cls, order):
        if callable(order):
            return order
        else:
            order = str(order).lower()

        if not order or order in cls.DESCENDING:
            return self.execute_descending
        elif order in cls.ASCENDING:
            return self.execute_ascending
        else:
            raise ValueError
