from unittest import TestCase
from src.core.game_elements.abstract_elements import (Team, Animal, Empty, Spawner)


class TestTeam(TestCase):
    spawner = Spawner("paid pack 1")
    team = Team()

    def clean_start(self, mode: str = "base pack"):
        self.spawner = Spawner(mode)
        self.team = Team()

    def test_has_lvl3(self):
        spawner = Spawner("paid pack 1")
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
        spawner = Spawner("paid pack 1")
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
        self.clean_start("paid pack 1")
        for i in range(5):
            self.team.animals[i] = self.spawner.spawn(4)
            if i != 3:
                self.team.animals[i].permanent_buff(15, 15)
        self.assertTrue(self.team.animals[3] == self.team.lowest_health_unit())

    #####################################

    def test_friends(self):
        self.clean_start()
        self.team[1] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(6)
        self.team[0] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(4)
        self.team.acting = 2
        self.assertTrue(self.team.friends() == [self.team[0], self.team[1], self.team[3]])

        self.clean_start()
        self.team[0] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(3)
        self.team.acting = 4
        self.assertTrue(self.team.friends() == [self.team[0]])

        self.clean_start()
        self.team[3] = self.spawner.spawn(5)
        self.team.acting = 3
        self.assertTrue(self.team.friends() is None)

        self.clean_start()
        self.assertTrue(self.team.friends() is None, "should be none due as there are no units present")

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
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(4)

        self.team.acting = 2
        self.assertTrue(self.team.friends_ahead(4) == [self.team[0]], "only unit ahead of position 2 is in position 0")
        self.team.acting = 0
        self.assertTrue(self.team.friends_ahead(4) is None, "front unit, no friend ahead of it")

        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(5)

        self.team.acting = 3
        self.assertTrue(self.team.friends_ahead(2) == [self.team[2], self.team[1]])
        self.assertTrue(self.team.friends_ahead(4) == [self.team[2], self.team[1]])

        self.team.acting = 4
        self.assertTrue(self.team.friends_ahead(4) == [self.team[3], self.team[2], self.team[1]])

        self.clean_start()
        self.team[0] = self.spawner.spawn(5)

        self.team.acting = 0
        self.assertTrue(self.team.friends_ahead(1) is None)

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
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(4)

        self.team.acting = 2
        self.assertTrue(self.team.friends_behind(4) is None, "no units behind position 2")
        self.team.acting = 0
        self.assertTrue(self.team.friends_behind(4) == [self.team[2]], "1 unit behind position 0")

        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(5)

        self.team.acting = 2
        self.assertTrue(self.team.friends_behind(4) == [self.team[3], self.team[4]])
        self.assertTrue(self.team.friends_behind(1) == [self.team[3]])

        self.team.acting = 1
        self.assertTrue(self.team.friends_behind(4) == [self.team[2], self.team[3], self.team[4]])
        self.assertTrue(self.team.friends_behind(1) == [self.team[2]])

        self.clean_start()
        self.team[0] = self.spawner.spawn(5)

        self.team.acting = 0
        self.assertTrue(self.team.friends_behind(1) is None)

    def test_other_lvl2_or_3(self):
        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team.acting = 1
        self.assertTrue(self.team.other_lvl2_or_3() is None)

        self.team[1].xp = 5
        self.team[2] = self.spawner.spawn(3)
        self.team.acting = 2
        self.assertTrue(self.team.other_lvl2_or_3() == [self.team[1]])

        self.team[0] = self.spawner.spawn(4)
        self.team.acting = 0
        self.team[2].xp = 2
        self.assertTrue(self.team.other_lvl2_or_3() == [self.team[1], self.team[2]])

    def test_push_forward(self):
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(4)
        animals = [self.team[0], self.team[2], Empty(), Empty(), Empty()]
        self.team.push_forward()

        for i in range(5):
            self.assertTrue(self.team[i] == animals[i], f"{self.team[i]} should be {animals[i]}")

        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(5)
        animals = [self.team[1], self.team[2], self.team[3], self.team[4], Empty()]
        self.team.push_forward()

        for i in range(5):
            self.assertTrue(self.team[i] == animals[i], f"{self.team[i]} should be {animals[i]}")

        self.clean_start()
        self.team[4] = self.spawner.spawn(4)
        animals = [self.team[4], Empty(), Empty(), Empty(), Empty()]
        self.team.push_forward()

        for i in range(5):
            self.assertTrue(self.team[i] == animals[i], f"{self.team[i]} should be {animals[i]}")

    def test_random_friend(self):
        self.clean_start()
        self.team[2] = self.spawner.spawn(4)
        self.team.acting = 2
        friend = self.team.random_friend()
        self.assertTrue(friend is None, "shoud be no friends")

        self.team[3] = self.spawner.spawn(6)
        friend = self.team.random_friend()
        self.assertTrue(friend == self.team[3])

        self.team[0] = self.spawner.spawn(2)
        for _ in range(20):
            friend = self.team.random_friend()
            self.assertTrue(friend is not None)

        self.team.acting = 0
        for _ in range(20):
            friend = self.team.random_friend()
            self.assertTrue(friend == self.team[2] or friend == self.team[3])

    def test_random_friends(self):
        # TODO
        self.fail()

    def test_random_unit(self):
        self.clean_start()
        unit = self.team.random_unit()
        self.assertTrue(unit is None)

        self.team[2] = self.spawner.spawn(4)
        self.team.acting = 2
        unit = self.team.random_unit()
        self.assertTrue(unit == self.team[2], f"guaranteed to be {self.team[2]}")

        self.team[3] = self.spawner.spawn(6)
        unit = self.team.random_unit()
        self.assertTrue(unit == self.team[3] or unit == self.team[2])

        self.team[0] = self.spawner.spawn(2)
        for _ in range(20):
            unit = self.team.random_unit()
            self.assertTrue(unit is not None)

        self.team.acting = 0
        for _ in range(20):
            unit = self.team.random_unit()
            self.assertTrue(unit == self.team[2] or unit == self.team[3] or unit == self.team[0])

        self.team[1] = self.spawner.spawn(3)
        self.team[4] = self.spawner.spawn(2)

        for _ in range(20):
            unit = self.team.random_unit()
            self.assertTrue(unit in self.team.animals)

    def test_random_units(self):
        # TODO
        self.fail()

    def test_random_units_idx(self):
        # TODO
        self.fail()

    def test_ret_diff_tiers(self):
        # TODO
        self.fail()

    def test_summon(self):
        # TODO
        self.fail()
