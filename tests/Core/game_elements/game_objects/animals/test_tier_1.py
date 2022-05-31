from unittest import TestCase

import src.core.game_elements.game_objects.animals.tier_1 as tier_1


class TestAnt(TestCase):
    def test_instantiation(self):
        anim = tier_1.Ant()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(tier_1.ON_FAINT))


class TestBeaver(TestCase):
    def test_instantiation(self):
        anim = tier_1.Beaver()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_1.SELL))


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
        self.assertTrue(anim.id == anim.trigger(tier_1.EAT_FOOD))


class TestBluebird(TestCase):
    def test_instantiation(self):
        anim = tier_1.Bluebird()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(tier_1.END_TURN))


class TestCricket(TestCase):
    def test_instantiation(self):
        anim = tier_1.Cricket()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_1.ON_FAINT))


class TestDuck(TestCase):
    def test_instantiation(self):
        anim = tier_1.Duck()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(tier_1.SELL))


class TestFish(TestCase):
    def test_instantiation(self):
        anim = tier_1.Fish()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_1.ON_LEVEL))


class TestHorse(TestCase):
    def test_instantiation(self):
        anim = tier_1.Horse()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(tier_1.FRIEND_SUMMONED_BATTLE))


class TestLadybug(TestCase):
    def test_instantiation(self):
        anim = tier_1.Ladybug()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(tier_1.FRIEND_EATS_FOOD))


class TestMosquito(TestCase):
    def test_instantiation(self):
        anim = tier_1.Mosquito()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_1.START_BATTLE))


class TestOtter(TestCase):
    def test_instantiation(self):
        anim = tier_1.Otter()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_1.BUY))
