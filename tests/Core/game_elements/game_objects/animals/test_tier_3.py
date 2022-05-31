from unittest import TestCase

import src.core.game_elements.game_objects.animals.tier_3 as tier_3


class TestBadger(TestCase):
    def test_instantiation(self):
        anim = tier_3.Badger()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(tier_3.ON_FAINT))


class TestBlowfish(TestCase):
    def test_instantiation(self):
        anim = tier_3.Blowfish()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(tier_3.HURT))


class TestCamel(TestCase):
    def test_instantiation(self):
        anim = tier_3.Camel()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(tier_3.HURT))


class TestDog(TestCase):
    def test_instantiation(self):
        anim = tier_3.Dog()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(tier_3.FRIEND_SUMMONED_BATTLE))
        self.assertTrue(anim.id == anim.trigger(tier_3.FRIEND_SUMMONED_SHOP))


class TestGiraffe(TestCase):
    def test_instantiation(self):
        anim = tier_3.Giraffe()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(tier_3.END_TURN))


class TestHatchingChick(TestCase):
    def test_instantiation(self):
        anim = tier_3.Hatching_Chick()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(tier_3.END_TURN))
        self.assertFalse(anim.id == anim.trigger(tier_3.START_TURN))
        anim.xp = 5
        self.assertTrue(anim.id == anim.trigger(tier_3.START_TURN))


class TestKangaroo(TestCase):
    def test_instantiation(self):
        anim = tier_3.Kangaroo()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_3.FRIEND_AHEAD_ATTACKS))


class TestOx(TestCase):
    def test_instantiation(self):
        anim = tier_3.Ox()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(tier_3.FRIEND_AHEAD_FAINTS))


class TestPuppy(TestCase):
    def test_instantiation(self):
        anim = tier_3.Puppy()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(tier_3.END_TURN))


class TestRabbit(TestCase):
    def test_instantiation(self):
        anim = tier_3.Rabbit()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_3.EAT_FOOD))
        self.assertTrue(anim.id == anim.trigger(tier_3.FRIEND_EATS_FOOD))


class TestSheep(TestCase):
    def test_instantiation(self):
        anim = tier_3.Sheep()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_3.ON_FAINT))


class TestSnail(TestCase):
    def test_instantiation(self):
        anim = tier_3.Snail()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_3.BUY))


class TestTropicalFish(TestCase):
    def test_instantiation(self):
        anim = tier_3.Tropical_Fish()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(tier_3.END_TURN))


class TestTurtle(TestCase):
    def test_instantiation(self):
        anim = tier_3.Turtle()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_3.ON_FAINT))
