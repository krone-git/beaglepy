from ..component.interface import NamedComponent, DescribedComponent
from .inheritance import InheritanceHandler
from .mutation import MutationHandler
from .survival import SurvivalHandler

__all__ = (
  "Trait",
  )


class Trait(NamedComponent, DescribedComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._survival_handler = SurvivalHandler()
        self._inheritance_handler = InheritanceHandler()
        self._mutation_handler = MutationHandler()
