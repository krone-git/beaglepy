from .state import SimulationStateFactory
from .history import SimulationHistoryFactory
from .process import SimulationProcessFactory
from .console import SimulationConsoleFactory


class SimulationEngineFactory:
    @classmethod
    def create(self, **kwargs):
        state = SimulationStateFactory.create(**kwargs)
        history = SimulationHistoryFactory.create(**kwargs)
        processes = SimulationProcessFactory.create(**kwargs)
        console = SimulationConsoleFactory.create(**kwargs)
        return SimulationEngine(
            state=state,
            history=history,
            processes=processes,
            console=console
            )


class SimulationEngine:
    def __init__(self, state=None, history=None, processes=(), console=None):
        self._state = state
        self._history = history
        self._processes = processes
        self._console = console

    def execute(self):
        for process in self._processes:
            process.execute(self._state, self._history, self._console)
        return self._history
