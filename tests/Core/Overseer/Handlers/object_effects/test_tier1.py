from unittest import TestCase

from src.core.game_elements.game_objects.animals import tier_1
from src.core.game_systems import ShopSystem, BattleSystem
from src.core.overseer import MessageAgent

from src.core.overseer.handlers.object_effects.tier1 import Tier1


class TestTier1(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        ShopSystem(self.agent)
        BattleSystem(self.agent)

    def test__ant(self):
        self.agent.summon(tier_1.Bee(), ("team", 1))
        ant = tier_1.Ant()

        Tier1.ant(self.agent, ("team", 0), ("team", 4), ant)

        self.assertTrue(self.agent.team[1].atk == 3)
        self.assertTrue(self.agent.team[1].hp == 2)
        self.assertTrue(self.agent.team[1].battle_atk == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 2)

        ant.xp = 5
        self.assertTrue(ant.level == 3)

        Tier1.ant(self.agent, ("team", 0), ("team", 4), ant)

        self.assertTrue(self.agent.team[1].atk == 9)
        self.assertTrue(self.agent.team[1].hp == 5)
        self.assertTrue(self.agent.team[1].battle_atk == 9)
        self.assertTrue(self.agent.team[1].battle_hp == 5)

    def test__beaver(self):
        self.agent.summon(tier_1.Bee(), ("team", 1))
        self.agent.summon(tier_1.Beaver(), ("team", 0))

        Tier1.beaver(self.agent, ("team", 0), ("team", 3), removed=self.agent.team[0])
        self.assertTrue(self.agent.team[1].atk == 1)
        self.assertTrue(self.agent.team[1].hp == 2)
        self.assertTrue(self.agent.team[1].battle_atk == 1)
        self.assertTrue(self.agent.team[1].battle_hp == 2)

    def test__beetle(self):
        self.agent.summon(tier_1.Beetle(), ("team", 0))
        Tier1.beetle(self.agent, ("team", 0), ("team", 1))

        shop_anim = self.agent.shop[0].item
        new_shop_anim = shop_anim.__class__()

        self.assertTrue(shop_anim.hp == new_shop_anim.hp + 1)
        self.assertTrue(shop_anim.battle_hp == new_shop_anim.battle_hp + 1)
        self.assertTrue(shop_anim.atk == new_shop_anim.atk)
        self.assertTrue(shop_anim.battle_atk)

    def test__bluebird(self):
        self.agent.summon(tier_1.Bluebird(), ("team", 0))
        self.agent.summon(tier_1.Fish(), ("team", 3))
        Tier1.bluebird(self.agent, ("team", 0), ("team", 2))

        self.assertTrue(self.agent.team[3].atk == 3)
        self.assertTrue(self.agent.team[3].battle_atk == 3)

    def test__cricket(self):
        cricket = tier_1.Cricket()
        cricket.xp = 5

        Tier1.cricket(self.agent, ("team", 0), ("team", 2), cricket)
        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].battle_atk == 3)
        self.assertTrue(self.agent.team[0].hp == 3)
        self.assertTrue(self.agent.team[0].battle_hp == 3)

    def test__duck(self):
        self.agent.summon(tier_1.Duck(), ("team", 0))
        Tier1.duck(self.agent, ("team", 0), ("team", 4), removed=self.agent.team[0])

        shop_anim = self.agent.shop[0].item
        new_shop_anim = shop_anim.__class__()

        self.assertTrue(shop_anim.hp == new_shop_anim.hp + 1)
        self.assertTrue(shop_anim.battle_hp == new_shop_anim.battle_hp + 1)
        self.assertTrue(shop_anim.atk == new_shop_anim.atk)
        self.assertTrue(shop_anim.battle_atk)

    def test__fish(self):
        self.agent.summon(tier_1.Fish(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("team", 1))

        self.agent.team[0].xp = 2
        Tier1.fish(self.agent, ("team", 0), ("team", 1))
        self.assertTrue(self.agent.team[1].atk == 2)
        self.assertTrue(self.agent.team[1].battle_atk == 2)
        self.assertTrue(self.agent.team[1].hp == 2)
        self.assertTrue(self.agent.team[1].battle_hp == 2)

        self.agent.team[0].xp = 5
        Tier1.fish(self.agent, ("team", 0), ("team", 3))
        self.assertTrue(self.agent.team[1].atk == 4)
        self.assertTrue(self.agent.team[1].battle_atk == 4)
        self.assertTrue(self.agent.team[1].hp == 4)
        self.assertTrue(self.agent.team[1].battle_hp == 4)

    def test__horse(self):
        self.agent.summon(tier_1.Horse(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("team", 0))

        Tier1.horse(self.agent, ("team", 1), ("team", 0))
        self.assertTrue(self.agent.team[0].atk == 1)
        self.assertTrue(self.agent.team[0].battle_atk == 2)
        self.assertTrue(self.agent.team[0].hp == 1)
        self.assertTrue(self.agent.team[0].battle_hp == 1)

    def test__ladybug(self):
        self.agent.summon(tier_1.Ladybug(), ("team", 0))

        Tier1.ladybug(self.agent, ("team", 0), ("team", 2))
        self.assertTrue(self.agent.team[0].battle_hp == 4)
        self.assertTrue(self.agent.team[0].hp == 3)
        self.assertTrue(self.agent.team[0].battle_atk == 2)
        self.assertTrue(self.agent.team[0].atk == 1)

    def test__mosquito(self):
        self.agent.in_shop = False
        self.agent.summon(tier_1.Fish(), ("enemy", 0))
        self.agent.summon(tier_1.Mosquito(), ("team", 0))

        Tier1.mosquito(self.agent, ("team", 0), ("team", 3), self.agent.team[0])
        self.assertTrue(self.agent.enemy[0].battle_hp == 1)
        self.assertTrue(self.agent.enemy[0].hp == 2)

    def test__otter(self):
        self.agent.summon(tier_1.Otter(), ("team", 0))
        self.agent.summon(tier_1.Fish(), ("team", 2))

        Tier1.otter(self.agent, ("team", 0), ("team", 3))
        self.assertTrue(self.agent.team[2].atk == 3)
        self.assertTrue(self.agent.team[2].battle_atk == 3)
        self.assertTrue(self.agent.team[2].hp == 3)
        self.assertTrue(self.agent.team[2].battle_hp == 3)

    def test__pig(self):
        self.agent.summon(tier_1.Pig(), ("team", 0))

        Tier1.pig(self.agent, ("team", 0), ("team", 4), removed=self.agent.team[0])
        self.assertTrue(self.agent.gold == 11)
