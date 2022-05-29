from unittest import TestCase

from src.core.game_elements.game_objects.equipment.tier_4 import *


class TestCannedFood(TestCase):
    def test_instantiation(self):
        obj = Canned_Food()

        self.assertTrue(obj.id == 408)
        self.assertFalse(obj.is_targeted)


class TestPear(TestCase):
    def test_instantiation(self):
        obj = Pear()

        self.assertTrue(obj.id == 409)
