from .interface import Trait
from .attribute import *


ALL_TRAITS = {
    ID: Trait(ID,
                description="Object's unique identifier"
                ),
    LOCATION: Trait(LOCATION,
                    description="Object's location in two dimensional space"
        ),
    SPECIATION: Trait(SPECIATION,
                        description="Organism's speciation spectrum location"
        ),
    PROPAGATION_RATE: Trait(PROPAGATION_RATE,
                            description="Base number of offspring produced" \
                                            "during propagation"
        ),
    PROPAGATION_RADIUS: Trait(PROPAGATION_RADIUS,
                                description="Max distance from organism's" \
                                                "location that a mating" \
                                                " partner can be found"
        ),
    OFFSPRING_RADIUS: Trait(OFFSPRING_RADIUS,
                            description="Max distance from parent organism's" \
                                        "location that offspring can spawn"
        ),
    BORDER_RADIUS: Trait(BORDER_RADIUS,
                            description = "Max distance from a biome's" \
                                            "location an organism can lie" \
                                            "within"
        ),
    }

INIT_TRAITS = tuple(
    v for k, v in ALL_TRAITS.items() if k in (ID,
                                                LOCATION,
                                                SPECIATION,
                                                PROPAGATION_RATE,
                                                PROPAGATION_RADIUS,
                                                OFFSPRING_RADIUS,
                                                BORDER_RADIUS
                                                )
    )
