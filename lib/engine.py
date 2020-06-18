from .state import SimulationStateFactory
from .history import SimulationHistoryFactory


class SimulationEngineFactory:
    @classmethod
    def create(self, processes=(), **kwargs):
        state = SimulationStateFactory(**kwargs)
        history = SimulationHistoryFactory(**kwargs)
        console = S
        return SimulationEngine(
            state=state,
            history=history,
            processes=processes
            )
    

class SimulationEngine:
    def __init__(self, state=None, history=None, processes=(), console=None):
        self._state = state
        self._history = history
        self._processes = processes
        self._console = console

    def run(self):
        for process in self._processes:
            process.execute(self._state, self._history, self._console)
        return self._history
