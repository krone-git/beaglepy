
__all__ = ()


class TraitComponentFactory(metaclass=ABCMeta):
    def create_new_component(self):
        component = self._create_blank_component()
        self._initialize_component_traits(component)
        return component

    @abstractmethod
    def _create_blank_component(self):
        raise NotImplementedError

    @abstractmethod
    def _initialize_component_traits(self, component):
        raise NotImplementedError
