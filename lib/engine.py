from .state import SimulationStateFactory
from .history import SimulationHistoryFactory


class SimulationEngineFactory:
    @classmethod
    def create(self, processes=(,), **kwargs):
        state = SimulationStateFactory(**kwargs)
        history = SimulationHistoryFactory(**kwargs)
        return SimulationEngine(
            state=state,
            history=history,
            processes=processes
            )
    

class SimulationEngine:
    def __init__(self, state=None, history=None, processes=(,)):
        self._state = state
        self._history = history
        self._processes = processes

    def run(self):
        for process in self._processes:
            process.execute(self._state, self._history)
        return self._history
