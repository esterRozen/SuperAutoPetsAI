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

        Tier1.beaver(self.agent, ("team", 0), ("team", 3))
        self.assertTrue(self.agent.team[1].atk == 1)
        self.assertTrue(self.agent.team[1].hp == 2)
        self.assertTrue(self.agent.team[1].battle_atk == 1)
        self.assertTrue(self.agent.team[1].battle_hp == 2)

    def test__beetle(self):
        # TODO
        self.fail()

    def test__bluebird(self):
        # TODO
        self.fail()

    def test__cricket(self):
        # TODO
        self.fail()

    def test__duck(self):
        # TODO
        self.fail()

    def test__fish(self):
        # TODO
        self.fail()

    def test__horse(self):
        # TODO
        self.fail()

    def test__ladybug(self):
        # TODO
        self.fail()

    def test__mosquito(self):
        # TODO
        self.fail()

    def test__otter(self):
        # TODO
        self.fail()

    def test__pig(self):
        # TODO
        self.fail()
