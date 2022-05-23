from unittest import TestCase
from src.core.game_elements.game_objects import Items


class TestItems(TestCase):
    base_food = [
        [
            'Apple', 'Honey'
        ], [
            'Cupcake', 'MeatBone', 'SleepingPill', 'Weak'
        ], [
            'Garlic', 'SaladBowl'
        ], [
            'CannedFood', 'Pear'
        ], [
            'BestMilk', 'BetterMilk', 'Chili', 'Chocolate', 'Milk', 'Sushi'
        ], [
            'Melon', 'Mushroom', 'Pizza', 'Steak'
        ]
    ]

    def test_instantiation(self):
        food = Items()
        food = [[item.__class__.__name__ for item in tier] for tier in food.items]
        for i, tier in enumerate(food):
            for j, obj in enumerate(tier):
                self.assertTrue(obj == self.base_food[i][j], f"T{i+1}: {obj} should be {self.base_food[i][j]}")
