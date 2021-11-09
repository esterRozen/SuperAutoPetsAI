from .Base import Base
from .Paid1 import Paid1
from .Food import Items
import random


# outputs a random animal given a range of tiers
class Spawner:
    def __init__(self, mode):
        self._population = []
        if mode == "base":
            self._population = Base().animals
        elif mode == "paid_1":
            self._population = Paid1().animals
        elif mode == "food":
            self._population = Items().items

    def spawn(self, max_tier):
        return type(self.spawn_n(1, max_tier)[0])()

    def spawn_n(self, n, max_tier):
        max_idx = min(max_tier, 6)
        max_idx = max(max_idx, 1)

        subpopulation = sum(self._population[:max_idx], [])
        sample = random.choices(subpopulation, k=n)
        return [type(instance)() for instance in sample]

    def spawn_tier(self, tier):
        idx = tier - 1
        idx = max(idx, 0)
        idx = min(idx, 5)

        subpopulation = self._population[idx]
        return type(random.choice(subpopulation))()


if __name__ == "__main__":
    spawner = Spawner("base")

    a = spawner.spawn(2)
    b = spawner.spawn(3)
    c = spawner.spawn_n(3,2)
    d = spawner.spawn_tier(4)
    print("end")
