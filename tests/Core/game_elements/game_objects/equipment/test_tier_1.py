from unittest import TestCase

import src.core.game_elements.game_objects.equipment.tier_1 as tier_1


class TestApple(TestCase):
    def test_instantiation(self):
        obj = tier_1.Apple()
        self.assertTrue(obj.id == 400)


class TestHoney(TestCase):
    def test_instantiation(self):
        obj = tier_1.Honey()
        self.assertTrue(obj.id == 401)
