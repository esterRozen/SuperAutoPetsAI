from unittest import TestCase

import src.core.game_elements.game_objects.animals.tier_6 as tier_6


class TestBoar(TestCase):
    def test_instantiation(self):
        anim = tier_6.Boar()
        self.assertTrue(anim.atk == 10)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(tier_6.BEFORE_ATTACK))


class TestCat(TestCase):
    def test_instantiation(self):
        anim = tier_6.Cat()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(tier_6.BUY_FOOD))


class TestDragon(TestCase):
    def test_instantiation(self):
        anim = tier_6.Dragon()
        self.assertTrue(anim.atk == 6)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(tier_6.BUY_T1_PET))


class TestFly(TestCase):
    def test_instantiation(self):
        anim = tier_6.Fly()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(tier_6.FRIEND_FAINTS))


class TestGorilla(TestCase):
    def test_instantiation(self):
        anim = tier_6.Gorilla()
        self.assertTrue(anim.atk == 6)
        self.assertTrue(anim.hp == 9)
        self.assertTrue(anim.id == anim.trigger(tier_6.HURT))


class TestLeopard(TestCase):
    def test_instantiation(self):
        anim = tier_6.Leopard()
        self.assertTrue(anim.atk == 10)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(tier_6.START_BATTLE))


class TestMammoth(TestCase):
    def test_instantiation(self):
        anim = tier_6.Mammoth()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 10)
        self.assertTrue(anim.id == anim.trigger(tier_6.ON_FAINT))


class TestOctopus(TestCase):
    def test_instantiation(self):
        anim = tier_6.Octopus()
        self.assertTrue(anim.atk == 8)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(tier_6.BEFORE_ATTACK))


class TestSauropod(TestCase):
    def test_instantiation(self):
        anim = tier_6.Sauropod()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 12)
        self.assertTrue(anim.id == anim.trigger(tier_6.BUY_FOOD))


class TestSnake(TestCase):
    def test_instantiation(self):
        anim = tier_6.Snake()
        self.assertTrue(anim.atk == 6)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(tier_6.FRIEND_AHEAD_ATTACKS))


class TestTiger(TestCase):
    def test_instantiation(self):
        anim = tier_6.Tiger()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(tier_6.START_BATTLE))


class TestTyrannosaurus(TestCase):
    def test_instantiation(self):
        anim = tier_6.Tyrannosaurus()
        self.assertTrue(anim.atk == 9)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(tier_6.END_TURN))
