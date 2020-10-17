# example_simulation.py

from beaglepy import Simulation, Trait, Event, Biome, Organism
from beaglepy.trait import RandRangeInheritance, NormalDistMutation

from .example_trait import ...
from .example_biome import ...
from .example_event import event2_effect, ExampleEvent1, ExampleEvent2


# Instantiate Simulation instance
sim = Simulation()


# Set simulation environment variable from Simulation.environment property
sim.environment.generations = 1200

# Setting simulation environment variables in a 'with' statement
with sim.environment as env:
    # using property setting
    env.initial_population = 150

    # using 'set' method with lowercase name
    env.set("speciation_threshold", 10)
    # using 'set' method with uppercase name
    env.set("INITIAL_SPECIES_COUNT", 1)

    # using '__setitem__' method to set variable
    env["propagation_origin"] = (200, 300)
    # using '__setitem__' with constant to set variable
    env[env.PROPAGATION_RADIUS] = 100


# Instantiating Trait instance ahead of adding it to Simulation.traits
# collection
trait1 = Trait(
    "Trait1",                             # trait's name
    (Biome,),                             # tuple of classes trait affects
    description="First example trait.",   # trait's description
    initial=10                            # trait's default intial value
    )
sim.traits.add(trait1) # add Trait instance to Simulation.traits collection

# using Simulation.traits.add_new to instantiate Trait instance and add
# it to Simulation.traits collection in a single method
trait2 = sim.traits.add_new(
    "Trait2",
    (Organism, Biome),
    description="Second example trait.",
    # keyword arguments for traits that affect Organisms;
    # does not apply to traits that only affect Biomes
    inheritance=RandRangeInheritance,   # trait's inheritance handler
    mutation=NormalDistMutation         # trait's mutation handler
    )


# Working with Simulation.biomes collection using 'with' statement
with sim.biomes as bio:
    # using property getting and setting with lowercase
    bio.world.border_radius = 1000

    # using 'get' method with uppercase
    bio.get("WORLD").climate = 100

    # using 'set' method with lowercase
    bio.set("world", "climate_threshold", 10)

    # using 'set' method with constant values
    world = bio.get(bio.WORLD)
    world.set(world.CLIMATE, 100)

# Instantiating Biome instance ahead of adding to Simulation.biomes collection
biome1 = Biome(
    "Biome1",                             # biome's name
    description="First example biome.",   # biome's description
    location=[300, 400],                  # biome's initial location
    border_radius=100                     # biome's border radius
    )
sim.biomes.add(biome1) # add Biome instance to Simulation.biomes collection

# using Simulation.biomes.add_new to instantiate Biome instance and add
# it to Simulation.biomes collection in a single method
biome2 = sim.biomes.add_new(
  "Biome2",
  description="Second example biome."
  )

# using property getting and setting to get trait values for biome and
# set one of it's values
biome1.trait1.initial = 30
# using 'get' and 'set' methods
biome1.get("trait2").set("initial", 10)
# using 'set' method with alternating case
biome2.set("tRaIt2", "initial", 20)


# Instantiating Event instance ahead of adding to Simulation.events collection
event1 = Event(
    "Event1",                               # event's name
    description="First example trait.",     # event's description
    # generation event starts to take effect
    start=0,
    # number of generations event's effect remains active;
    # using Simulation.environment '__getitem__' method
    duration=sim.environment["generations"],
    # event's effect handler;
    # using Simulation.biomes '__getitem__' method with alternating case
    effect=(lambda state: state.biomes["bIoMe1"].climate += 1)
    )
sim.events.add(event1) # add Event instance to Simulation.events collection

# using Simulation.events.add_new to instantiate Event instance and add
# it to Simulation.events collection in a single method
event2 = sim.events.add_new(
    "Trait2",
    description="Second example trait."
    start=sim.environment.generations / 2
    duration=sim.environment.get("generations"),  # using
    effect=event2_effect
    )

# add instance of user defined Event classes
event3 = sim.events.add(ExampleEvent1())
event4 = sim.events.add(ExampleEvent2())

# Run simulation
sim.start()

# export simulation results and history to file
sim.export("simulation_results.csv")
