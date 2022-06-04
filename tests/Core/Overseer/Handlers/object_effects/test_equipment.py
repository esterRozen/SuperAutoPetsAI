from unittest import TestCase

from src.core.game_elements.game_objects.animals import Bee, Fish
from src.core.game_systems import ShopSystem, BattleSystem
from src.core.overseer import MessageAgent

from src.core.overseer.handlers.object_effects.equipment import Equipment


class TestEquipment(TestCase):
    def setUp(self):
        self.agent = MessageAgent("base pack")
        ShopSystem(self.agent)
        BattleSystem(self.agent)

    def test_apple(self):
        agent = MessageAgent("base pack")
        ShopSystem(agent)
        BattleSystem(agent)

        agent.summon(Bee(), ("team", 0))

        Equipment.apple(agent, ("team", 0), ("team", 1))

        self.assertTrue(agent.team[0].atk == 2)
        self.assertTrue(agent.team[0].hp == 2)
        self.assertTrue(agent.team[0].battle_hp == 2)
        self.assertTrue(agent.team[0].battle_atk == 2)

    def test_honey(self):
        Equipment.honey(self.agent, ("team", 0), ("team", 1), Fish())
        self.assertTrue(isinstance(self.agent.team[0], Bee))

    def test_cupcake(self):
        self.agent.summon(Bee(), ("team", 0))
        Equipment.cupcake(self.agent, ("team", 0), ("team", 1))

        self.assertTrue(self.agent.team[0].battle_hp == 4)
        self.assertTrue(self.agent.team[0].battle_atk == 4)
        self.assertTrue(self.agent.team[0].hp == 1)
        self.assertTrue(self.agent.team[0].atk == 1)

        self.agent.reset_temp_stats()

        self.assertTrue(self.agent.team[0].battle_hp == 1)
        self.assertTrue(self.agent.team[0].battle_atk == 1)
        self.assertTrue(self.agent.team[0].hp == 1)
        self.assertTrue(self.agent.team[0].atk == 1)

    def test_sleeping_pill(self):
        # TODO
        self.fail()

    def test_salad_bowl(self):
        # TODO
        self.fail()

    def test_canned_food(self):
        # TODO
        self.fail()

    def test_pear(self):
        # TODO
        self.fail()

    def test_best_milk(self):
        # TODO
        self.fail()

    def test_better_milk(self):
        # TODO
        self.fail()

    def test_chocolate(self):
        # TODO
        self.fail()

    def test_milk(self):
        # TODO
        self.fail()

    def test_sushi(self):
        # TODO
        self.fail()

    def test_mushroom(self):
        # TODO
        self.fail()

    def test_pizza(self):
        # TODO
        self.fail()
