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
        self.agent.summon(tier_5.Rhino(), ("team", 0))
        self.agent.summon(tier_5.Eagle(), ("team", 2))
        self.agent.summon(tier_5.Monkey(), ("team", 4))

        Tier5.monkey(self.agent, ("team", 4), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 7)
        self.assertTrue(self.agent.team[0].battle_atk == 7)
        self.assertTrue(self.agent.team[0].hp == 11)
        self.assertTrue(self.agent.team[0].battle_hp == 11)

        self.agent.team[4].xp = 2

        Tier5.monkey(self.agent, ("team", 4), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 11)
        self.assertTrue(self.agent.team[0].battle_atk == 11)
        self.assertTrue(self.agent.team[0].hp == 17)
        self.assertTrue(self.agent.team[0].battle_hp == 17)

        self.agent.team[4].xp = 5

        Tier5.monkey(self.agent, ("team", 4), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 17)
        self.assertTrue(self.agent.team[0].battle_atk == 17)
        self.assertTrue(self.agent.team[0].hp == 26)
        self.assertTrue(self.agent.team[0].battle_hp == 26)

    def test__poodle(self):
        self.agent.summon(tier_1.Fish(), ("team", 4))
        self.agent.summon(tier_2.Shrimp(), ("team", 3))
        self.agent.summon(tier_1.Fish(), ("team", 2))
        self.agent.summon(tier_5.Poodle(), ("team", 1))
        self.agent.summon(tier_5.Cow(), ("team", 0))

        Tier5.poodle(self.agent, ("team", 1), ("team", 4))
        self.assertTrue(self.agent.team[4].atk == 3)
        self.assertTrue(self.agent.team[4].battle_atk == 3)
        self.assertTrue(self.agent.team[4].hp == 3)
        self.assertTrue(self.agent.team[4].battle_hp == 3)

        self.assertTrue(self.agent.team[3].atk == 3)
        self.assertTrue(self.agent.team[3].battle_atk == 3)
        self.assertTrue(self.agent.team[3].hp == 4)
        self.assertTrue(self.agent.team[3].battle_hp == 4)

        self.assertTrue(self.agent.team[2].atk == 2)
        self.assertTrue(self.agent.team[2].battle_atk == 2)
        self.assertTrue(self.agent.team[2].hp == 2)
        self.assertTrue(self.agent.team[2].battle_hp == 2)

        self.assertTrue(self.agent.team[1].atk == 3)
        self.assertTrue(self.agent.team[1].battle_atk == 3)
        self.assertTrue(self.agent.team[1].hp == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 3)

        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_atk == 4)
        self.assertTrue(self.agent.team[0].hp == 6)
        self.assertTrue(self.agent.team[0].battle_hp == 6)

        self.agent.team[1].xp = 2
        Tier5.poodle(self.agent, ("team", 1), ("team", 4))
        self.assertTrue(self.agent.team[4].atk == 5)
        self.assertTrue(self.agent.team[4].battle_atk == 5)
        self.assertTrue(self.agent.team[4].hp == 5)
        self.assertTrue(self.agent.team[4].battle_hp == 5)

        self.assertTrue(self.agent.team[3].atk == 5)
        self.assertTrue(self.agent.team[3].battle_atk == 5)
        self.assertTrue(self.agent.team[3].hp == 6)
        self.assertTrue(self.agent.team[3].battle_hp == 6)

        self.assertTrue(self.agent.team[2].atk == 2)
        self.assertTrue(self.agent.team[2].battle_atk == 2)
        self.assertTrue(self.agent.team[2].hp == 2)
        self.assertTrue(self.agent.team[2].battle_hp == 2)

        self.assertTrue(self.agent.team[1].atk == 5)
        self.assertTrue(self.agent.team[1].battle_atk == 5)
        self.assertTrue(self.agent.team[1].hp == 5)
        self.assertTrue(self.agent.team[1].battle_hp == 5)

        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_atk == 4)
        self.assertTrue(self.agent.team[0].hp == 6)
        self.assertTrue(self.agent.team[0].battle_hp == 6)

    def test__rhino(self):
        self.agent.in_shop = False
        self.agent.summon(tier_5.Rhino(), ("team", 0))
        self.agent.summon(tier_5.Rhino(), ("enemy", 0))
        self.agent.summon(tier_1.Fish(), ("enemy", 1))

        Tier5.rhino(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.enemy[0].battle_hp == 4)

        Tier5.rhino(self.agent, ("enemy", 0), ("enemy", 4))
        self.assertTrue(self.agent.team[0].battle_hp == 4)

        self.agent.summon(tier_5.Rhino(), ("enemy", 0))
        self.agent.team[0].xp = 2

        Tier5.rhino(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

    def test__scorpion(self):
        Tier5.scorpion(self.agent, ("team", 0), ("team", 4))

    def test__seal(self):
        self.agent.summon(tier_5.Seal(), ("team", 0))
        Tier5.seal(self.agent, ("team", 0), ("team", 4))

        self.agent.summon(tier_5.Cow(), ("team", 1))
        Tier5.seal(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[1].atk == 5)
        self.assertTrue(self.agent.team[1].battle_atk == 5)
        self.assertTrue(self.agent.team[1].hp == 7)
        self.assertTrue(self.agent.team[1].battle_hp == 7)

        self.agent.summon(tier_5.Poodle(), ("team", 2))
        Tier5.seal(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[1].atk == 6)
        self.assertTrue(self.agent.team[1].battle_atk == 6)
        self.assertTrue(self.agent.team[1].hp == 8)
        self.assertTrue(self.agent.team[1].battle_hp == 8)

        self.assertTrue(self.agent.team[2].atk == 3)
        self.assertTrue(self.agent.team[2].battle_atk == 3)
        self.assertTrue(self.agent.team[2].hp == 3)
        self.assertTrue(self.agent.team[2].battle_hp == 3)

        self.agent.team[0].xp = 2
        Tier5.seal(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[1].atk == 8)
        self.assertTrue(self.agent.team[1].battle_atk == 8)
        self.assertTrue(self.agent.team[1].hp == 10)
        self.assertTrue(self.agent.team[1].battle_hp == 10)

        self.assertTrue(self.agent.team[2].atk == 5)
        self.assertTrue(self.agent.team[2].battle_atk == 5)
        self.assertTrue(self.agent.team[2].hp == 5)
        self.assertTrue(self.agent.team[2].battle_hp == 5)

        self.agent.team[0].xp = 5
        Tier5.seal(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[1].atk == 11)
        self.assertTrue(self.agent.team[1].battle_atk == 11)
        self.assertTrue(self.agent.team[1].hp == 13)
        self.assertTrue(self.agent.team[1].battle_hp == 13)

        self.assertTrue(self.agent.team[2].atk == 8)
        self.assertTrue(self.agent.team[2].battle_atk == 8)
        self.assertTrue(self.agent.team[2].hp == 8)
        self.assertTrue(self.agent.team[2].battle_hp == 8)

    def test__shark(self):
        self.agent.summon(tier_5.Shark(), ("team", 0))
        Tier5.shark(self.agent, ("team", 0), ("team", 4), fainted=tier_5.Cow())

        self.assertTrue(self.agent.team[0].atk == 6)
        self.assertTrue(self.agent.team[0].battle_atk == 6)
        self.assertTrue(self.agent.team[0].hp == 6)
        self.assertTrue(self.agent.team[0].battle_hp == 6)

        self.agent.team[0].xp = 2
        Tier5.shark(self.agent, ("team", 0), ("team", 4), fainted=tier_5.Cow())

        self.assertTrue(self.agent.team[0].atk == 10)
        self.assertTrue(self.agent.team[0].battle_atk == 10)
        self.assertTrue(self.agent.team[0].hp == 10)
        self.assertTrue(self.agent.team[0].battle_hp == 10)

        self.agent.team[0].xp = 5
        Tier5.shark(self.agent, ("team", 0), ("team", 4), fainted=tier_5.Cow())

        self.assertTrue(self.agent.team[0].atk == 16)
        self.assertTrue(self.agent.team[0].battle_atk == 16)
        self.assertTrue(self.agent.team[0].hp == 16)
        self.assertTrue(self.agent.team[0].battle_hp == 16)

    def test__turkey(self):
        self.agent.summon(tier_5.Turkey(), ("team", 4))
        self.agent.summon(tier_5.Cow(), ("team", 2))
        Tier5.turkey(self.agent, ("team", 4), ("team", 2))

        self.assertTrue(self.agent.team[2].atk == 6)
        self.assertTrue(self.agent.team[2].battle_atk == 6)
        self.assertTrue(self.agent.team[2].hp == 9)
        self.assertTrue(self.agent.team[2].battle_hp == 9)

        self.agent.team[4].xp = 2
        Tier5.turkey(self.agent, ("team", 4), ("team", 2))

        self.assertTrue(self.agent.team[2].atk == 10)
        self.assertTrue(self.agent.team[2].battle_atk == 10)
        self.assertTrue(self.agent.team[2].hp == 15)
        self.assertTrue(self.agent.team[2].battle_hp == 15)

        self.agent.team[4].xp = 5
        Tier5.turkey(self.agent, ("team", 4), ("team", 2))

        self.assertTrue(self.agent.team[2].atk == 16)
        self.assertTrue(self.agent.team[2].battle_atk == 16)
        self.assertTrue(self.agent.team[2].hp == 24)
        self.assertTrue(self.agent.team[2].battle_hp == 24)
