from unittest import TestCase

from src.core.game_elements.game_objects.animals.tier_4 import *


class TestBison(TestCase):
    def test_instantiation(self):
        anim = Bison()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestBuffalo(TestCase):
    def test_instantiation(self):
        anim = Buffalo()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(FRIEND_BOUGHT))


class TestButterfly(TestCase):
    def test_instantiation(self):
        anim = Butterfly()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(IS_SUMMONED))


class TestCaterpillar(TestCase):
    def test_instantiation(self):
        anim = Caterpillar()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(START_TURN))
        self.assertFalse(anim.id == anim.trigger(START_BATTLE))
        anim.xp = 5
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestDeer(TestCase):
    def test_instantiation(self):
        anim = Deer()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestDolphin(TestCase):
    def test_instantiation(self):
        anim = Dolphin()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestHippo(TestCase):
    def test_instantiation(self):
        anim = Hippo()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 7)
        self.assertTrue(anim.id == anim.trigger(KNOCK_OUT))


class TestLlama(TestCase):
    def test_instantiation(self):
        anim = Llama()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestLobster(TestCase):
    def test_instantiation(self):
        anim = Lobster()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(FRIEND_SUMMONED_SHOP))
        self.assertFalse(anim.id == anim.trigger(FRIEND_SUMMONED_BATTLE))


class TestMicrobe(TestCase):
    def test_instantiation(self):
        anim = Microbe()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestParrot(TestCase):
    def test_instantiation(self):
        anim = Parrot()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestPenguin(TestCase):
    def test_instantiation(self):
        anim = Penguin()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(END_TURN))


class TestRooster(TestCase):
    def test_instantiation(self):
        anim = Rooster()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(ON_FAINT))


class TestSkunk(TestCase):
    def test_instantiation(self):
        anim = Skunk()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestSquirrel(TestCase):
    def test_instantiation(self):
        anim = Squirrel()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(START_TURN))


class TestWhale(TestCase):
    def test_instantiation(self):
        anim = Whale()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(START_BATTLE))


class TestWorm(TestCase):
    def test_instantiation(self):
        anim = Worm()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(EAT_FOOD))
