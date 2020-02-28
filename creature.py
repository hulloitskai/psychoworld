from typing import List


class Creature:
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

    def __str__(self) -> str:
        return f"Creature(name: {self.name})"

    def tick(self, world: "World"):
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
            creatures: List["Creature"] = world.creatures
            creatures.remove(self)

    def hungry(self):
        print(f"{self.name} is hungry. (hunger = {self.hunger})")

    def dying(self):
        print(f"{self.name} is dying. (health = {self.health})")

    def last_words(self):
        print(f"{self.name} is dead.")


class SmallPeePee(Creature):
    def __init__(self):
        super(SmallPeePee, self).__init__("u/small_peepee")

    def last_words(self):
        print(f"{self.name} I wish I had GF...")
        super(SmallPeePee, self).last_words()
