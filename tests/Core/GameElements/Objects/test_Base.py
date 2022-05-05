from unittest import TestCase
from src.Core.GameElements.Objects import Base


class TestBase(TestCase):
    base_animals = [
        [
            'Ant', 'Beaver', 'Bee', 'Cricket', 'Duck', 'Fish',
            'Horse', 'Mosquito', 'Otter', 'Pig', 'Sloth', 'ZombieCricket',
        ], [
            'Crab', 'DirtyRat', 'Dodo', 'Elephant', 'Flamingo', 'Hedgehog',
            'Peacock', 'Rat', 'Shrimp', 'Spider', 'Swan'
        ], [
            'Badger', 'Blowfish', 'Camel', 'Dog', 'Giraffe', 'Kangaroo',
            'Ox', 'Rabbit', 'Ram', 'Sheep', 'Snail', 'Turtle'
        ], [
            'Bison', 'Bus', 'Chick', 'Deer', 'Dolphin', 'Hippo', 'Parrot',
            'Penguin', 'Rooster', 'Skunk', 'Squirrel', 'Whale', 'Worm'
        ], [
            'Cow', 'Crocodile', 'Monkey', 'Rhino', 'Scorpion', 'Seal',
            'Shark', 'Turkey'
        ], [
            'Boar', 'Cat', 'Dragon', 'Fly', 'FlyFriend', 'Gorilla',
            'Leopard', 'Mammoth', 'Snake', 'Tiger'
        ]
    ]

    def test_instantiation(self):
        base_pack = Base()
        self.assertTrue(len(base_pack.animals) == 6, "Should be 6 tiers in list")
        animals = [[animal.__class__.__name__ for animal in tier] for tier in base_pack.animals]
        for i, tier in enumerate(animals):
            for j, animal in enumerate(tier):
                self.assertTrue(animal == self.base_animals[i][j], f"T{i+1}: {animal} should be {self.base_animals[i][j]}")
