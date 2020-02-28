from __future__ import annotations

from typing import List, NewType
from logging import INFO

import util


Creature = NewType("Creature", object)


class World:
    """
    This is the world, as we know it. That is to say, a one-dimensional plane
    of existence, stretching as far as the eye can see.

    TODO: Implement the concept of space.
    TODO: Implement creature movement.
    TODO: Draw the world in the terminal (stdout) on each tick.
    TODO: Log to a file, instead of to stderr.
    TODO: Implement the concept of food, and random food generation.
    TODO: Implement creature reproduction.
    """

    __logger = util.create_logger("World")
    __creatures: List[Creature]

    def __init__(self):
        self.__creatures = list()

    def tick(self):
        if not self.__creatures:
            self.__logger.log(INFO, "All creatures are dead.")
        else:
            for creature in self.creatures():
                creature.tick(self)

    def creatures(self) -> List[Creature]:
        return self.__creatures

    def add_creature(self, creature: Creature):
        self.__creatures.append(creature)
        self.__logger.log(INFO, f"Added {type(creature).__name__} {creature.name}.")

    def kill_creature(self, creature: Creature):
        self.__creatures.remove(creature)
        self.__logger.log(INFO, f"{creature.name} has died.")
