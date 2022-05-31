from unittest import TestCase

from src.core.game_elements.game_objects.animals import Fish
import src.core.game_elements.game_objects.equipment.tier_2 as tier_2
from src.core.overseer import MessageAgent


class TestCupcake(TestCase):
    def test_instantiation(self):
        obj = tier_2.Cupcake()
        self.assertTrue(obj.id == 402)


class TestMeatBone(TestCase):
    def test_query(self):
        agent = MessageAgent("base pack")
        animal = Fish()
        obj = tier_2.Meat_Bone()

        self.assertTrue(obj.id == 403)
        self.assertTrue(obj.query(animal, agent, 5, "outgoing") == 10)


class TestSleepingPill(TestCase):
    def test_initializaiton(self):
        obj = tier_2.Sleeping_Pill()
        self.assertTrue(obj.id == 404)


class TestWeak(TestCase):
    def test_instantiation(self):
        agent = MessageAgent("paid pack 1")
        animal = Fish()
        obj = tier_2.Weak()

        self.assertTrue(obj.id == 405)
        self.assertFalse(obj.rollable)
        self.assertTrue(obj.query(animal, agent, 5, "incoming") == 8)
