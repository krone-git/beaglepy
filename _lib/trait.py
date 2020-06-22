from .handler import ObjectHandler


class TraitHandler(ObjectHandler):
    def __init__(self, name, inheritance_handler, mutation_handler,
                    fitness_handler):
        self._name = name
        self._inheritance_handler = inheritance_handler
        self._mutation_handler = mutation_handler
        self._fitness_handler = fitness_handler

    def get_trait(self, organism):
        return self.get_value(organism, self._name)

    def set_trait(self, organism, value):
        self.set_value(organism, self._name, value)
        return self

    def inherit_trait(self, organism, parents):
        value = self._inheritance_handler.handle(
            self.get_trait(parents[0]),
            self.get_trait(parents[1])
            )
        value = self._mutation_handler.handle(value)
        self.set_trait(organism, value)
        return self

    def is_fit(self, organism, target):
        value = self.get_trait(organism)
        return self.fitness_handler.handle(value, target)

    def collect(self, handler, organism):
        #...
        handler.handle(organism)
        return self
