from .engine import EngineFactory


class Session:
    def __init__(self, *args, **kwargs):
        self._engine = EngineFactory.create(*args, **kwargs)
        self._export_handler = ExportHandlerFactory(*args, **kwargs) #...

    @property
    def history(self):
        return self._engine.history

    @property
    def state(self):
        return self._engine.state

    @property
    def engine(self):
        return self._engine

    @property
    def export_handler(self):
        return self._export_handler

    def execute(self):
        self._engine.execute()

    def export(self, location):
        #...
        pass
