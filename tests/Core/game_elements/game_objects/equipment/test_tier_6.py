from unittest import TestCase

from src.core.game_elements.game_objects.animals.tier_1 import Fish
import src.core.game_elements.game_objects.equipment.tier_6 as tier_6
from src.core.overseer import MessageAgent


class TestCoconut(TestCase):
    def test_instantiation(self):
        animal = Fish()
        obj = tier_6.Coconut()
        animal.held = obj
        agent = MessageAgent("base pack")
        agent.team[0] = animal
        agent.target = ("team", 0)

        self.assertTrue(obj.id == 417)
        self.assertTrue(obj.query(animal, agent, 40, "incoming") == 0)
        self.assertTrue(isinstance(animal.held, tier_6.Unarmed))


class TestMelon(TestCase):
    def test_instantiation(self):
        animal = Fish()
        obj = tier_6.Melon()
        animal.held = obj
        agent = MessageAgent("base pack")
        agent.team[0] = animal
        agent.target = ("team", 0)

        self.assertTrue(obj.id == 418)
        self.assertTrue(obj.query(animal, agent, 30, "incoming") == 10)
        self.assertTrue(isinstance(animal.held, tier_6.Unarmed))


class TestMushroom(TestCase):
    def test_instantiation(self):
        obj = tier_6.Mushroom()

        self.assertTrue(obj.id == 419)


class TestPizza(TestCase):
    def test_instantiation(self):
        obj = tier_6.Pizza()

        self.assertTrue(obj.id == 420)
        self.assertFalse(obj.is_targeted)


class TestSteak(TestCase):
    def test_instantiation(self):
        animal = Fish()
        obj = tier_6.Steak()
        animal.held = obj
        agent = MessageAgent("base pack")
        agent.team[0] = animal
        agent.event_raiser = ("team", 0)

        self.assertTrue(obj.id == 421)
