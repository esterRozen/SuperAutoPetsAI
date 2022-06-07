from unittest import TestCase

from src.core.game_elements.abstract_elements import Empty
from src.core.game_elements.game_objects.animals import tier_3
from src.core.game_elements.game_objects.equipment import Melon
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
        self.agent.summon(tier_3.Camel(), ("team", 0))
        self.agent.summon(tier_3.Kangaroo(), ("team", 1))

        Tier3.camel(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[1].battle_hp == 4)
        self.assertTrue(self.agent.team[1].battle_atk == 3)

    def test__dog(self):
        self.agent.summon(tier_3.Dog(), ("team", 0))

        Tier3.dog(self.agent, ("team", 0), ("team", 1))

        self.assertTrue(self.agent.team[0].hp == 4 or self.agent.team[0].atk == 4)

    def test__giraffe(self):
        self.agent.summon(tier_3.Kangaroo(), ("team", 0))
        self.agent.summon(tier_3.Giraffe(), ("team", 1))

        Tier3.giraffe(self.agent, ("team", 1), ("team", 3))

        self.assertTrue(self.agent.team[0].hp == 3)
        self.assertTrue(self.agent.team[0].atk == 2)

    def test__hatching_chick(self):
        self.agent.summon(tier_3.Kangaroo(), ("team", 0))
        self.agent.summon(tier_3.Hatching_Chick(), ("team", 1))

        Tier3.hatching_chick(self.agent, ("team", 1), ("team", 2))

        self.assertTrue(self.agent.team[0].atk == 1)
        self.assertTrue(self.agent.team[0].battle_atk == 6)
        self.assertTrue(self.agent.team[0].hp == 2)
        self.assertTrue(self.agent.team[0].battle_hp == 7)

        self.agent.team[1].xp = 2
        Tier3.hatching_chick(self.agent, ("team", 1), ("team", 2))

        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].battle_atk == 8)
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 9)

        self.agent.team[1].xp = 5
        Tier3.hatching_chick(self.agent, ("team", 1), ("team", 2))

        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_atk == 9)
        self.assertTrue(self.agent.team[0].hp == 5)
        self.assertTrue(self.agent.team[0].battle_hp == 10)

        self.assertTrue(self.agent.team[0].xp == 1)

    def test__kangaroo(self):
        self.agent.summon(tier_3.Kangaroo(), ("team", 1))

        Tier3.kangaroo(self.agent, ("team", 1), ("team", 0))

        self.assertTrue(self.agent.team[1].battle_hp == 4)
        self.assertTrue(self.agent.team[1].battle_atk == 3)

    def test__owl(self):
        self.agent.summon(tier_3.Owl(), ("team", 0))
        self.agent.summon(tier_3.Kangaroo(), ("team", 1))

        Tier3.owl(self.agent, ("team", 0), ("team", 3))

        self.assertTrue(self.agent.team[1].atk == 3)
        self.assertTrue(self.agent.team[1].hp == 4)

    def test__ox(self):
        self.agent.summon(tier_3.Ox(), ("team", 0))

        Tier3.ox(self.agent, ("team", 0), ("team", 3), fainted=tier_3.Camel())

        self.assertTrue(self.agent.team[0].atk == 2)
        self.assertTrue(isinstance(self.agent.team[0].held, Melon))

    def test__puppy(self):
        self.agent.summon(tier_3.Puppy(), ("team", 0))

        Tier3.puppy(self.agent, ("team", 0), ("team", 3))

        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].hp == 3)

        self.agent.gold = 1

        Tier3.puppy(self.agent, ("team", 0), ("team", 3))

        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].hp == 3)

    def test__rabbit(self):
        self.agent.summon(tier_3.Rabbit(), ("team", 0))
        self.agent.summon(tier_3.Kangaroo(), ("team", 1))

        Tier3.rabbit(self.agent, ("team", 0), ("team", 1))
        self.assertTrue(self.agent.team[1].hp == 3)

        Tier3.rabbit(self.agent, ("team", 0), ("team", 0))
        self.assertTrue(self.agent.team[0].hp == 3)

    def test__sheep(self):
        sheep = tier_3.Sheep()

        Tier3.sheep(self.agent, ("team", 0), ("team", 3), fainted=sheep)
        self.assertTrue(isinstance(self.agent.team[0], tier_3.Ram))
        self.assertTrue(isinstance(self.agent.team[1], tier_3.Ram))

        self.agent.team[0].hp -= 1
        self.assertTrue(self.agent.team[0].hp == 1)
        self.assertTrue(self.agent.team[1].hp == 2)

    def test__snail(self):
        self.agent.summon(tier_3.Snail(), ("team", 0))
        self.agent.summon(tier_3.Kangaroo(), ("team", 1))

        Tier3.snail(self.agent, ("team", 0), ("team", 1))
        self.assertTrue(self.agent.team[1].atk == 1)
        self.assertTrue(self.agent.team[1].hp == 2)

        self.agent.battle_lost = True
        Tier3.snail(self.agent, ("team", 0), ("team", 1))
        self.assertTrue(self.agent.team[1].atk == 2)
        self.assertTrue(self.agent.team[1].hp == 3)

    def test__tropical_fish(self):
        self.agent.summon(tier_3.Kangaroo(), ("team", 0))
        self.agent.summon(tier_3.Tropical_Fish(), ("team", 1))

        Tier3.tropical_fish(self.agent, ("team", 1), ("team", 4))

        self.assertTrue(self.agent.team[0].hp == 3)
        self.assertTrue(self.agent.team[0].atk == 1)

        self.agent.summon(tier_3.Kangaroo(), ("team", 2))

        Tier3.tropical_fish(self.agent, ("team", 1), ("team", 4))
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].atk == 1)

        self.assertTrue(self.agent.team[2].hp == 3)
        self.assertTrue(self.agent.team[2].atk == 1)

    def test__turtle(self):
        turtle = tier_3.Turtle()

        self.agent.summon(tier_3.Kangaroo(), ("team", 1))
        self.agent.summon(tier_3.Kangaroo(), ("team", 2))

        Tier3.turtle(self.agent, ("team", 0), ("team", 4), fainted=turtle)
        self.assertTrue(isinstance(self.agent.team[1].held, Melon))

        turtle.xp = 2
        Tier3.turtle(self.agent, ("team", 0), ("team", 4), fainted=turtle)
        self.assertTrue(isinstance(self.agent.team[1].held, Melon))
        self.assertTrue(isinstance(self.agent.team[2].held, Melon))
