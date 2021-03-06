from .engine import SimulationEngineFactory
from .export import ExportHandlerFactory


class Session:
    def __init__(self, **kwargs):
        self._engine = SimulationEngineFactory.create(**kwargs)
        self._exporter = ExportHandlerFactory.create(**kwargs)

    def simulate(self):
        self._engine.execute()

    def export(self, path=None):
        self._exporter.execute(
            data=self._engine.state,
            history=self._engine.history
            )
