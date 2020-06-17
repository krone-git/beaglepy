

class Session:
    def __init__(self, environment=None, population=None):
        self._environment = environment
        self._population = population
        self.export = ExportHandler()

    def simulate(self):
        pass
