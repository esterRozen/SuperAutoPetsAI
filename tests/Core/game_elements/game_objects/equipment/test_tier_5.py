from unittest import TestCase

from src.core.game_elements.game_objects.animals.tier_1 import Fish
import src.core.game_elements.game_objects.equipment.tier_5 as tier_5
from src.core.overseer import MessageAgent


class TestBestMilk(TestCase):
    def test_instantiation(self):
        obj = tier_5.Best_Milk()

        self.assertTrue(obj.id == 416)
        self.assertFalse(obj.rollable)


class TestBetterMilk(TestCase):
    def test_instantiation(self):
        obj = tier_5.Better_Milk()
        self.assertTrue(obj.id == 415)
        self.assertFalse(obj.rollable)


class TestChili(TestCase):
    def test_instantiation(self):
        agent = MessageAgent("base pack")
        animal = Fish()
        obj = tier_5.Chili()

        self.assertTrue(obj.id == 410)
        self.assertTrue(obj.query(animal, agent, 5, "outgoing") == 5)


class TestChocolate(TestCase):
    def test_instantiation(self):
        obj = tier_5.Chocolate()

        self.assertTrue(obj.id == 411)


class TestMilk(TestCase):
    def test_instantiation(self):
        obj = tier_5.Milk()

        self.assertTrue(obj.id == 414)
        self.assertFalse(obj.rollable)


class TestSushi(TestCase):
    def test_instantiation(self):
        obj = tier_5.Sushi()

        self.assertTrue(obj.id == 413)
        self.assertFalse(obj.is_targeted)
