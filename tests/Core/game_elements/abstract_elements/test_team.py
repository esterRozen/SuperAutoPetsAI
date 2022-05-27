from unittest import TestCase
from src.core.game_elements.abstract_elements import (Team, Animal, Empty, Spawner)


class TestTeam(TestCase):
    spawner = Spawner("paid_1")
    team = Team()

    def clean_start(self, mode: str = "base"):
        self.spawner = Spawner(mode)
        self.team = Team()

    def test_has_lvl3(self):
        spawner = Spawner("paid_1")
        team = Team()
        for i in range(5):
            team.animals[i] = spawner.spawn(1)
            self.assertFalse(team.has_lvl3, "team should not have any level 3 units")

        team.animals[3].increase_xp(5)
        self.assertTrue(team.has_lvl3, "team should have a level 3")

    def test_leftmost_unit(self):
        self.clean_start()
        self.team[1] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(6)
        self.team[0] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(4)
        self.assertTrue(self.team.leftmost_unit == self.team[3])

        self.clean_start()
        self.team[0] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(3)
        self.assertTrue(self.team.leftmost_unit == self.team[4])

        self.clean_start()
        self.team[3] = self.spawner.spawn(5)
        self.assertTrue(self.team.leftmost_unit == self.team[3])

        self.clean_start()
        self.assertTrue(self.team.leftmost_unit is None, "should be none due as there are no units present")

    def test_level_of_actor(self):
        self.clean_start()
        for i in range(5):
            self.team.animals[i] = self.spawner.spawn(3)
            self.team.animals[i].increase_xp(i+1)
            self.assertTrue(self.team.level_of_actor == 1, "actor shouldn't change")

        levels = [1, 2, 2, 2, 3]
        for i in range(5):
            self.team.acting = i
            self.assertTrue(self.team.level_of_actor == levels[i], f"actor should be lvl {1+(i+2)//3}")

    def test_rightmost_unit(self):
        self.clean_start()
        self.team[1] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(6)
        self.team[4] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(4)
        self.assertTrue(self.team.rightmost_unit == self.team[1])

        self.clean_start()
        self.team[0] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(3)
        self.assertTrue(self.team.rightmost_unit == self.team[0])

        self.clean_start()
        self.team[3] = self.spawner.spawn(5)
        self.assertTrue(self.team.rightmost_unit == self.team[3])

        self.clean_start()
        self.assertTrue(self.team.rightmost_unit is None, "should be none due as there are no units present")

    def test_second_unit(self):
        self.clean_start()
        self.team[1] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(6)
        self.team[4] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(4)
        self.assertTrue(self.team.second_unit == self.team[2])

        self.clean_start()
        self.team[0] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(3)
        self.assertTrue(self.team.second_unit == self.team[4])

        self.clean_start()
        self.team[3] = self.spawner.spawn(5)
        self.assertTrue(self.team.second_unit is None, "should be none as there is only 1 unit")

        self.clean_start()
        self.assertTrue(self.team.rightmost_unit is None, "should be none due as there are no units present")

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

    def test_lowest_health(self):
        self.clean_start("paid_1")
        for i in range(5):
            self.team.animals[i] = self.spawner.spawn(4)
            if i != 3:
                self.team.animals[i].permanent_buff(15, 15)
        self.assertTrue(self.team.animals[3] == self.team.lowest_health_unit())

    #####################################

    def test_faint(self):
        self.fail()

    def test_friends(self):
        self.fail()

    def test_friend_ahead(self):
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(4)

        self.team.acting = 2
        self.assertTrue(self.team.friend_ahead() == self.team[0], "only unit ahead of position 2 is in position 0")

        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(5)

        self.team.acting = 3
        self.assertTrue(self.team.friend_ahead() == self.team[2])

        self.clean_start()
        self.team[0] = self.spawner.spawn(5)

        self.team.acting = 0
        self.assertTrue(self.team.friend_ahead() is None)

    def test_friends_ahead(self):
        self.fail()

    def test_friend_behind(self):
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(4)

        self.team.acting = 0
        self.assertTrue(self.team.friend_behind() == self.team[2], "only unit ahead of position 2 is in position 0")

        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(5)

        self.team.acting = 3
        self.assertTrue(self.team.friend_behind() == self.team[4])

        self.clean_start()
        self.team[0] = self.spawner.spawn(5)

        self.team.acting = 0
        self.assertTrue(self.team.friend_behind() is None)

    def test_friends_behind(self):
        self.fail()

    def test_other_lvl2_or_3(self):
        self.fail()

    def test_push_forward(self):
        self.fail("function not implemented")

    def test_random_friend(self):
        self.fail()

    def test_random_friends(self):
        self.fail()

    def test_random_unit(self):
        self.fail()

    def test_random_units(self):
        self.fail()

    def test_random_units_idx(self):
        self.fail()

    def test_ret_diff_tiers(self):
        self.fail()

    def test_summon(self):
        self.fail("function not implemented")
