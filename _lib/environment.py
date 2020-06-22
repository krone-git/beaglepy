from .state import SimulationStateHandler
from enum import Enum


# class EnvironmentVariableEnum(Enum):
    # SURVIVAL_TARGET = "survival_target"
    # RESOURCES = "resources"
    # MAX_RESOUCRES = "max_resources"
    # REPLENISH_RATE = "replenish_rate"


class EnvironmentFactory:
    _id = 0

    @classmethod
    def create(cls, center=0, radius=0):
        cls._id += 1
        return {
            cls._id: {
                SimulationStateHandler.ID: cls._id,
                EnvironmentHandler.CENTER: center,
                EnvironmentHandler.RADIUS: radius
                }
            }


class EnvironmentHandler(SimulationStateHandler):
    NAMESPACE = "environments"
    CENTER = "center"
    RADIUS = "radius"

    # @classmethod
    # def replenish(cls, environment):
    #     resources = cls.get_resources(environment)
    #     replenish_rate = cls.get_replenish_rate(environment)
    #     if isinstance(replenish_rate, int):
    #         resources += replenish_rate
    #     elif isinstance(replenish_rate, float):
    #         resources *= replenish_rate
    #     cls.set_resources(environment, resources)
    #     return cls
    #
    # @classmethod
    # def consume(cls, environment, value):
    #     resources = cls.get_resources(environment)
    #     resources -= value
    #     resources = 1 if resources < 1 else resources
    #     cls.set_resources(environment, resources)
    #     return cls

    @classmethod
    def get_center(cls, environment):
        return cls.get_value(environment, cls.CENTER)

    @classmethod
    def set_center(cls, environment, value):
        return cls.set_value(environment, cls.CENTER, value)

    @classmethod
    def get_radius(cls, environment):
        return cls.get_value(environment, cls.RADIUS)

    @classmethod
    def set_radius(cls, environment, value):
        return cls.set_value(environment, cls.RADIUS, value)

    @classmethod
    def contains(cls, environment, coord, divisor):
        center = cls.get_center(environment)
        x1, y1 = center % divisor, center // divisor
        x2, y2 = (coord % divisor) - x1, (coord // divisor) - y1
        return (x2 ** 2) + (y2 ** 2) <= cls.get_radius(environment) ** 2


# def make_get(name):
#     return classmethod(lambda cls, environment: cls.get_value(environment, name))
#
# def make_set(name):
#     return classmethod(lambda cls, environment, value: cls.set_value(environment, name, value))
#
# for i in EnvironmentVariableEnum:
#     setattr(EnvironmentHandler, i.name, i.value)
#     setattr(EnvironmentHandler, "set_" + i.value, make_set(i.value))
#     setattr(EnvironmentHandler, "get_" + i.value, make_get(i.value))
#
# del i, make_set, make_get
