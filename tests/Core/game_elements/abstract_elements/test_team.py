from unittest import TestCase
from src.core.game_elements.abstract_elements import (Team, Animal, Unarmed, Empty, Equipment, Spawner)



class TestTeam(TestCase):
    spawner = Spawner("paid_1")
    team = Team()

    def clean_start(self, mode: str):
        self.spawner = Spawner(mode)
        self.team = Team()

    def test_size(self):
        spawner = Spawner("paid_1")
        team = Team()
        for i in range(5):
            team.animals[i]: Animal = spawner.spawn(1)
            self.assertTrue(team.size == i+1, f"team should have {i+1} animals on it")

        team.animals[2] = Empty()
        self.assertTrue(team.size == 4, f"team should have 4 units on it")

        team.animals[0] = Empty()
        self.assertTrue(team.size == 3, f"team should have 3 units on it")

        team.push_forward()
        self.assertTrue(team.size == 3, "team should still have 3 units on it")

    def test_has_lvl3(self):
        spawner = Spawner("paid_1")
        team = Team()
        for i in range(5):
            team.animals[i] = spawner.spawn(1)
            self.assertFalse(team.has_lvl3, "team should not have any level 3 units")

        team.animals[3].increase_xp(5)
        self.assertTrue(team.has_lvl3, "team should have a level 3")

    def test_level_of_actor(self):
        self.clean_start("base")
        for i in range(5):
            self.team.animals[i] = self.spawner.spawn(3)
            self.team.animals[i].increase_xp(i+1)
            self.assertTrue(self.team.level_of_actor == 1, "actor shouldn't change")

        levels = [1, 2, 2, 2, 3]
        for i in range(5):
            self.team.acting = i
            self.assertTrue(self.team.level_of_actor == levels[i], f"actor should be lvl {1+(i+2)//3}")

    def test_lowest_health(self):
        self.clean_start("paid_1")
        for i in range(5):
            self.team.animals[i] = self.spawner.spawn(4)
            if i != 3:
                self.team.animals[i].permanent_buff(15, 15)
        self.assertTrue(self.team.animals[3] == self.team.lowest_health())

    def test_ret_diff_tiers(self):
        self.fail("function not implemented")

    def test_faint(self):
        self.fail()

    def test_push_forward(self):
        self.fail("function not implemented")

    def test_summon(self):
        self.fail()

    def test_leftmost_unit(self):
        self.fail()

    def test_rightmost_unit(self):
        self.fail()

    def test_friend_ahead(self):
        self.fail()

    def test_other_lvl2_or_3(self):
        self.fail()

    def test_friends_ahead(self):
        self.fail()

    def test_friend_behind(self):
        self.fail()

    def test_friends_behind(self):
        self.fail()

    def test_random_friend(self):
        self.fail()

    def test_friends(self):
        self.fail()

    def test_random_friends(self):
        self.fail()

    def test_random_unit(self):
        self.fail()

    def test_random_units(self):
        self.fail()

    def test_random_units_idx(self):
        self.fail()

