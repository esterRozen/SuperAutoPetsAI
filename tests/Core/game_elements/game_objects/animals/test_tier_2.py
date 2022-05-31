from unittest import TestCase

from src.core.game_elements.game_objects.animals import tier_2
from src.core import eventnames


class TestCrab(TestCase):
    def test_instantiation(self):
        anim = tier_2.Crab()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(eventnames.START_BATTLE))


class TestDodo(TestCase):
    def test_instantiation(self):
        anim = tier_2.Dodo()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(eventnames.START_BATTLE))


class TestDromedary(TestCase):
    def test_instantiation(self):
        anim = tier_2.Dromedary()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(eventnames.START_TURN))


class TestElephant(TestCase):
    def test_instantiation(self):
        anim = tier_2.Elephant()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(eventnames.BEFORE_ATTACK))


class TestFlamingo(TestCase):
    def test_instantiation(self):
        anim = tier_2.Flamingo()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(eventnames.ON_FAINT))


class TestHedgehog(TestCase):
    def test_instantiation(self):
        anim = tier_2.Hedgehog()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(eventnames.ON_FAINT))


class TestPeacock(TestCase):
    def test_instantiation(self):
        anim = tier_2.Peacock()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(eventnames.HURT))


class TestRat(TestCase):
    def test_instantiation(self):
        anim = tier_2.Rat()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(eventnames.ON_FAINT))


class TestShrimp(TestCase):
    def test_instantiation(self):
        anim = tier_2.Shrimp()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(eventnames.FRIEND_SOLD))


class TestSpider(TestCase):
    def test_instantiation(self):
        anim = tier_2.Spider()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(eventnames.ON_FAINT))


class TestSwan(TestCase):
    def test_instantiation(self):
        anim = tier_2.Swan()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(eventnames.START_TURN))


class TestTabbyCat(TestCase):
    def test_instantiation(self):
        anim = tier_2.Tabby_Cat()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(eventnames.EAT_FOOD))
