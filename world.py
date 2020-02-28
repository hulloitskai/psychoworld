from typing import List
from creature import Creature


class World:
    creatures: List[Creature]

    def __init__(self):
        self.creatures = list()

    def tick(self):
        for creature in self.creatures:
            creature.tick(self)
