from unittest import TestCase

import src.core.game_elements.game_objects.animals.tier_4 as tier_4


class TestBison(TestCase):
    def test_instantiation(self):
        anim = tier_4.Bison()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(tier_4.END_TURN))


class TestBuffalo(TestCase):
    def test_instantiation(self):
        anim = tier_4.Buffalo()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 4)
        self.assertTrue(anim.id == anim.trigger(tier_4.FRIEND_BOUGHT))


class TestButterfly(TestCase):
    def test_instantiation(self):
        anim = tier_4.Butterfly()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(tier_4.IS_SUMMONED))


class TestCaterpillar(TestCase):
    def test_instantiation(self):
        anim = tier_4.Caterpillar()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_4.START_TURN))
        self.assertFalse(anim.id == anim.trigger(tier_4.START_BATTLE))
        anim.xp = 5
        self.assertTrue(anim.id == anim.trigger(tier_4.START_BATTLE))


class TestDeer(TestCase):
    def test_instantiation(self):
        anim = tier_4.Deer()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(tier_4.ON_FAINT))


class TestDolphin(TestCase):
    def test_instantiation(self):
        anim = tier_4.Dolphin()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(tier_4.START_BATTLE))


class TestHippo(TestCase):
    def test_instantiation(self):
        anim = tier_4.Hippo()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 7)
        self.assertTrue(anim.id == anim.trigger(tier_4.KNOCK_OUT))


class TestLlama(TestCase):
    def test_instantiation(self):
        anim = tier_4.Llama()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 6)
        self.assertTrue(anim.id == anim.trigger(tier_4.END_TURN))


class TestLobster(TestCase):
    def test_instantiation(self):
        anim = tier_4.Lobster()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(tier_4.FRIEND_SUMMONED_SHOP))
        self.assertFalse(anim.id == anim.trigger(tier_4.FRIEND_SUMMONED_BATTLE))


class TestMicrobe(TestCase):
    def test_instantiation(self):
        anim = tier_4.Microbe()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 1)
        self.assertTrue(anim.id == anim.trigger(tier_4.ON_FAINT))


class TestParrot(TestCase):
    def test_instantiation(self):
        anim = tier_4.Parrot()
        self.assertTrue(anim.atk == 4)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_4.END_TURN))


class TestPenguin(TestCase):
    def test_instantiation(self):
        anim = tier_4.Penguin()
        self.assertTrue(anim.atk == 1)
        self.assertTrue(anim.hp == 2)
        self.assertTrue(anim.id == anim.trigger(tier_4.END_TURN))


class TestRooster(TestCase):
    def test_instantiation(self):
        anim = tier_4.Rooster()
        self.assertTrue(anim.atk == 5)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(tier_4.ON_FAINT))


class TestSkunk(TestCase):
    def test_instantiation(self):
        anim = tier_4.Skunk()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(tier_4.START_BATTLE))


class TestSquirrel(TestCase):
    def test_instantiation(self):
        anim = tier_4.Squirrel()
        self.assertTrue(anim.atk == 2)
        self.assertTrue(anim.hp == 5)
        self.assertTrue(anim.id == anim.trigger(tier_4.START_TURN))


class TestWhale(TestCase):
    def test_instantiation(self):
        anim = tier_4.Whale()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 8)
        self.assertTrue(anim.id == anim.trigger(tier_4.START_BATTLE))


class TestWorm(TestCase):
    def test_instantiation(self):
        anim = tier_4.Worm()
        self.assertTrue(anim.atk == 3)
        self.assertTrue(anim.hp == 3)
        self.assertTrue(anim.id == anim.trigger(tier_4.EAT_FOOD))
