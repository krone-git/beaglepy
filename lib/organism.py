from .state import SimulationStateHandler


class OrganismFactory:
    _id = 0

    @classmethod
    def create(cls, parents=[None, None]):
        cls._id += 1
        return {
            cls._id: {
                SimulationStateHandler.ID: cls._id,
                OrganismEnum.PARENTS: parents
                }
            }


class OrganismHandler(SimulationStateHandler):
    NAMESPACE = "organisms"
    PARENTS = "parents"

    @classmethod
    def get_parents(cls, organism):
        return self.get_value(organism, cls.PARENTS)
