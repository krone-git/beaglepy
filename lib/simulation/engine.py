from .history import HistoryHandler
from .generation import GenerationHandler
from .propagation import PropagationHandler
from .trait import SimulationTraitHandler
from .event import SimulationEventHandler
from .console import ConsoleHandler

__all__ = ()


class SimulationEngine:
    def __init__(self, handler):
        self._handler = handler
        self._history = HistoryHandler()

    def run(self):
        handler_method_sequence = (
                GenerationHandler.handle,
                SimulationTraitHandler.handle,
                SimulationEventHandler.handle,
                PropagationHandler.handle,
                self._history.record_state,
                ConsoleHandler.handle
            )
        generation_limit = GenerationHandler.get_generation_limit(
                                self._handler
                                )

        PropagationHandler.instantiate(self._handler)
        self._history.record_state(self._handler)
        for generation in range(generation_limit):
            for handler_method in handler_method_sequence:
                handler_method(self._handler)
