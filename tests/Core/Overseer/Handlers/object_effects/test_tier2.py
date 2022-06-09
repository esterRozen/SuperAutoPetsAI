from unittest import TestCase

from src.core.game_elements.game_objects.equipment import Weak
from src.core.overseer import MessageAgent
from src.core.game_systems import ShopSystem, BattleSystem
from src.core.game_elements.game_objects.animals import tier_2
from src.core.overseer.handlers.object_effects.tier2 import Tier2


class TestTier2(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        ShopSystem(self.agent)
        BattleSystem(self.agent)

    def test__bat(self):
        self.agent.in_shop = False
        self.agent.summon(tier_2.Bat(), ("team", 0))
        self.agent.summon(tier_2.Swan(), ("enemy", 0))

        Tier2.bat(self.agent, ("team", 0), ("team", 2))
        self.assertTrue(isinstance(self.agent.enemy[0].held, Weak))

    def test__crab(self):
        self.agent.summon(tier_2.Crab(), ("team", 0))
        self.agent.summon(tier_2.Elephant(), ("team", 1))

        Tier2.crab(self.agent, ("team", 0), ("team", 2))
        self.assertTrue(self.agent.team[0].battle_hp == 2)
        self.assertTrue(self.agent.team[0].hp == 1)
        self.assertTrue(self.agent.team[0].battle_atk == 3)
        self.assertTrue(self.agent.team[0].atk == 3)

    def test__dodo(self):
        self.agent.summon(tier_2.Dodo(), ("team", 2))
        self.agent.summon(tier_2.Flamingo(), ("team", 0))

        Tier2.dodo(self.agent, ("team", 2), ("team", 3))
        self.assertTrue(self.agent.team[0].battle_atk == 5)
        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 2)
        self.assertTrue(self.agent.team[0].hp == 2)

    def test__dromedary(self):
        self.agent.summon(tier_2.Dromedary(), ("team", 0))
        Tier2.dromedary(self.agent, ("team", 0), ("team", 4))

        shop_anim = self.agent.shop[0].item
        new_anim = shop_anim.__class__()

        self.assertTrue(shop_anim.battle_atk == new_anim.battle_atk + 1)
        self.assertTrue(shop_anim.atk == new_anim.atk + 1)
        self.assertTrue(shop_anim.battle_hp == new_anim.battle_hp + 1)
        self.assertTrue(shop_anim.hp == new_anim.hp + 1)

    def test__elephant(self):
        self.agent.summon(tier_2.Elephant(), ("team", 0))
        self.agent.summon(tier_2.Flamingo(), ("team", 1))

        Tier2.elephant(self.agent, ("team", 0), ("team", 2))

        self.assertTrue(self.agent.team[1].battle_hp == 1)

    def test__flamingo(self):
        self.agent.summon(tier_2.Flamingo(), ("team", 0))
        self.agent.summon(tier_2.Peacock(), ("team", 1))
        self.agent.summon(tier_2.Shrimp(), ("team", 3))

        Tier2.flamingo(self.agent, ("team", 0), ("team", 2), fainted=self.agent.team[0])

        self.assertTrue(self.agent.team[1].battle_atk == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 6)
        self.assertTrue(self.agent.team[3].battle_atk == 3)
        self.assertTrue(self.agent.team[3].battle_hp == 4)

    def test__hedgehog(self):
        self.agent.in_shop = False
        hedgehog = tier_2.Hedgehog()
        self.agent.summon(tier_2.Elephant(), ("team", 1))
        self.agent.summon(tier_2.Elephant(), ("team", 2))
        self.agent.summon(tier_2.Elephant(), ("team", 3))

        self.agent.summon(tier_2.Elephant(), ("enemy", 0))

        Tier2.hedgehog(self.agent, ("team", 0), ("team", 1), fainted=hedgehog)

        self.assertTrue(self.agent.team[1].battle_hp == 3)
        self.assertTrue(self.agent.team[2].battle_hp == 3)
        self.assertTrue(self.agent.team[3].battle_hp == 3)

        self.assertTrue(self.agent.enemy[0].battle_hp == 3)

    def test__peacock(self):
        self.agent.summon(tier_2.Peacock(), ("team", 0))

        Tier2.peacock(self.agent, ("team", 0), ("team", 1))

        self.assertTrue(self.agent.team[0].battle_atk == 6)

    def test__rat(self):
        rat = tier_2.Rat()
        self.agent.in_shop = False

        Tier2.rat(self.agent, ("team", 0), ("team", 1), rat)
        self.assertTrue(isinstance(self.agent.enemy[0], tier_2.Dirty_Rat))

    def test__shrimp(self):
        self.agent.summon(tier_2.Shrimp(), ("team", 0))
        self.agent.summon(tier_2.Flamingo(), ("team", 2))

        Tier2.shrimp(self.agent, ("team", 0), ("team", 3))

        self.assertTrue(self.agent.team[2].atk == 4)
        self.assertTrue(self.agent.team[2].battle_atk == 4)
        self.assertTrue(self.agent.team[2].hp == 3)
        self.assertTrue(self.agent.team[2].battle_hp == 3)

    def test__spider(self):
        spider = tier_2.Spider()

        Tier2.spider(self.agent, ("team", 0), ("team", 3), spider)

        self.assertTrue(self.agent.team[0].battle_hp == 2)
        self.assertTrue(self.agent.team[0].battle_atk == 2)
        self.assertTrue(self.agent.team[0].xp == 0)

        spider.xp = 5
        self.agent.team.faint(0)
        Tier2.spider(self.agent, ("team", 0), ("team", 3), spider)
        self.assertTrue(self.agent.team[0].battle_hp == 2)
        self.assertTrue(self.agent.team[0].battle_atk == 2)
        self.assertTrue(self.agent.team[0].xp == 5)

    def test__swan(self):
        self.agent.summon(tier_2.Swan(), ("team", 0))
        Tier2.swan(self.agent, ("team", 0), ("team", 2))
        self.assertTrue(self.agent.gold == 11)

        self.agent.team[0].xp = 5
        Tier2.swan(self.agent, ("team", 0), ("team", 2))
        self.assertTrue(self.agent.gold == 14)

    def test__tabby_cat(self):
        self.agent.summon(tier_2.Tabby_Cat(), ("team", 0))
        self.agent.summon(tier_2.Flamingo(), ("team", 1))
        self.agent.summon(tier_2.Flamingo(), ("team", 2))

        Tier2.tabby_cat(self.agent, ("team", 0), ("team", 3))

        self.assertTrue(self.agent.team[1].atk == 4)
        self.assertTrue(self.agent.team[1].battle_atk == 5)
        self.assertTrue(self.agent.team[1].hp == 2)
        self.assertTrue(self.agent.team[1].battle_hp == 2)

        self.assertTrue(self.agent.team[2].atk == 4)
        self.assertTrue(self.agent.team[2].battle_atk == 5)
        self.assertTrue(self.agent.team[2].hp == 2)
        self.assertTrue(self.agent.team[2].battle_hp == 2)
