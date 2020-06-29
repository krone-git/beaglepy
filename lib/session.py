from .engine import EngineFactory


class Session:
    def __init__(self):
        self._engine = EngineFactory.create()

    @property
    def history(self):
        return self._engine.history

    @property
    def state(self):
        return self._engine.state

    def execute(self):
        self._engine.execute()
