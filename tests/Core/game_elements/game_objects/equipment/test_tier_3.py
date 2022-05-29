from unittest import TestCase

from src.core.game_elements.game_objects.animals import Fish
from src.core.game_elements.game_objects.equipment.tier_3 import *
from src.core.overseer import MessageAgent


class TestGarlic(TestCase):
    def test_instantiation(self):
        agent = MessageAgent("base pack")
        obj = Garlic()
        animal = Fish()

        self.assertTrue(obj.id == 406)
        self.assertTrue(obj.query(animal, agent, 4, "incoming") == 2)
        self.assertTrue(obj.query(animal, agent, 2, "incoming") == 1)


class TestSaladBowl(TestCase):
    def test_instantiation(self):
        obj = Salad_Bowl()

        self.assertTrue(obj.id == 407)
        self.assertFalse(obj.is_targeted)
