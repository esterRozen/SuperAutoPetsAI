import sys, inspect
from Core.Animals.Base import Base
from Core.Animals.Paid1 import Paid1

# outputs a random animal given a range of tiers
class Spawner:
    def __init__(self, mode):
        self.animals = []
        if mode == "base":
            self.animals = Base().animals
        elif mode == "paid_1":
            self.animals = Paid1().animals
            pass
    pass

if __name__ == "__main__":
    spawner = Spawner("base")
