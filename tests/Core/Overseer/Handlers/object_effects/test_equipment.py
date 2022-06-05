from unittest import TestCase

from src.core.game_elements.abstract_elements import Empty, Animal
from src.core.game_elements.game_objects.animals import Bee, Fish, Cricket
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
        self.agent.summon(Bee(), ("team", 0))
        self.assertTrue(isinstance(self.agent.team[0], Bee))

        Equipment.sleeping_pill(self.agent, ("team", 0), ("team", 1))

        self.assertTrue(isinstance(self.agent.team[0], Empty))

    def test_salad_bowl(self):
        self.agent.summon(Bee(), ("team", 0))
        Equipment.salad_bowl(self.agent, ("team", 2), ("team", 2))

        self.assertTrue(self.agent.team[0].hp == 2)
        self.assertTrue(self.agent.team[0].atk == 2)
        self.assertTrue(self.agent.team[0].battle_hp == 2)
        self.assertTrue(self.agent.team[0].battle_atk == 2)

        self.agent.summon(Cricket(), ("team", 1))
        Equipment.salad_bowl(self.agent, ("team", 2), ("team", 2))

        self.assertTrue(self.agent.team[0].hp == 3)
        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].battle_hp == 3)
        self.assertTrue(self.agent.team[0].battle_atk == 3)

        self.assertTrue(self.agent.team[1].hp == 3)
        self.assertTrue(self.agent.team[1].atk == 2)
        self.assertTrue(self.agent.team[1].battle_hp == 3)
        self.assertTrue(self.agent.team[1].battle_atk == 2)

    def test_canned_food(self):
        Equipment.canned_food(self.agent, ("team", 2), ("team", 2))

        self.agent.shop.reroll()
        animal: Animal = self.agent.shop[0].item
        # noinspection PyArgumentList
        original = animal.__class__()

        self.assertTrue(animal.hp == original.hp + 1)
        self.assertTrue(animal.atk == original.atk + 2)
        self.assertTrue(animal.battle_hp == original.battle_hp + 1)
        self.assertTrue(animal.battle_atk == original.battle_atk + 2)

    def test_pear(self):
        self.agent.summon(Bee(), ("team", 0))
        Equipment.pear(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].hp == 3)
        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].battle_hp == 3)
        self.assertTrue(self.agent.team[0].battle_atk == 3)

    def test_best_milk(self):
        self.agent.summon(Bee(), ("team", 0))
        Equipment.best_milk(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].atk == 7)
        self.assertTrue(self.agent.team[0].battle_hp == 4)
        self.assertTrue(self.agent.team[0].battle_atk == 7)

    def test_better_milk(self):
        self.agent.summon(Bee(), ("team", 0))
        Equipment.better_milk(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].hp == 3)
        self.assertTrue(self.agent.team[0].atk == 5)
        self.assertTrue(self.agent.team[0].battle_hp == 3)
        self.assertTrue(self.agent.team[0].battle_atk == 5)

    def test_chocolate(self):
        self.agent.summon(Bee(), ("team", 0))
        Equipment.chocolate(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].xp == 1)
        self.assertTrue(self.agent.team[0].hp == 2)
        self.assertTrue(self.agent.team[0].atk == 2)
        self.assertTrue(self.agent.team[0].battle_hp == 2)
        self.assertTrue(self.agent.team[0].battle_atk == 2)

    def test_milk(self):
        self.agent.summon(Bee(), ("team", 0))
        Equipment.milk(self.agent, ("team", 0), ("team", 4))

        self.assertTrue(self.agent.team[0].hp == 2)
        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].battle_hp == 2)
        self.assertTrue(self.agent.team[0].battle_atk == 3)

    def test_sushi(self):
        self.agent.summon(Bee(), ("team", 0))
        Equipment.sushi(self.agent, ("team", 1), ("team", 2))

        self.assertTrue(self.agent.team[0].hp == 2)
        self.assertTrue(self.agent.team[0].atk == 2)
        self.assertTrue(self.agent.team[0].battle_hp == 2)
        self.assertTrue(self.agent.team[0].battle_atk == 2)

        self.agent.summon(Bee(), ("team", 2))
        Equipment.sushi(self.agent, ("team", 1), ("team", 3))
        self.assertTrue(self.agent.team[0].hp == 3)
        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].battle_hp == 3)
        self.assertTrue(self.agent.team[0].battle_atk == 3)

        self.assertTrue(self.agent.team[2].hp == 2)
        self.assertTrue(self.agent.team[2].atk == 2)
        self.assertTrue(self.agent.team[2].battle_hp == 2)
        self.assertTrue(self.agent.team[2].battle_atk == 2)

        self.agent.summon(Bee(), ("team", 4))
        Equipment.sushi(self.agent, ("team", 1), ("team", 3))
        self.assertTrue(self.agent.team[0].hp == 4)
        self.assertTrue(self.agent.team[0].atk == 4)
        self.assertTrue(self.agent.team[0].battle_hp == 4)
        self.assertTrue(self.agent.team[0].battle_atk == 4)

        self.assertTrue(self.agent.team[2].hp == 3)
        self.assertTrue(self.agent.team[2].atk == 3)
        self.assertTrue(self.agent.team[2].battle_hp == 3)
        self.assertTrue(self.agent.team[2].battle_atk == 3)

        self.assertTrue(self.agent.team[4].hp == 2)
        self.assertTrue(self.agent.team[4].atk == 2)
        self.assertTrue(self.agent.team[4].battle_hp == 2)
        self.assertTrue(self.agent.team[4].battle_atk == 2)

    def test_mushroom(self):
        animal = Fish()
        animal.increase_xp(3)

        Equipment.mushroom(self.agent, ("team", 0), ("team", 3), animal)

        self.assertTrue(self.agent.team[0].__class__.__name__ == "Fish")
        self.assertTrue(self.agent.team[0].atk == 1)
        self.assertTrue(self.agent.team[0].hp == 1)
        self.assertTrue(self.agent.team[0].battle_atk == 1)
        self.assertTrue(self.agent.team[0].battle_hp == 1)

        self.assertTrue(self.agent.team.size == 1)

    def test_pizza(self):
        self.agent.summon(Bee(), ("team", 1))
        Equipment.pizza(self.agent, ("team", 0), ("team", 2))

        self.assertTrue(self.agent.team[1].atk == 3)
        self.assertTrue(self.agent.team[1].hp == 3)
        self.assertTrue(self.agent.team[1].battle_atk == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 3)

        self.agent.summon(Bee(), ("team", 3))
        Equipment.pizza(self.agent, ("team", 0), ("team", 2))

        self.assertTrue(self.agent.team[1].atk == 5)
        self.assertTrue(self.agent.team[1].hp == 5)
        self.assertTrue(self.agent.team[1].battle_atk == 5)
        self.assertTrue(self.agent.team[1].battle_hp == 5)

        self.assertTrue(self.agent.team[3].atk == 3)
        self.assertTrue(self.agent.team[3].hp == 3)
        self.assertTrue(self.agent.team[3].battle_atk == 3)
        self.assertTrue(self.agent.team[3].battle_hp == 3)
