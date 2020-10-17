from ..trait.collection import TraitCollectionFactory
from ..biome.collection import BiomeCollectionFactory
from ..event.collection import EventCollectionFactory
from ..environment.factory import EnvironmentSettingsFactory
from ..console.factory import ConsoleFactory
from .factory import SimulationEngineFactory

__all__ = (
    "Simulation",
    )


class Simulation:
    def __init__(self, traits=[], biomes=[], events=[], environment={},
                    console=None, **kwargs):
        self._trait_collection = TraitCollectionFactory.create_new(
            components=traits
            )
        self._biome_collection = BiomeCollectionFactory.create_new(
            components=biomes,
            simulation=self
            )
        self._event_collection = EventCollectionFactory.create_new(
            components=events
            )

        environment = environment.copy()
        environment.update(kwargs)
        self._environment_settings = EnvironmentSettingsFactory.create_new(
            **environment
            )

        self._console = ConsoleFactory.create_new(console=console)

    @property
    def traits(self):
        return self._trait_collection

    @property
    def biomes(self):
        return self._biome_collection

    @property
    def events(self):
        return self._event_collection

    @property
    def environment(self):
        return self._environment_settings

    def start(self):
        engine = SimulationEngineFactory.create_new(self)
        engine.run()
