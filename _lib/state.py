from .handler import ObjectHandler


class SimulationStateFactory:
    def create(self, *args, **kwargs):
        #...
        return dict()


class SimulationStateHandler(ObjectHandler):
    NAMESPACE = ""
    ID = "id"

    @classmethod
    def get_id(cls, obj):
        return self.get_value(obj, cls.ID)

    @classmethod
    def get_by_id(cls, state, _id):
        return self.get_value(
            self.get_value(state, cls.NAMESPACE),
            _id
            )
