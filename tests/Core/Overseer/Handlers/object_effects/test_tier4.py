from unittest import TestCase

from src.core.game_elements.abstract_elements import Empty, Team
from src.core.game_elements.game_objects.animals import tier_4
from src.core.game_elements.game_objects.equipment import Weak
from src.core.game_systems import ShopSystem, BattleSystem
from src.core.overseer import MessageAgent
from src.core.overseer.handlers.object_effects import Tier4


class TestTier4(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        ShopSystem(self.agent)
        BattleSystem(self.agent)

    def test__bison(self):
        self.agent.summon(tier_4.Bison(), ("team", 0))
        self.agent.summon(tier_4.Bus(), ("team", 1))

        Tier4.bison(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].atk == 4)

        self.agent.team[1].xp = 5
        Tier4.bison(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].hp == 6)
        self.assertTrue(self.agent.team[0].atk == 6)

        self.agent.team[0].xp = 2
        Tier4.bison(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].hp == 10)
        self.assertTrue(self.agent.team[0].atk == 10)

        self.agent.team[0].xp = 5
        Tier4.bison(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].hp == 16)
        self.assertTrue(self.agent.team[0].atk == 16)

    def test__buffalo(self):
        self.agent.summon(tier_4.Buffalo(), ("team", 0))

        Tier4.buffalo(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].hp == 5)
        self.assertTrue(self.agent.team[0].atk == 5)

        self.agent.team[0].xp = 2
        Tier4.buffalo(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].hp == 7)
        self.assertTrue(self.agent.team[0].atk == 7)

        self.agent.team[0].xp = 5
        Tier4.buffalo(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].hp == 10)
        self.assertTrue(self.agent.team[0].atk == 10)

    def test__caterpillar(self):
        self.agent.summon(tier_4.Caterpillar(), ("team", 0))

        Tier4.caterpillar(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].xp == 1)
        self.assertTrue(self.agent.team[0].hp == 2)
        self.assertTrue(self.agent.team[0].atk == 2)

        Tier4.caterpillar(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].xp == 2)
        Tier4.caterpillar(self.agent, ("team", 0), ("team", 4))
        Tier4.caterpillar(self.agent, ("team", 0), ("team", 4))
        Tier4.caterpillar(self.agent, ("team", 0), ("team", 4))
        # start battle type message
        Tier4.caterpillar(self.agent, ("team", 0), ("team", 4), self.agent.team[0])
        self.assertTrue(isinstance(self.agent.team[0], tier_4.Butterfly))

    def test__deer(self):
        deer = tier_4.Deer()

        Tier4.deer(self.agent, ("team", 0), ("team", 4), fainted=deer)
        self.assertTrue(isinstance(self.agent.team[0], tier_4.Bus))

    def test__dolphin(self):
        self.agent.in_shop = False
        self.agent.summon(tier_4.Dolphin(), ("team", 0))
        self.agent.summon(tier_4.Buffalo(), ("enemy", 0))

        self.assertTrue(isinstance(self.agent.enemy[0], tier_4.Buffalo))
        Tier4.dolphin(self.agent, ("team", 0), ("team", 4), self.agent.team[0])

        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.summon(tier_4.Dolphin(), ("enemy", 0))
        Tier4.dolphin(self.agent, ("enemy", 0), ("enemy", 4), self.agent.team[0])

        self.assertTrue(self.agent.team[0].battle_hp == 1)

    def test__hippo(self):
        self.agent.summon(tier_4.Hippo(), ("team", 0))

        Tier4.hippo(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].battle_atk == 7)
        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 10)
        self.assertTrue(self.agent.team[0].hp == 7)

        self.agent.team[0].xp = 2
        Tier4.hippo(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].battle_atk == 13)
        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 16)
        self.assertTrue(self.agent.team[0].hp == 7)

        self.agent.team[0].xp = 5
        Tier4.hippo(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].battle_atk == 22)
        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 25)
        self.assertTrue(self.agent.team[0].hp == 7)

    def test__llama(self):
        self.agent.summon(tier_4.Llama(), ("team", 0))
        Tier4.llama(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].battle_atk == 5)
        self.assertTrue(self.agent.team[0].atk == 5)
        self.assertTrue(self.agent.team[0].battle_hp == 8)
        self.assertTrue(self.agent.team[0].hp == 8)

        self.agent.team[0].xp = 2
        Tier4.llama(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].battle_atk == 9)
        self.assertTrue(self.agent.team[0].atk == 9)
        self.assertTrue(self.agent.team[0].battle_hp == 12)
        self.assertTrue(self.agent.team[0].hp == 12)

        self.agent.team[0].xp = 5
        Tier4.llama(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].battle_atk == 15)
        self.assertTrue(self.agent.team[0].atk == 15)
        self.assertTrue(self.agent.team[0].battle_hp == 18)
        self.assertTrue(self.agent.team[0].hp == 18)

        self.agent.summon(tier_4.Bus(), ("team", 1))
        self.agent.summon(tier_4.Bus(), ("team", 2))
        self.agent.summon(tier_4.Bus(), ("team", 3))
        self.agent.summon(tier_4.Bus(), ("team", 4))

        Tier4.llama(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].battle_atk == 15)
        self.assertTrue(self.agent.team[0].atk == 15)
        self.assertTrue(self.agent.team[0].battle_hp == 18)
        self.assertTrue(self.agent.team[0].hp == 18)

    def test__lobster(self):
        self.agent.summon(tier_4.Lobster(), ("team", 0))
        self.agent.summon(tier_4.Bison(), ("team", 1))

        Tier4.lobster(self.agent, ("team", 0), ("team", 1))

        self.assertTrue(self.agent.team[1].atk == 6)
        self.assertTrue(self.agent.team[1].battle_atk == 6)
        self.assertTrue(self.agent.team[1].hp == 7)
        self.assertTrue(self.agent.team[1].battle_hp == 7)

        self.agent.team[0].xp = 2
        Tier4.lobster(self.agent, ("team", 0), ("team", 1))

        self.assertTrue(self.agent.team[1].atk == 10)
        self.assertTrue(self.agent.team[1].battle_atk == 10)
        self.assertTrue(self.agent.team[1].hp == 13)
        self.assertTrue(self.agent.team[1].battle_hp == 13)

        self.agent.team[0].xp = 5
        Tier4.lobster(self.agent, ("team", 0), ("team", 1))

        self.assertTrue(self.agent.team[1].atk == 16)
        self.assertTrue(self.agent.team[1].battle_atk == 16)
        self.assertTrue(self.agent.team[1].hp == 22)
        self.assertTrue(self.agent.team[1].battle_hp == 22)

    def test__microbe(self):
        self.agent.in_shop = False
        self.agent.summon(tier_4.Bus(), ("team", 1))
        self.agent.summon(tier_4.Hippo(), ("team", 3))
        self.agent.summon(tier_4.Bison(), ("enemy", 0))
        self.agent.summon(tier_4.Rooster(), ("enemy", 4))

        Tier4.microbe(self.agent, ("team", 0), ("enemy", 0), tier_4.Microbe())

        for unit in self.agent.team.units():
            self.assertTrue(isinstance(unit.held, Weak))

        for unit in self.agent.enemy.units():
            self.assertTrue(isinstance(unit.held, Weak))

    def test__parrot(self):
        # TODO
        self.fail()

    def test__penguin(self):
        self.agent.summon(tier_4.Penguin(), ("team", 0))
        self.agent.summon(tier_4.Bus(), ("team", 1))
        self.agent.team[1].xp = 2
        self.agent.summon(tier_4.Bus(), ("team", 2))
        self.agent.team[2].xp = 5

        self.agent.summon(tier_4.Bus(), ("team", 3))
        self.agent.summon(tier_4.Bus(), ("team", 4))
        self.agent.team[4].xp = 2

        Tier4.penguin(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].atk == 1)
        self.assertTrue(self.agent.team[0].battle_atk == 1)
        self.assertTrue(self.agent.team[0].hp == 2)
        self.assertTrue(self.agent.team[0].battle_hp == 2)

        self.assertTrue(self.agent.team[1].atk == 6)
        self.assertTrue(self.agent.team[1].battle_atk == 6)
        self.assertTrue(self.agent.team[1].hp == 6)
        self.assertTrue(self.agent.team[1].battle_hp == 6)

        self.assertTrue(self.agent.team[2].atk == 6)
        self.assertTrue(self.agent.team[2].battle_atk == 6)
        self.assertTrue(self.agent.team[2].hp == 6)
        self.assertTrue(self.agent.team[2].battle_hp == 6)

        self.assertTrue(self.agent.team[3].atk == 5)
        self.assertTrue(self.agent.team[3].battle_atk == 5)
        self.assertTrue(self.agent.team[3].hp == 5)
        self.assertTrue(self.agent.team[3].battle_hp == 5)

        self.assertTrue(self.agent.team[4].atk == 6)
        self.assertTrue(self.agent.team[4].battle_atk == 6)
        self.assertTrue(self.agent.team[4].hp == 6)
        self.assertTrue(self.agent.team[4].battle_hp == 6)

        self.agent.team[0].xp = 2
        Tier4.penguin(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].atk == 1)
        self.assertTrue(self.agent.team[0].battle_atk == 1)
        self.assertTrue(self.agent.team[0].hp == 2)
        self.assertTrue(self.agent.team[0].battle_hp == 2)

        self.agent.team[0].xp = 5
        Tier4.penguin(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].atk == 1)
        self.assertTrue(self.agent.team[0].battle_atk == 1)
        self.assertTrue(self.agent.team[0].hp == 2)
        self.assertTrue(self.agent.team[0].battle_hp == 2)

        self.assertTrue(self.agent.team[1].atk == 11)
        self.assertTrue(self.agent.team[1].battle_atk == 11)
        self.assertTrue(self.agent.team[1].hp == 11)
        self.assertTrue(self.agent.team[1].battle_hp == 11)

        self.assertTrue(self.agent.team[2].atk == 11)
        self.assertTrue(self.agent.team[2].battle_atk == 11)
        self.assertTrue(self.agent.team[2].hp == 11)
        self.assertTrue(self.agent.team[2].battle_hp == 11)

        self.assertTrue(self.agent.team[3].atk == 5)
        self.assertTrue(self.agent.team[3].battle_atk == 5)
        self.assertTrue(self.agent.team[3].hp == 5)
        self.assertTrue(self.agent.team[3].battle_hp == 5)

        self.assertTrue(self.agent.team[4].atk == 11)
        self.assertTrue(self.agent.team[4].battle_atk == 11)
        self.assertTrue(self.agent.team[4].hp == 11)
        self.assertTrue(self.agent.team[4].battle_hp == 11)

    def test__rooster(self):
        rooster = tier_4.Rooster()
        Tier4.rooster(self.agent, ("team", 0), ("team", 4), fainted=rooster)
        self.assertTrue(isinstance(self.agent.team[0], tier_4.Chick))
        self.assertTrue(isinstance(self.agent.team[1], Empty))

        self.agent.team = Team()
        rooster.xp = 2
        Tier4.rooster(self.agent, ("team", 0), ("team", 4), fainted=rooster)
        self.assertTrue(isinstance(self.agent.team[0], tier_4.Chick))
        self.assertTrue(isinstance(self.agent.team[1], tier_4.Chick))
        self.assertTrue(isinstance(self.agent.team[2], Empty))

        self.agent.team = Team()
        rooster.xp = 5
        Tier4.rooster(self.agent, ("team", 0), ("team", 4), fainted=rooster)
        self.assertTrue(isinstance(self.agent.team[0], tier_4.Chick))
        self.assertTrue(isinstance(self.agent.team[1], tier_4.Chick))
        self.assertTrue(isinstance(self.agent.team[2], tier_4.Chick))
        self.assertTrue(isinstance(self.agent.team[3], Empty))

    def test__skunk(self):
        self.agent.in_shop = False
        self.agent.summon(tier_4.Skunk(), ("team", 0))
        self.agent.summon(tier_4.Hippo(), ("enemy", 0))

        Tier4.skunk(self.agent, ("team", 0), ("team", 3), self.agent.team[0])
        self.assertTrue(self.agent.enemy[0].battle_hp == 5)

        self.agent.enemy = Team()
        self.agent.summon(tier_4.Hippo(), ("enemy", 0))
        self.agent.team[0].xp = 2

        Tier4.skunk(self.agent, ("team", 0), ("team", 3), self.agent.team[0])
        self.assertTrue(self.agent.enemy[0].battle_hp == 3)

        self.agent.enemy = Team()
        self.agent.summon(tier_4.Hippo(), ("enemy", 0))
        self.agent.team[0].xp = 5

        Tier4.skunk(self.agent, ("team", 0), ("team", 3), self.agent.team[0])
        self.assertTrue(self.agent.enemy[0].battle_hp == 1)

    def test__squirrel(self):
        self.agent.summon(tier_4.Squirrel(), ("team", 0))
        Tier4.squirrel(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.shop[5].item.cost == 2)

        self.agent.team[0].xp = 2
        Tier4.squirrel(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.shop[5].item.cost == 0)

        self.agent.shop.reroll()
        self.agent.team[0].xp = 5
        Tier4.squirrel(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.shop[5].item.cost == 0)

    def test__whale(self):
        # TODO
        self.fail()

    def test__worm(self):
        self.agent.summon(tier_4.Worm(), ("team", 0))
        Tier4.worm(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_atk == 4)
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 4)

        self.agent.team[0].xp = 2
        Tier4.worm(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].atk == 6)
        self.assertTrue(self.agent.team[0].battle_atk == 6)
        self.assertTrue(self.agent.team[0].hp == 6)
        self.assertTrue(self.agent.team[0].battle_hp == 6)

        self.agent.team[0].xp = 5
        Tier4.worm(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].atk == 9)
        self.assertTrue(self.agent.team[0].battle_atk == 9)
        self.assertTrue(self.agent.team[0].hp == 9)
        self.assertTrue(self.agent.team[0].battle_hp == 9)
