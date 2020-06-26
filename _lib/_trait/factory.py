from .trait import TraitHandler
from .upkeep import TraitUpkeepHandler
from .fitness import TraitFitnessHandler
from .mutation import TraitMutationHandler
from .inheritance import TraitInheritanceHandler


class TraitHandlerFactory:
    @classmethod
    def create(cls, **kwargs):
        return TraitHandler(**kwargs)


class SubTraitHandlerFactory:
    @classmethod
    def create_inheritance_handler(cls, **kwargs):
        return TraitInheritanceHandler(**kwargs)

    @classmethod
    def create_mutation_handler(cls, **kwargs):
        return TraitMutationHandler(**kwargs)

    @classmethod
    def create_fitness_handler(cls, **kwargs):
        return TraitFitnessHandler(**kwargs)

    @classmethod
    def create_upkeep_handler(cls, **kwargs):
        return TraitFitnessHandler(**kwargs)
