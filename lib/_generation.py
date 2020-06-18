import copy


class GenerationFactory:
    def create(self, *args, **kwargs):
        return Generation(*args, **kwargs)


class Geneology:
    def __init__(self):
        self._generations = []

    @property
    def generations(self):
        return self._generations

    def new(self, *args, **kwargs):
        return GenerationFactory.create(*args, **kwargs)

    def add(self, generation):
        if generation not in self._generations:
            self._generations.append(generation)

    def add_new(self, *args, **kwargs):
        generation = self.new(*args, **kwargs)
        self.add(generation)


class Generation:
    def __init__(self, world):
        self._world = copy.deepcopy(world)

    @property
    def world(self):
        return self._world
