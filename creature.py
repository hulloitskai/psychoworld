from __future__ import annotations

from logging import Logger, INFO
from world import World

import util


class Creature:
    logger: Logger

    "The name of the creature."
    name: str

    """
    The amount of health the creature has. Starts at 100.
    The creature dies when this reaches 0.
    """
    health = 20

    """
    Hunger starts at 0, and goes up by one each tick. When hunger reaches 10,
    the creature starts losing health.
    """
    hunger = 0

    def __init__(self, name: str):
        self.name = name
        self.logger = util.create_logger(f"Creature({name})")

    def __str__(self) -> str:
        return f"Creature(name: {self.name})"

    def tick(self, world: World):
        dying = False

        # Respond to hunger.
        if self.hunger < 10:
            self.hunger += 1
        else:
            dying = True

        if self.hunger > 5:
            self.hungry()

        if dying:
            self.health -= 1
            self.dying()

        # Respond to health.
        if self.health == 0:
            self.last_words()
            world.kill_creature(self)

    def say(self, msg: str):
        self.logger.log(INFO, msg)

    def hungry(self):
        self.say(f"I'm hungry. (hunger = {self.hunger})")

    def dying(self):
        self.say(f"I'm dying! (health = {self.health})")

    def last_words(self):
        self.say(f"Good night, sweet prince.")


class SmallPeePee(Creature):
    def __init__(self):
        super(SmallPeePee, self).__init__("u/small_peepee")

    def last_words(self):
        self.say(f"{self.name} I wish I had GF...")
