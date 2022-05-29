from unittest import TestCase

from src.core.game_elements.game_objects.animals.tier_5 import *


class TestChicken(TestCase):
    def test_instantiation(self):
        anim = Chicken()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(BUY_T1_PET))


class TestCow(TestCase):
    def test_instantiation(self):
        anim = Cow()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(BUY))


class TestCrocodile(TestCase):
    def test_instantiation(self):
        anim = Crocodile()
        self.assertTrue(anim.atk == 8)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestEagle(TestCase):
    def test_instantiation(self):
        anim = Eagle()
        self.assertTrue(anim.atk == 6)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestGoat(TestCase):
    def test_instantiation(self):
        anim = Goat()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(FRIEND_BOUGHT))


class TestMonkey(TestCase):
    def test_instantiation(self):
        anim = Monkey()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestPoodle(TestCase):
    def test_instantiation(self):
        anim = Poodle()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestRhino(TestCase):
    def test_instantiation(self):
        anim = Rhino()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(KNOCK_OUT))


class TestScorpion(TestCase):
    def test_instantiation(self):
        anim = Scorpion()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(IS_SUMMONED))


class TestSeal(TestCase):
    def test_instantiation(self):
        anim = Seal()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(EAT_FOOD))


class TestShark(TestCase):
    def test_instantiation(self):
        anim = Shark()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(FRIEND_FAINTS))


class TestTurkey(TestCase):
    def test_instantiation(self):
        anim = Turkey()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(FRIEND_SUMMONED_BATTLE))
        self.assertTrue(anim.id == anim.trigger(FRIEND_SUMMONED_SHOP))
