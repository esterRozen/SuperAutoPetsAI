from unittest import TestCase
from typing import List
from src.core.game_elements.abstract_elements import Spawner, Animal, Equipment


class TestSpawner(TestCase):
    def test_base(self):
        spawner = Spawner("base")
        for _ in range(10):
            animal: type(Animal) = spawner.spawn_tier(3)
            self.assertTrue(animal.tier == 3, "wrong tier")

    def test_equipment(self):
        spawner = Spawner("food")
        for _ in range(10):
            item: type(Equipment) = spawner.spawn_tier(2)
            self.assertTrue(item.tier == 2, "wrong tier")

    def test_paid1(self):
        spawner = Spawner("paid_1")
        for _ in range(10):
            animal: type(Animal) = spawner.spawn_tier(4)
            self.assertTrue(animal.tier == 4, "wrong tier")

    def test_spawn(self):
        spawner = Spawner("base")
        for _ in range(20):
            animal: type(Animal) = spawner.spawn(4)
            self.assertTrue(animal.tier <= 4, "wrong tier")
            self.assertIsInstance(animal, Animal, "not an animal")
            self.assertTrue(animal.cost == 3, "wrong cost")

    def test_spawn_n(self):
        spawner = Spawner("paid_1")
        for _ in range(10):
            animals: List[type(Animal)] = spawner.spawn_n(5, 3)
            self.assertTrue(len(animals) == 5, "wrong number of animals")
            for animal in animals:
                self.assertTrue(animal.tier <= 3, "wrong tier")

    def test_spawn_tier(self):
        spawner = Spawner("base")
        for _ in range(20):
            animal: type(Animal) = spawner.spawn_tier(4)
            self.assertTrue(animal.tier == 4, "wrong tier")
        for i in range(0, 8):
            animal: type(Animal) = spawner.spawn_tier(i)
            self.assertTrue(max(min(animal.tier, 6), 1) == max(min(i, 6), 1), "wrong tier")