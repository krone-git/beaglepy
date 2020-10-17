from ..trait.attribute import BORDER_RADIUS
from .interface import Biome
from .attribute import WORLD
from sys import maxsize


INIT_BIOMES = (
    Biome(
        WORLD,
        description="A catch all biome",
        **{BORDER_RADIUS: maxsize}
        ),
    )
