from unittest import TestCase
from src.core.game_elements.game_objects import Paid1


class TestPaid1(TestCase):
    paid1_animals = [
        [
            'Ant', 'Beaver', 'Bee', 'Beetle', 'Bluebird', 'Cricket', 'Fish',
            'Ladybug', 'Mosquito', 'Pig', 'Sloth', 'ZombieCricket',
        ], [
            'Bat', 'DirtyRat', 'Dromedary', 'Flamingo', 'Hedgehog', 'Peacock',
            'Rat', 'Shrimp', 'Spider', 'Swan', 'TabbyCat'
        ], [
            'Blowfish', 'Butterfly', 'Caterpillar', 'Dog', 'HatchingChick',
            'Owl', 'Puppy', 'Rabbit', 'Ram', 'Sheep', 'Snail', 'TropicalFish',
            'Turtle'
        ], [
            'Bison', 'Buffalo', 'Bus', 'Chick', 'Deer', 'Dolphin', 'Llama',
            'Lobster', 'Microbe', 'Rooster', 'Skunk', 'Squirrel', 'Worm'
        ], [
            'Chicken', 'Cow', 'Eagle', 'Goat', 'Poodle', 'Rhino', 'Scorpion',
            'Seal', 'Shark', 'Turkey'
        ], [
            'Boar', 'Dragon', 'Gorilla', 'Leopard', 'Mammoth', 'Octopus',
            'Sauropod', 'Tiger', 'Tyrannosaurus'
        ]
    ]

    def test_instantiation(self):
        paid = Paid1()
        self.assertTrue(len(paid.animals) == 6, "Should be 6 tiers in list")
        animals = [[animal.__class__.__name__ for animal in tier] for tier in paid.animals]
        for i, tier in enumerate(animals):
            for j, animal in enumerate(tier):
                self.assertTrue(animal == self.paid1_animals[i][j], f"T{i+1}: {animal} should be {self.paid1_animals[i][j]}")
