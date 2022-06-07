from unittest import TestCase

from src.core.game_elements.abstract_elements import Unarmed
from src.core.game_elements.game_objects.animals import tier_1, tier_2, tier_5
from src.core.game_elements.game_objects.equipment import Milk, Better_Milk, Best_Milk
from src.core.overseer.handlers.object_effects.tier5 import Tier5
from src.core.game_systems import BattleSystem, ShopSystem
from src.core.overseer import MessageAgent


class TestTier5(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        BattleSystem(self.agent)
        ShopSystem(self.agent)

    def test__chicken(self):
        self.agent.summon(tier_5.Chicken(), ("team", 0))
        Tier5.chicken(self.agent, ("team", 0), ("team", 4))

        shop_anim = self.agent.shop[0].item
        orig_anim = shop_anim.__class__()

        self.assertTrue(shop_anim.atk == orig_anim.atk + 1)
        self.assertTrue(shop_anim.battle_atk == orig_anim.battle_atk + 1)
        self.assertTrue(shop_anim.hp == orig_anim.hp + 1)
        self.assertTrue(shop_anim.battle_hp == orig_anim.battle_hp + 1)

        self.agent.team[0].xp = 2
        Tier5.chicken(self.agent, ("team", 0), ("team", 4))

        shop_anim = self.agent.shop[0].item
        orig_anim = shop_anim.__class__()

        self.assertTrue(shop_anim.atk == orig_anim.atk + 3)
        self.assertTrue(shop_anim.battle_atk == orig_anim.battle_atk + 3)
        self.assertTrue(shop_anim.hp == orig_anim.hp + 3)
        self.assertTrue(shop_anim.battle_hp == orig_anim.battle_hp + 3)

        self.agent.team[0].xp = 5
        Tier5.chicken(self.agent, ("team", 0), ("team", 4))

        shop_anim = self.agent.shop[0].item
        orig_anim = shop_anim.__class__()

        self.assertTrue(shop_anim.atk == orig_anim.atk + 6)
        self.assertTrue(shop_anim.battle_atk == orig_anim.battle_atk + 6)
        self.assertTrue(shop_anim.hp == orig_anim.hp + 6)
        self.assertTrue(shop_anim.battle_hp == orig_anim.battle_hp + 6)

    def test__cow(self):
        self.agent.summon(tier_5.Cow(), ("team", 0))
        Tier5.cow(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(isinstance(self.agent.shop[5].item, Milk))
        self.assertTrue(isinstance(self.agent.shop[6].item, Unarmed))

        self.agent.team[0].xp = 2
        Tier5.cow(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(isinstance(self.agent.shop[5].item, Better_Milk))
        self.assertTrue(isinstance(self.agent.shop[6].item, Unarmed))

        self.agent.team[0].xp = 5
        Tier5.cow(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(isinstance(self.agent.shop[5].item, Best_Milk))
        self.assertTrue(isinstance(self.agent.shop[6].item, Unarmed))

    def test__crocodile(self):
        # TODO
        self.fail()

    def test__eagle(self):
        # TODO
        self.fail()

    def test__goat(self):
        # TODO
        self.fail()

    def test__microbe(self):
        # TODO
        self.fail()

    def test__parrot(self):
        # TODO
        self.fail()

    def test__poodle(self):
        self.agent.summon(tier_1.Fish(), ("team", 4))
        self.agent.summon(tier_2.Shrimp(), ("team", 3))
        self.agent.summon(tier_1.Fish(), ("team", 2))
        self.agent.summon(tier_5.Poodle(), ("team", 1))
        self.agent.summon(tier_5.Cow(), ("team", 0))
        self.fail()

    def test__rhino(self):
        # TODO
        self.fail()

    def test__scorpion(self):
        # TODO
        self.fail()

    def test__seal(self):
        # TODO
        self.fail()

    def test__shark(self):
        # TODO
        self.fail()

    def test__turkey(self):
        # TODO
        self.fail()
