from unittest import TestCase

import src.core.game_elements.game_objects.animals.tier_5 as tier_5


class TestChicken(TestCase):
    def test_instantiation(self):
        anim = tier_5.Chicken()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_5.BUY_T1_PET))


class TestCow(TestCase):
    def test_instantiation(self):
        anim = tier_5.Cow()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(tier_5.BUY))


class TestCrocodile(TestCase):
    def test_instantiation(self):
        anim = tier_5.Crocodile()
        self.assertTrue(anim.atk == 8)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(tier_5.START_BATTLE))


class TestEagle(TestCase):
    def test_instantiation(self):
        anim = tier_5.Eagle()
        self.assertTrue(anim.atk == 6)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(tier_5.ON_FAINT))


class TestGoat(TestCase):
    def test_instantiation(self):
        anim = tier_5.Goat()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(tier_5.FRIEND_BOUGHT))


class TestMonkey(TestCase):
    def test_instantiation(self):
        anim = tier_5.Monkey()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_5.END_TURN))


class TestPoodle(TestCase):
    def test_instantiation(self):
        anim = tier_5.Poodle()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_5.END_TURN))


class TestRhino(TestCase):
    def test_instantiation(self):
        anim = tier_5.Rhino()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(tier_5.KNOCK_OUT))


class TestScorpion(TestCase):
    def test_instantiation(self):
        anim = tier_5.Scorpion()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(tier_5.IS_SUMMONED))


class TestSeal(TestCase):
    def test_instantiation(self):
        anim = tier_5.Seal()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(tier_5.EAT_FOOD))


class TestShark(TestCase):
    def test_instantiation(self):
        anim = tier_5.Shark()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(tier_5.FRIEND_FAINTS))


class TestTurkey(TestCase):
    def test_instantiation(self):
        anim = tier_5.Turkey()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(tier_5.FRIEND_SUMMONED_BATTLE))
        self.assertTrue(anim.id == anim.trigger(tier_5.FRIEND_SUMMONED_SHOP))
