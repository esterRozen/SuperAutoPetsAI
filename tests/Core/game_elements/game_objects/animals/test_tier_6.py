from unittest import TestCase

from src.core.game_elements.game_objects.animals.tier_6 import *


class TestBoar(TestCase):
    def test_instantiation(self):
        anim = Boar()
        self.assertTrue(anim.atk == 10)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(BEFORE_ATTACK))


class TestCat(TestCase):
    def test_instantiation(self):
        anim = Cat()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(BUY_FOOD))


class TestDragon(TestCase):
    def test_instantiation(self):
        anim = Dragon()
        self.assertTrue(anim.atk == 6)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(BUY_T1_PET))


class TestFly(TestCase):
    def test_instantiation(self):
        anim = Fly()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(FRIEND_FAINTS))


class TestGorilla(TestCase):
    def test_instantiation(self):
        anim = Gorilla()
        self.assertTrue(anim.atk == 6)
        self.assertTrue(anim.hp == 9)
        self.assertTrue(anim.id == anim.trigger(HURT))


class TestLeopard(TestCase):
    def test_instantiation(self):
        anim = Leopard()
        self.assertTrue(anim.atk == 10)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestMammoth(TestCase):
    def test_instantiation(self):
        anim = Mammoth()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 10)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestOctopus(TestCase):
    def test_instantiation(self):
        anim = Octopus()
        self.assertTrue(anim.atk == 8)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(BEFORE_ATTACK))


class TestSauropod(TestCase):
    def test_instantiation(self):
        anim = Sauropod()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 12)
        self.assertTrue(anim.id == anim.trigger(BUY_FOOD))


class TestSnake(TestCase):
    def test_instantiation(self):
        anim = Snake()
        self.assertTrue(anim.atk == 6)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(FRIEND_AHEAD_ATTACKS))


class TestTiger(TestCase):
    def test_instantiation(self):
        anim = Tiger()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestTyrannosaurus(TestCase):
    def test_instantiation(self):
        anim = Tyrannosaurus()
        self.assertTrue(anim.atk == 9)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(END_TURN))
