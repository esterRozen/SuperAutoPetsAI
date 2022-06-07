from unittest import TestCase

from src.core.game_elements.abstract_elements import Empty
from src.core.game_elements.game_objects.animals import tier_3
from src.core.game_systems import BattleSystem, ShopSystem
from src.core.overseer import MessageAgent
from src.core.overseer.handlers.object_effects import Tier3


class TestTier3(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        BattleSystem(self.agent)
        ShopSystem(self.agent)

    def test__badger(self):
        self.agent.in_shop = False

        self.agent.summon(tier_3.Kangaroo(), ("team", 0))
        badger = tier_3.Badger()
        self.agent.summon(tier_3.Kangaroo(), ("team", 2))

        Tier3.badger(self.agent, ("team", 1), ("team", 3), badger)

        self.assertTrue(isinstance(self.agent.team[0], Empty))
        self.assertTrue(isinstance(self.agent.team[2], Empty))

        self.agent.summon(tier_3.Kangaroo(), ("team", 1))
        self.agent.summon(tier_3.Kangaroo(), ("enemy", 0))

        Tier3.badger(self.agent, ("team", 0), ("team", 3), badger)

        self.assertTrue(isinstance(self.agent.team[1], Empty))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.summon(tier_3.Giraffe(), ("team", 0))
        self.agent.summon(tier_3.Giraffe(), ("team", 2))

        Tier3.badger(self.agent, ("team", 1), ("team", 3), badger)

        self.assertTrue(self.agent.team[0].battle_hp == 2)
        self.assertTrue(self.agent.team[2].battle_hp == 2)

    def test__blowfish(self):
        self.agent.in_shop = False
        self.agent.summon(tier_3.Blowfish(), ("team", 0))
        self.agent.summon(tier_3.Giraffe(), ("enemy", 0))

        Tier3.blowfish(self.agent, ("team", 0), ("team", 1))

        self.assertTrue(self.agent.enemy[0].battle_hp == 2)

    def test__camel(self):
        # TODO
        self.fail()

    def test__caterpillar(self):
        # TODO
        self.fail()

    def test__dog(self):
        # TODO
        self.fail()

    def test__giraffe(self):
        # TODO
        self.fail()

    def test__hatching_chick(self):
        # TODO
        self.fail()

    def test__kangaroo(self):
        # TODO
        self.fail()

    def test__owl(self):
        # TODO
        self.fail()

    def test__ox(self):
        # TODO
        self.fail()

    def test__puppy(self):
        # TODO
        self.fail()

    def test__rabbit(self):
        # TODO
        self.fail()

    def test__sheep(self):
        # TODO
        self.fail()

    def test__snail(self):
        # TODO
        self.fail()

    def test__tropical_fish(self):
        # TODO
        self.fail()

    def test__turtle(self):
        # TODO
        self.fail()

    def test__whale(self):
        # TODO
        self.fail()
