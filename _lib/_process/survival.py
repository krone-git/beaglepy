from .process import SimulationProcess


class SurvivalProcess:
    def execute(self, state, console):
        for process in self._processes:
            
