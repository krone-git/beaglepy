

class EnvironmentFactory:
    @classmethod
    def create(cls, *args, **kwargs):
        return Environment(*args, **kwargs)


class Environment:
    def __init__(self, environments=(), radius=None, survival=None,
                 center=(0, 0), max_resources=None, replenish_rate=None):
#        self.environments = list(environments)
        self.raidus = raidus
        self.survival_target = survival
        self.center = list(center)
        self.max_resources = self.resources = max_resources
        self.resource_replenishment_rate = replenish_rate

#    def add(self, environment):
#        self.environments.append(environment)
#        return self

#    def remove(self, environment):
#        self.environments.remove(environment)

    def contains(self, x, y):
        return ((x - self.center[0]) ** 2) + \
               ((y - self.center[1]) ** 2) < self.radius ** 2

    def replenish(self):
        if self.resources < 1:
            self.resources  = 1
        if isinstance(self.resource_replenishment_rate, float):
            self.resources *= self.resource_replenishment_rate
        elif isinstance(self.resource_replenishment_rate, int):
            self.resources += self.resource_replenishment_rate
        else:
            raise TypeError
        return self
