import time

from world import World
from creature import Creature, SmallPeePee

"The speed of a tick, in seconds."
tick_duration = 1

if __name__ == "__main__":
    world = World()

    owya = Creature("Owya")
    # owya.hunger = 5

    small = SmallPeePee()
    small.hunger = 10
    small.health = 3

    # Populate the world.
    world.add_creature(owya)
    world.add_creature(small)

    # Game loop.
    while True:
        start = time.time()
        world.tick()
        end = time.time()

        delta = (start + tick_duration) - end
        time.sleep(delta)
