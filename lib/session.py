from .engine import SimulationEngineFactory
from .export import ExportHandlerFactory


class Session:
    def __init__(self, generations, *args, exporter=None, **kwargs):
        self._engine = SimulationEngineFactory.create(
            generations=generations,
            **kwargs
            )
        self._export_handler = ExportHandlerFactory.create(**kwargs)

    def simulate(self):
        self._engine.simulate()

    def export(self, path=None):
        self._export_handler.export(
            path=path,
            history=self._engine.full_history()
            )
