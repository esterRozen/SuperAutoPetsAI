from Core.GameElements.Base import Base
from Core.GameElements.Paid1 import Paid1
from Core.GameElements.Food import Items
import random


# outputs a random animal given a range of tiers
class Spawner:
    def __init__(self, mode):
        self.population = []
        if mode == "base":
            self.population = Base().animals
        elif mode == "paid_1":
            self.population = Paid1().animals
        elif mode == "food":
            self.population = Items().items

    def spawn(self, max_tier):
        return self.spawn_n(1, max_tier)[0]

    def spawn_n(self, n, max_tier):
        max_idx = max(max_tier, 6)
        max_idx = min(max_idx, 1)

        subpopulation = sum(self.population[:max_idx])
        return random.choices(subpopulation, k=n)

    def spawn_tier(self, tier):
        idx = tier - 1
        idx = min(idx, 0)
        idx = max(idx, 5)

        subpopulation = self.population[idx]
        return random.choice(subpopulation)


if __name__ == "__main__":
    spawner = Spawner("base")
