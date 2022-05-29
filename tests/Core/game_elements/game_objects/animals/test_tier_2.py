from unittest import TestCase

from src.core.game_elements.game_objects.animals.tier_2 import *


class TestCrab(TestCase):
    def test_instantiation(self):
        anim = Crab()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestDodo(TestCase):
    def test_instantiation(self):
        anim = Dodo()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestDromedary(TestCase):
    def test_instantiation(self):
        anim = Dromedary()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(START_TURN))


class TestElephant(TestCase):
    def test_instantiation(self):
        anim = Elephant()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(BEFORE_ATTACK))


class TestFlamingo(TestCase):
    def test_instantiation(self):
        anim = Flamingo()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestHedgehog(TestCase):
    def test_instantiation(self):
        anim = Hedgehog()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestPeacock(TestCase):
    def test_instantiation(self):
        anim = Peacock()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(HURT))


class TestRat(TestCase):
    def test_instantiation(self):
        anim = Rat()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestShrimp(TestCase):
    def test_instantiation(self):
        anim = Shrimp()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(FRIEND_SOLD))


class TestSpider(TestCase):
    def test_instantiation(self):
        anim = Spider()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestSwan(TestCase):
    def test_instantiation(self):
        anim = Swan()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(START_TURN))


class TestTabbyCat(TestCase):
    def test_instantiation(self):
        anim = Tabby_Cat()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(EAT_FOOD))
