from unittest import TestCase

import src.core.game_elements.game_objects.equipment.tier_4 as tier_4


class TestCannedFood(TestCase):
    def test_instantiation(self):
        obj = tier_4.Canned_Food()

        self.assertTrue(obj.id == 408)
        self.assertFalse(obj.is_targeted)


class TestPear(TestCase):
    def test_instantiation(self):
        obj = tier_4.Pear()

        self.assertTrue(obj.id == 409)
