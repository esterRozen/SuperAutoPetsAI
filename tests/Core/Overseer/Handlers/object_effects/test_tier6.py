from unittest import TestCase

from src.core.game_elements.abstract_elements import Unarmed, Empty
from src.core.game_elements.game_objects.animals import tier_6
from src.core.game_elements.game_objects.equipment import Coconut
from src.core.overseer.handlers.object_effects.tier6 import Tier6
from src.core.game_systems import ShopSystem, BattleSystem
from src.core.overseer import MessageAgent


class TestTier6(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        BattleSystem(self.agent)
        ShopSystem(self.agent)

    def test__boar(self):
        self.agent.summon(tier_6.Boar(), ("team", 0))

        Tier6.boar(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].atk == 10)
        self.assertTrue(self.agent.team[0].battle_atk == 12)
        self.assertTrue(self.agent.team[0].hp == 6)
        self.assertTrue(self.agent.team[0].battle_hp == 8)

        self.agent.team[0].xp = 2
        Tier6.boar(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].atk == 10)
        self.assertTrue(self.agent.team[0].battle_atk == 16)
        self.assertTrue(self.agent.team[0].hp == 6)
        self.assertTrue(self.agent.team[0].battle_hp == 12)

        self.agent.team[0].xp = 5
        Tier6.boar(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].atk == 10)
        self.assertTrue(self.agent.team[0].battle_atk == 22)
        self.assertTrue(self.agent.team[0].hp == 6)
        self.assertTrue(self.agent.team[0].battle_hp == 18)

    def test__cat(self):
        # TODO
        self.fail()

    def test__dragon(self):
        self.agent.summon(tier_6.Dragon(), ("team", 0))
        self.agent.summon(tier_6.Tyrannosaurus(), ("team", 1))
        self.agent.summon(tier_6.Leopard(), ("team", 2))
        self.agent.summon(tier_6.Octopus(), ("team", 4))

        Tier6.dragon(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 6)
        self.assertTrue(self.agent.team[0].battle_atk == 6)
        self.assertTrue(self.agent.team[0].hp == 8)
        self.assertTrue(self.agent.team[0].battle_hp == 8)

        self.assertTrue(self.agent.team[1].atk == 10)
        self.assertTrue(self.agent.team[1].battle_atk == 10)
        self.assertTrue(self.agent.team[1].hp == 5)
        self.assertTrue(self.agent.team[1].battle_hp == 5)

        self.assertTrue(self.agent.team[2].atk == 11)
        self.assertTrue(self.agent.team[2].battle_atk == 11)
        self.assertTrue(self.agent.team[2].hp == 5)
        self.assertTrue(self.agent.team[2].battle_hp == 5)

        self.assertTrue(self.agent.team[4].atk == 9)
        self.assertTrue(self.agent.team[4].battle_atk == 9)
        self.assertTrue(self.agent.team[4].hp == 9)
        self.assertTrue(self.agent.team[4].battle_hp == 9)

        self.agent.team[0].xp = 2
        Tier6.dragon(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 6)
        self.assertTrue(self.agent.team[0].battle_atk == 6)
        self.assertTrue(self.agent.team[0].hp == 8)
        self.assertTrue(self.agent.team[0].battle_hp == 8)

        self.assertTrue(self.agent.team[1].atk == 12)
        self.assertTrue(self.agent.team[1].battle_atk == 12)
        self.assertTrue(self.agent.team[1].hp == 7)
        self.assertTrue(self.agent.team[1].battle_hp == 7)

        self.assertTrue(self.agent.team[2].atk == 13)
        self.assertTrue(self.agent.team[2].battle_atk == 13)
        self.assertTrue(self.agent.team[2].hp == 7)
        self.assertTrue(self.agent.team[2].battle_hp == 7)

        self.assertTrue(self.agent.team[4].atk == 11)
        self.assertTrue(self.agent.team[4].battle_atk == 11)
        self.assertTrue(self.agent.team[4].hp == 11)
        self.assertTrue(self.agent.team[4].battle_hp == 11)

        self.agent.team[0].xp = 5
        Tier6.dragon(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 6)
        self.assertTrue(self.agent.team[0].battle_atk == 6)
        self.assertTrue(self.agent.team[0].hp == 8)
        self.assertTrue(self.agent.team[0].battle_hp == 8)

        self.assertTrue(self.agent.team[1].atk == 15)
        self.assertTrue(self.agent.team[1].battle_atk == 15)
        self.assertTrue(self.agent.team[1].hp == 10)
        self.assertTrue(self.agent.team[1].battle_hp == 10)

        self.assertTrue(self.agent.team[2].atk == 16)
        self.assertTrue(self.agent.team[2].battle_atk == 16)
        self.assertTrue(self.agent.team[2].hp == 10)
        self.assertTrue(self.agent.team[2].battle_hp == 10)

        self.assertTrue(self.agent.team[4].atk == 14)
        self.assertTrue(self.agent.team[4].battle_atk == 14)
        self.assertTrue(self.agent.team[4].hp == 14)
        self.assertTrue(self.agent.team[4].battle_hp == 14)

    def test__fly(self):
        self.agent.summon(tier_6.Fly(), ("team", 4))
        Tier6.fly(self.agent, ("team", 4), ("team", 0), fainted=tier_6.Octopus())
        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_atk == 4)
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 4)

        self.agent.team[4].xp = 2
        Tier6.fly(self.agent, ("team", 4), ("team", 1), fainted=tier_6.Octopus())
        self.assertTrue(self.agent.team[1].atk == 8)
        self.assertTrue(self.agent.team[1].battle_atk == 8)
        self.assertTrue(self.agent.team[1].hp == 8)
        self.assertTrue(self.agent.team[1].battle_hp == 8)

        self.agent.team[4].xp = 5
        Tier6.fly(self.agent, ("team", 4), ("team", 2), fainted=tier_6.Octopus())
        self.assertTrue(self.agent.team[2].atk == 12)
        self.assertTrue(self.agent.team[2].battle_atk == 12)
        self.assertTrue(self.agent.team[2].hp == 12)
        self.assertTrue(self.agent.team[2].battle_hp == 12)

    def test__gorilla(self):
        self.agent.summon(tier_6.Gorilla(), ("team", 0))

        self.assertTrue(isinstance(self.agent.team[0].held, Unarmed))
        Tier6.gorilla(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(isinstance(self.agent.team[0].held, Coconut))

    def test__leopard(self):
        self.agent.in_shop = False
        self.agent.summon(tier_6.Leopard(), ("team", 0))
        self.agent.summon(tier_6.Sauropod(), ("enemy", 0))

        Tier6.leopard(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.enemy[0].battle_hp == 7)

        self.agent.team[0].xp = 2
        Tier6.leopard(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.summon(tier_6.Sauropod(), ("enemy", 0))
        self.agent.team[0].xp = 5
        Tier6.leopard(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.summon(tier_6.Leopard(), ("enemy", 0))
        Tier6.leopard(self.agent, ("enemy", 0), ("enemy", 4))
        self.assertTrue(isinstance(self.agent.team[0], Empty))

    def test__mammoth(self):
        self.agent.summon(tier_6.Mammoth(), ("team", 0))
        self.agent.summon(tier_6.Leopard(), ("team", 1))
        self.agent.summon(tier_6.Sauropod(), ("team", 4))

        Tier6.mammoth(self.agent, ("team", 0), ("team", 3), fainted=self.agent.team[0])
        self.assertTrue(self.agent.team[1].atk == 12)
        self.assertTrue(self.agent.team[1].battle_atk == 12)
        self.assertTrue(self.agent.team[1].hp == 6)
        self.assertTrue(self.agent.team[1].battle_hp == 6)

        self.assertTrue(self.agent.team[4].atk == 6)
        self.assertTrue(self.agent.team[4].battle_atk == 6)
        self.assertTrue(self.agent.team[4].hp == 14)
        self.assertTrue(self.agent.team[4].battle_hp == 14)

        self.agent.team[0].xp = 2
        Tier6.mammoth(self.agent, ("team", 0), ("team", 3), fainted=self.agent.team[0])
        self.assertTrue(self.agent.team[1].atk == 16)
        self.assertTrue(self.agent.team[1].battle_atk == 16)
        self.assertTrue(self.agent.team[1].hp == 10)
        self.assertTrue(self.agent.team[1].battle_hp == 10)

        self.assertTrue(self.agent.team[4].atk == 10)
        self.assertTrue(self.agent.team[4].battle_atk == 10)
        self.assertTrue(self.agent.team[4].hp == 18)
        self.assertTrue(self.agent.team[4].battle_hp == 18)

        self.agent.team[0].xp = 5
        Tier6.mammoth(self.agent, ("team", 0), ("team", 3), fainted=self.agent.team[0])
        self.assertTrue(self.agent.team[1].atk == 22)
        self.assertTrue(self.agent.team[1].battle_atk == 22)
        self.assertTrue(self.agent.team[1].hp == 16)
        self.assertTrue(self.agent.team[1].battle_hp == 16)

        self.assertTrue(self.agent.team[4].atk == 16)
        self.assertTrue(self.agent.team[4].battle_atk == 16)
        self.assertTrue(self.agent.team[4].hp == 24)
        self.assertTrue(self.agent.team[4].battle_hp == 24)

    def test__octopus(self):
        self.agent.in_shop = False
        self.agent.summon(tier_6.Octopus(), ("team", 0))
        self.agent.summon(tier_6.Boar(), ("enemy", 0))

        Tier6.octopus(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.enemy[0].battle_hp == 3)

        self.agent.summon(tier_6.Tiger(), ("enemy", 0))
        Tier6.octopus(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))
        self.assertTrue(isinstance(self.agent.enemy[1], Empty))

        self.agent.summon(tier_6.Mammoth(), ("enemy", 0))
        self.agent.team[0].xp = 2
        Tier6.octopus(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.enemy[0].battle_hp == 4)

        self.agent.summon(tier_6.Octopus(), ("enemy", 0))
        Tier6.octopus(self.agent, ("enemy", 0), ("enemy", 4))
        self.assertTrue(self.agent.team[0].battle_hp == 5)

    def test__sauropod(self):
        Tier6.sauropod(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.gold == 11)

    def test__snake(self):
        self.agent.in_shop = False
        self.agent.summon(tier_6.Snake(), ("team", 1))
        self.agent.summon(tier_6.Octopus(), ("enemy", 0))

        Tier6.snake(self.agent, ("team", 1), ("team", 4))
        self.assertTrue(self.agent.enemy[0].battle_hp == 3)
        Tier6.snake(self.agent, ("team", 1), ("team", 4))

        self.agent.team[1].xp = 2
        self.agent.summon(tier_6.Sauropod(), ("enemy", 0))
        Tier6.snake(self.agent, ("team", 1), ("team", 4))
        self.assertTrue(self.agent.enemy[0].battle_hp == 2)
        Tier6.snake(self.agent, ("team", 1), ("team", 4))

        self.agent.summon(tier_6.Snake(), ("enemy", 0))
        Tier6.snake(self.agent, ("enemy", 0), ("enemy", 4))
        self.assertTrue(self.agent.team[1].battle_hp == 1)

    def test__tiger(self):
        # TODO
        self.fail()

    def test__tyrannosaurus(self):
        self.agent.gold = 2
        self.agent.summon(tier_6.Tyrannosaurus(), ("team", 0))
        self.agent.summon(tier_6.Mammoth(), ("team", 1))
        self.agent.summon(tier_6.Octopus(), ("team", 4))

        Tier6.tyrannosaurus(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 9)
        self.assertTrue(self.agent.team[0].battle_atk == 9)
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 4)

        self.assertTrue(self.agent.team[1].atk == 3)
        self.assertTrue(self.agent.team[1].battle_atk == 3)
        self.assertTrue(self.agent.team[1].hp == 10)
        self.assertTrue(self.agent.team[1].battle_hp == 10)

        self.agent.gold = 3
        Tier6.tyrannosaurus(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 9)
        self.assertTrue(self.agent.team[0].battle_atk == 9)
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 4)

        self.assertTrue(self.agent.team[1].atk == 5)
        self.assertTrue(self.agent.team[1].battle_atk == 5)
        self.assertTrue(self.agent.team[1].hp == 11)
        self.assertTrue(self.agent.team[1].battle_hp == 11)

        self.assertTrue(self.agent.team[4].atk == 10)
        self.assertTrue(self.agent.team[4].battle_atk == 10)
        self.assertTrue(self.agent.team[4].hp == 9)
        self.assertTrue(self.agent.team[4].battle_hp == 9)

        self.agent.team[0].xp = 2
        Tier6.tyrannosaurus(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 9)
        self.assertTrue(self.agent.team[0].battle_atk == 9)
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 4)

        self.assertTrue(self.agent.team[1].atk == 9)
        self.assertTrue(self.agent.team[1].battle_atk == 9)
        self.assertTrue(self.agent.team[1].hp == 13)
        self.assertTrue(self.agent.team[1].battle_hp == 13)

        self.assertTrue(self.agent.team[4].atk == 14)
        self.assertTrue(self.agent.team[4].battle_atk == 14)
        self.assertTrue(self.agent.team[4].hp == 11)
        self.assertTrue(self.agent.team[4].battle_hp == 11)

        self.agent.team[0].xp = 5
        Tier6.tyrannosaurus(self.agent, ("team", 0), ("team", 4))
        self.assertTrue(self.agent.team[0].atk == 9)
        self.assertTrue(self.agent.team[0].battle_atk == 9)
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 4)

        self.assertTrue(self.agent.team[1].atk == 15)
        self.assertTrue(self.agent.team[1].battle_atk == 15)
        self.assertTrue(self.agent.team[1].hp == 16)
        self.assertTrue(self.agent.team[1].battle_hp == 16)

        self.assertTrue(self.agent.team[4].atk == 20)
        self.assertTrue(self.agent.team[4].battle_atk == 20)
        self.assertTrue(self.agent.team[4].hp == 14)
        self.assertTrue(self.agent.team[4].battle_hp == 14)
