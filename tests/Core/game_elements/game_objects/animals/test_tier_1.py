from unittest import TestCase

from src.core.game_elements.game_objects.animals.tier_1 import *


class TestAnt(TestCase):
    def test_instantiation(self):
        anim = Ant()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestBeaver(TestCase):
    def test_instantiation(self):
        anim = Beaver()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(SELL))


class TestBee(TestCase):
    def test_instantiation(self):
        anim = Bee()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)


class TestBeetle(TestCase):
    def test_instantiation(self):
        anim = Beetle()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(EAT_FOOD))


class TestBluebird(TestCase):
    def test_instantiation(self):
        anim = Bluebird()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestCricket(TestCase):
    def test_instantiation(self):
        anim = Cricket()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestDuck(TestCase):
    def test_instantiation(self):
        anim = Duck()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(SELL))


class TestFish(TestCase):
    def test_instantiation(self):
        anim = Fish()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(ON_LEVEL))


class TestHorse(TestCase):
    def test_instantiation(self):
        anim = Horse()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(FRIEND_SUMMONED_BATTLE))


class TestLadybug(TestCase):
    def test_instantiation(self):
        anim = Ladybug()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(FRIEND_EATS_FOOD))


class TestMosquito(TestCase):
    def test_instantiation(self):
        anim = Mosquito()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestOtter(TestCase):
    def test_instantiation(self):
        anim = Otter()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(BUY))
