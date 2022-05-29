from unittest import TestCase

from src.core.game_elements.game_objects.animals.tier_3 import *


class TestBadger(TestCase):
    def test_instantiation(self):
        anim = Badger()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestBlowfish(TestCase):
    def test_instantiation(self):
        anim = Blowfish()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(HURT))


class TestCamel(TestCase):
    def test_instantiation(self):
        anim = Camel()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(HURT))


class TestDog(TestCase):
    def test_instantiation(self):
        anim = Dog()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(FRIEND_SUMMONED_BATTLE))
        self.assertTrue(anim.id == anim.trigger(FRIEND_SUMMONED_SHOP))


class TestGiraffe(TestCase):
    def test_instantiation(self):
        anim = Giraffe()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestHatchingChick(TestCase):
    def test_instantiation(self):
        anim = Hatching_Chick()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(END_TURN))
        self.assertFalse(anim.id == anim.trigger(START_TURN))
        anim.xp = 5
        self.assertTrue(anim.id == anim.trigger(START_TURN))


class TestKangaroo(TestCase):
    def test_instantiation(self):
        anim = Kangaroo()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(FRIEND_AHEAD_ATTACKS))


class TestOx(TestCase):
    def test_instantiation(self):
        anim = Ox()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(FRIEND_AHEAD_FAINTS))


class TestPuppy(TestCase):
    def test_instantiation(self):
        anim = Puppy()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestRabbit(TestCase):
    def test_instantiation(self):
        anim = Rabbit()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(EAT_FOOD))
        self.assertTrue(anim.id == anim.trigger(FRIEND_EATS_FOOD))


class TestSheep(TestCase):
    def test_instantiation(self):
        anim = Sheep()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestSnail(TestCase):
    def test_instantiation(self):
        anim = Snail()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(BUY))


class TestTropicalFish(TestCase):
    def test_instantiation(self):
        anim = Tropical_Fish()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestTurtle(TestCase):
    def test_instantiation(self):
        anim = Turtle()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))
