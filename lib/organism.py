

class OrganismFactory:
    def create(self, *args, **kwargs):
        return Organism(*args, **kwargs)

        
class Organism:
    def __init__(self, coords=[0,0], survival=0, reproduction=0):
        self.coordinates = list(coords)
        self.survival_trait = survival
        self.reproductive_trait = reproduction
