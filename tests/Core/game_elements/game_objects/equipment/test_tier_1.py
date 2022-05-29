from unittest import TestCase

from src.core.game_elements.game_objects.equipment.tier_1 import *


class TestApple(TestCase):
    def test_instantiation(self):
        obj = Apple()
        self.assertTrue(obj.id == 400)


class TestHoney(TestCase):
    def test_instantiation(self):
        obj = Honey()
        self.assertTrue(obj.id == 401)
