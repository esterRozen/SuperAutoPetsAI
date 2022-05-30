from unittest import TestCase

from src.core.game_elements.abstract_elements import Empty
from src.core.game_elements.game_objects.animals.tier_1 import Ant, Fish, Cricket
from src.core.overseer.baseagent import BaseAgent


class TestBaseAgent(TestCase):
    def test_backup(self):
        agent = BaseAgent("base pack")
        agent.team[0] = Fish()
        agent.team[1] = Ant()
        agent.team[2] = Fish()
        agent.team[3] = Fish()

        team = [agent.team[0], agent.team[1], agent.team[2], agent.team[3], Empty()]

        agent.team[1].permanent_buff(2, 2)
        agent.store_backup()

        agent.team[0] = Empty()
        agent.team[1] = Empty()
        agent.team[2] = Empty()
        agent.team[3] = Empty()
        for animal in agent.team.animals:
            self.assertTrue(isinstance(animal, Empty))

        agent.load_backup()
        for i, animal in enumerate(agent.team.animals):
            self.assertTrue(team[i] == animal)

    def test_reset_temp_stats(self):
        agent = BaseAgent("paid pack 1")
        agent.team[0] = Fish()
        agent.team[1] = Fish()
        agent.team[2] = Ant()
        agent.team[3] = Cricket()
        agent.team[4] = Ant()

        agent.team[0].temp_buff(2, 2)
        agent.team[1].temp_buff(3, 4)
        agent.team[2].temp_buff(3, 2)
        agent.team[3].temp_buff(5, 4)
        agent.team[4].temp_buff(3, 3)

        # fish 4/4
        self.assertTrue(agent.team[0].battle_atk == 4)
        self.assertTrue(agent.team[0].battle_hp == 4)
        # fish 5/6
        self.assertTrue(agent.team[1].battle_atk == 5)
        self.assertTrue(agent.team[1].battle_hp == 6)
        # ant 5/3
        self.assertTrue(agent.team[2].battle_atk == 5)
        self.assertTrue(agent.team[2].battle_hp == 3)
        # cricket 6/6
        self.assertTrue(agent.team[3].battle_atk == 6)
        self.assertTrue(agent.team[3].battle_hp == 6)
        # ant 5/4
        self.assertTrue(agent.team[4].battle_atk == 5)
        self.assertTrue(agent.team[4].battle_hp == 4)

        agent.reset_temp_stats()
        # fish 2/2
        self.assertTrue(agent.team[0].battle_atk == 2)
        self.assertTrue(agent.team[0].battle_hp == 2)
        self.assertTrue(agent.team[0].atk == 2)
        self.assertTrue(agent.team[0].hp == 2)
        # fish 2/2
        self.assertTrue(agent.team[1].battle_atk == 2)
        self.assertTrue(agent.team[1].battle_hp == 2)
        self.assertTrue(agent.team[1].atk == 2)
        self.assertTrue(agent.team[1].hp == 2)
        # ant 2/1
        self.assertTrue(agent.team[2].battle_atk == 2)
        self.assertTrue(agent.team[2].battle_hp == 1)
        self.assertTrue(agent.team[2].atk == 2)
        self.assertTrue(agent.team[2].hp == 1)
        # cricket 1/2
        self.assertTrue(agent.team[3].battle_atk == 1)
        self.assertTrue(agent.team[3].battle_hp == 2)
        self.assertTrue(agent.team[3].atk == 1)
        self.assertTrue(agent.team[3].hp == 2)
        # ant 2/1
        self.assertTrue(agent.team[4].battle_atk == 2)
        self.assertTrue(agent.team[4].battle_hp == 1)
        self.assertTrue(agent.team[4].atk == 2)
        self.assertTrue(agent.team[4].hp == 1)

    def test_ability(self):
        # TODO
        self.fail()

    def test_attack(self):
        # TODO
        self.fail()

    def test_buff(self):
        agent = BaseAgent("base pack")
        agent.in_shop = True

        agent.team[0] = Fish()
        agent.team[1] = Ant()

        agent.buff([agent.team[0], agent.team[1]], 4, 2)
        # fish 6/4, 6/4
        self.assertTrue(agent.team[0].atk == 6)
        self.assertTrue(agent.team[0].hp == 4)
        self.assertTrue(agent.team[0].battle_atk == 6)
        self.assertTrue(agent.team[0].battle_hp == 4)
        # ant 6/3, 6/3
        self.assertTrue(agent.team[1].atk == 6)
        self.assertTrue(agent.team[1].hp == 3)
        self.assertTrue(agent.team[1].battle_atk == 6)
        self.assertTrue(agent.team[1].battle_hp == 3)

        agent.buff(agent.team[0], 3, 2)
        # fish 9/6, 9/6
        self.assertTrue(agent.team[0].atk == 9)
        self.assertTrue(agent.team[0].hp == 6)
        self.assertTrue(agent.team[0].battle_atk == 9)
        self.assertTrue(agent.team[0].battle_hp == 6)

        agent.in_shop = False
        agent.buff([agent.team[0], agent.team[1]], 1, 2)
        # fish 9/6, 10/8
        self.assertTrue(agent.team[0].atk == 9)
        self.assertTrue(agent.team[0].hp == 6)
        self.assertTrue(agent.team[0].battle_atk == 10)
        self.assertTrue(agent.team[0].battle_hp == 8)
        # ant 6/3, 7/5
        self.assertTrue(agent.team[1].atk == 6)
        self.assertTrue(agent.team[1].hp == 3)
        self.assertTrue(agent.team[1].battle_atk == 7)
        self.assertTrue(agent.team[1].battle_hp == 5)

        agent.buff(agent.team[1], 2, 3)
        # ant 6/3, 9/8
        self.assertTrue(agent.team[1].atk == 6)
        self.assertTrue(agent.team[1].hp == 3)
        self.assertTrue(agent.team[1].battle_atk == 9)
        self.assertTrue(agent.team[1].battle_hp == 8)

    def test_damage(self):
        # TODO
        self.fail()

    def test_faint(self):
        agent = BaseAgent("base pack")

        self.fail()

    def test_summon(self):
        # TODO
        self.fail()
