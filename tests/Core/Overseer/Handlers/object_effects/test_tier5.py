from unittest import TestCase

from src.core.game_elements.abstract_elements import Unarmed, Empty
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
        self.agent.in_shop = False
        self.agent.summon(tier_5.Crocodile(), ("team", 0))
        Tier5.crocodile(self.agent, ("team", 0), ("team", 4))

        self.agent.summon(tier_5.Rhino(), ("enemy", 0))

        Tier5.crocodile(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.enemy[0].battle_hp == 1)

        Tier5.crocodile(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.summon(tier_5.Crocodile(), ("enemy", 0))
        Tier5.crocodile(self.agent, ("enemy", 0), ("enemy", 4))
        self.assertTrue(isinstance(self.agent.team[0], Empty))

        self.agent.summon(tier_5.Rhino(), ("team", 0))
        self.agent.enemy[0].xp = 2

        Tier5.crocodile(self.agent, ("enemy", 0), ("enemy", 4))
        self.assertTrue(isinstance(self.agent.team[0], Empty))

    def test__eagle(self):
        eagle = tier_5.Eagle()
        Tier5.eagle(self.agent, ("team", 0), ("team", 4), fainted=eagle)
        self.assertTrue(self.agent.team[0].level == 1)

        eagle.xp = 2
        Tier5.eagle(self.agent, ("team", 1), ("team", 4), fainted=eagle)
        animal = self.agent.team[1]
        orig_anim = animal.__class__()
        self.assertTrue(self.agent.team[1].level == 2)
        self.assertTrue(animal.atk == 2 * orig_anim.atk)
        self.assertTrue(animal.battle_atk == 2 * orig_anim.battle_atk)
        self.assertTrue(animal.hp == 2 * orig_anim.hp)
        self.assertTrue(animal.battle_hp == 2 * orig_anim.battle_hp)

        eagle.xp = 5
        Tier5.eagle(self.agent, ("team", 2), ("team", 4), fainted=eagle)
        self.assertTrue(self.agent.team[2].level == 3)

    def test__goat(self):
        Tier5.goat(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.gold == 11)

    def test__monkey(self):
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
