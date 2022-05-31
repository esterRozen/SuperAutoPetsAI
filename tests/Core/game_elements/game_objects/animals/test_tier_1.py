from unittest import TestCase

from src.core.game_elements.game_objects.animals import tier_1
from src.core import eventnames


class TestAnt(TestCase):
    def test_instantiation(self):
        anim = tier_1.Ant()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(eventnames.ON_FAINT))


class TestBeaver(TestCase):
    def test_instantiation(self):
        anim = tier_1.Beaver()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(eventnames.SELL))


class TestBee(TestCase):
    def test_instantiation(self):
        anim = tier_1.Bee()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)


class TestBeetle(TestCase):
    def test_instantiation(self):
        anim = tier_1.Beetle()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(eventnames.EAT_FOOD))


class TestBluebird(TestCase):
    def test_instantiation(self):
        anim = tier_1.Bluebird()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(eventnames.END_TURN))


class TestCricket(TestCase):
    def test_instantiation(self):
        anim = tier_1.Cricket()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(eventnames.ON_FAINT))


class TestDuck(TestCase):
    def test_instantiation(self):
        anim = tier_1.Duck()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(eventnames.SELL))


class TestFish(TestCase):
    def test_instantiation(self):
        anim = tier_1.Fish()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(eventnames.ON_LEVEL))


class TestHorse(TestCase):
    def test_instantiation(self):
        anim = tier_1.Horse()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(eventnames.FRIEND_SUMMONED_BATTLE))


class TestLadybug(TestCase):
    def test_instantiation(self):
        anim = tier_1.Ladybug()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(eventnames.FRIEND_EATS_FOOD))


class TestMosquito(TestCase):
    def test_instantiation(self):
        anim = tier_1.Mosquito()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(eventnames.START_BATTLE))


class TestOtter(TestCase):
    def test_instantiation(self):
        anim = tier_1.Otter()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(eventnames.BUY))
