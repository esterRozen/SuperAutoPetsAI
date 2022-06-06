from unittest import TestCase

from src.core.game_elements.game_objects.animals import Fish, Ant, Beaver, Duck, Cricket, Otter
from src.core.overseer import MessageAgent


# testing the actual message handling as well as the other basic functions.
class TestMessageAgent(TestCase):
    def test_sorted_team(self):
        agent = MessageAgent("base pack")
        agent.team[0] = Fish()
        agent.team[0].permanent_buff(5, 5)
        agent.team[1] = Fish()
        agent.team[1].permanent_buff(4, 4)
        agent.team[2] = Fish()
        agent.team[2].permanent_buff(3, 3)
        agent.team[3] = Ant()
        agent.team[3].permanent_buff(4, 4)

        team_sort = agent.sorted_team()
        self.assertTrue(team_sort[0] == agent.team[0])
        self.assertTrue(team_sort[1] == agent.team[3])
        self.assertTrue(team_sort[2] == agent.team[1])
        self.assertTrue(team_sort[3] == agent.team[2])
        self.assertTrue(len(team_sort) == 4)

        # X 1 1 2 3 -> X 3 4 2 1
        agent.enemy[0] = Beaver()
        agent.enemy[1] = Duck()
        agent.enemy[2] = Cricket()
        agent.enemy[3] = Otter()

        team_sort = agent.sorted_team("enemy")
        self.assertTrue(team_sort[0] == agent.enemy[0])
        self.assertTrue(team_sort[1] == agent.enemy[1])
        self.assertTrue(team_sort[2] == agent.enemy[3])
        self.assertTrue(team_sort[3] == agent.enemy[2])
        self.assertTrue(len(team_sort) == 4)

    def test_sorted_without_(self):
        agent = MessageAgent("base pack")
        agent.team[0] = Fish()
        agent.team[0].permanent_buff(5, 5)
        agent.team[1] = Fish()
        agent.team[1].permanent_buff(4, 4)
        agent.team[2] = Fish()
        agent.team[2].permanent_buff(3, 3)
        agent.team[3] = Ant()
        agent.team[3].permanent_buff(4, 4)

        actor = ("team", 2)
        team_sort = agent.sorted_without_(actor)
        self.assertTrue(team_sort[0] == agent.team[0])
        self.assertTrue(team_sort[1] == agent.team[3])
        self.assertTrue(team_sort[2] == agent.team[1])
        self.assertTrue(len(team_sort) == 3)

        actor = ("team", 1)
        team_sort = agent.sorted_without_(actor)
        self.assertTrue(team_sort[0] == agent.team[0])
        self.assertTrue(team_sort[1] == agent.team[3])
        self.assertTrue(team_sort[2] == agent.team[2])
        self.assertTrue(len(team_sort) == 3)

        agent.team[4] = Fish()
        agent.team[4].permanent_buff(5, 5)
        actor = ("team", 0)
        team_sort = agent.sorted_without_(actor)

        self.assertTrue(id(team_sort[0]) == id(agent.team[4]))
        self.assertTrue(team_sort[1] == agent.team[3])
        self.assertTrue(team_sort[2] == agent.team[1])
        self.assertTrue(team_sort[3] == agent.team[2])
        self.assertTrue(len(team_sort) == 4)

        actor = ("team", 4)
        team_sort = agent.sorted_without_(actor)

        self.assertTrue(id(team_sort[0]) == id(agent.team[0]))
        self.assertTrue(team_sort[1] == agent.team[3])
        self.assertTrue(team_sort[2] == agent.team[1])
        self.assertTrue(team_sort[3] == agent.team[2])
        self.assertTrue(len(team_sort) == 4)

    def test_sorted_units_behind_(self):
        agent = MessageAgent("base pack")
        agent.team[0] = Fish()
        agent.team[0].permanent_buff(5, 5)
        agent.team[1] = Fish()
        agent.team[1].permanent_buff(4, 4)
        agent.team[2] = Fish()
        agent.team[2].permanent_buff(3, 3)
        agent.team[3] = Ant()
        agent.team[3].permanent_buff(4, 4)

        actor = ("team", 1)
        team_sort = agent.sorted_units_behind_(actor)
        self.assertTrue(team_sort[0] == agent.team[3])
        self.assertTrue(team_sort[1] == agent.team[2])
        self.assertTrue(len(team_sort) == 2)

        actor = ("team", 0)
        team_sort = agent.sorted_units_behind_(actor)
        self.assertTrue(team_sort[0] == agent.team[3])
        self.assertTrue(team_sort[1] == agent.team[1])
        self.assertTrue(team_sort[2] == agent.team[2])
        self.assertTrue(len(team_sort) == 3)

    def test_load(self):
        # TODO
        self.fail()

    def test_save(self):
        # TODO
        self.fail()

    def test_handle_events(self):
        # TODO
        self.fail()

    def test_trigger_ability(self):
        # TODO
        self.fail()

    def test_ability(self):
        # TODO
        self.fail()

    def test_attack(self):
        # TODO
        self.fail()

    def test_damage(self):
        # TODO
        self.fail()

    def test_faint(self):
        # TODO
        self.fail()

    def test_summon(self):
        # TODO
        self.fail()
