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
            self.team.animals[i].increase_xp(i + 1)
            self.assertTrue(self.team.level_of_actor(0) == 1, "actor shouldn't change")

        levels = [1, 2, 2, 2, 3]
        for i in range(5):
            self.assertTrue(self.team.level_of_actor(i) == levels[i], f"actor should be lvl {1 + (i + 2) // 3}")

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
        self.assertTrue(self.team.friends(2) == [self.team[0], self.team[1], self.team[3]])

        self.clean_start()
        self.team[0] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(3)
        self.assertTrue(self.team.friends(4) == [self.team[0]])

        self.clean_start()
        self.team[3] = self.spawner.spawn(5)
        self.assertTrue(self.team.friends(3) is None)

        self.clean_start()
        self.assertTrue(self.team.friends(0) is None, "should be none due as there are no units present")

    def test_friend_ahead(self):
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(4)

        self.assertTrue(self.team.friend_ahead(2) == self.team[0], "only unit ahead of position 2 is in position 0")

        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(5)

        self.assertTrue(self.team.friend_ahead(3) == self.team[2])

        self.clean_start()
        self.team[0] = self.spawner.spawn(5)

        self.assertTrue(self.team.friend_ahead(0) is None)

    def test_friends_ahead(self):
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(4)

        self.assertTrue(self.team.friends_ahead(2, 4) == [self.team[0]],
                        "only unit ahead of position 2 is in position 0")
        self.assertTrue(self.team.friends_ahead(0, 4) is None,
                        "front unit, no friend ahead of it")

        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(5)

        self.assertTrue(self.team.friends_ahead(3, 2) == [self.team[2], self.team[1]])
        self.assertTrue(self.team.friends_ahead(3, 4) == [self.team[2], self.team[1]])

        self.assertTrue(self.team.friends_ahead(4, 4) == [self.team[3], self.team[2], self.team[1]])

        self.clean_start()
        self.team[0] = self.spawner.spawn(5)

        self.assertTrue(self.team.friends_ahead(0, 1) is None)

    def test_friend_behind(self):
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(4)

        self.assertTrue(self.team.friend_behind(0) == self.team[2], "only unit ahead of position 2 is in position 0")

        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(5)

        self.assertTrue(self.team.friend_behind(3) == self.team[4])

        self.clean_start()
        self.team[0] = self.spawner.spawn(5)

        self.assertTrue(self.team.friend_behind(0) is None)

    def test_friends_behind(self):
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(4)

        self.assertTrue(self.team.friends_behind(2, 4) is None, "no units behind position 2")
        self.assertTrue(self.team.friends_behind(0, 4) == [self.team[2]], "1 unit behind position 0")

        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.team[2] = self.spawner.spawn(3)
        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(5)

        self.assertTrue(self.team.friends_behind(2, 4) == [self.team[3], self.team[4]])
        self.assertTrue(self.team.friends_behind(2, 1) == [self.team[3]])

        self.assertTrue(self.team.friends_behind(1, 4) == [self.team[2], self.team[3], self.team[4]])
        self.assertTrue(self.team.friends_behind(1, 1) == [self.team[2]])

        self.clean_start()
        self.team[0] = self.spawner.spawn(5)

        self.assertTrue(self.team.friends_behind(0, 1) is None)

    def test_make_summon_room_with_left_shift_at(self):
        self.clean_start()
        self.team[0] = self.spawner.spawn(3)
        self.team[1] = self.spawner.spawn(4)

        anims = [self.team[0], self.team[1]]
        self.team.make_summon_room_with_left_shift_at(0)
        self.assertTrue(self.team[2] == anims[1])
        self.assertTrue(self.team[1] == anims[0])
        self.assertTrue(isinstance(self.team[0], Empty))

        self.team[4] = self.spawner.spawn(5)
        anims.append(self.team[4])
        self.team.make_summon_room_with_left_shift_at(1)
        self.assertTrue(isinstance(self.team[0], Empty))
        self.assertTrue(isinstance(self.team[1], Empty))
        self.assertTrue(self.team[2] == anims[0])
        self.assertTrue(self.team[3] == anims[1])
        self.assertTrue(self.team[4] == anims[2])

        self.clean_start()
        self.team[1] = self.spawner.spawn(4)
        anims = self.team[1]
        self.team.make_summon_room_with_left_shift_at(0)
        self.assertTrue(isinstance(self.team[0], Empty))
        self.assertTrue(self.team[1] == anims)
        self.assertTrue(isinstance(self.team[2], Empty))

    def test_make_summon_room_with_right_shift_at(self):
        self.clean_start()
        self.team[1] = self.spawner.spawn(4)
        self.team[2] = self.spawner.spawn(5)
        anims = [self.team[1], self.team[2]]

        self.team.make_summon_room_with_right_shift_at(2)
        self.assertTrue(isinstance(self.team[2], Empty))
        self.assertTrue(self.team[1] == anims[1])
        self.assertTrue(self.team[0] == anims[0])

        self.team[3] = self.spawner.spawn(4)
        self.team[4] = self.spawner.spawn(6)
        anims.append(self.team[3])
        anims.append(self.team[4])

        self.team.make_summon_room_with_right_shift_at(4)
        self.assertTrue(self.team[0] == anims[0])
        self.assertTrue(self.team[1] == anims[1])
        self.assertTrue(self.team[2] == anims[2])
        self.assertTrue(self.team[3] == anims[3])
        self.assertTrue(isinstance(self.team[4], Empty))

        self.clean_start()
        self.team[1] = self.spawner.spawn(4)
        anims = self.team[1]
        self.team.make_summon_room_with_right_shift_at(2)
        self.assertTrue(isinstance(self.team[0], Empty))
        self.assertTrue(self.team[1] == anims)
        self.assertTrue(isinstance(self.team[2], Empty))

    def test_other_lvl2_or_3(self):
        self.clean_start()
        self.team[1] = self.spawner.spawn(5)
        self.assertTrue(self.team.other_lvl2_or_3(1) is None)

        self.team[1].xp = 5
        self.team[2] = self.spawner.spawn(3)
        self.assertTrue(self.team.other_lvl2_or_3(2) == [self.team[1]])

        self.team[0] = self.spawner.spawn(4)
        self.team[2].xp = 2
        self.assertTrue(self.team.other_lvl2_or_3(0) == [self.team[1], self.team[2]])

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
        friend = self.team.random_friend(2)
        self.assertTrue(friend is None, "shoud be no friends")

        self.team[3] = self.spawner.spawn(6)
        friend = self.team.random_friend(2)
        self.assertTrue(friend == self.team[3])

        self.team[0] = self.spawner.spawn(2)
        for _ in range(20):
            friend = self.team.random_friend(2)
            self.assertTrue(friend is not None)

        for _ in range(20):
            friend = self.team.random_friend(0)
            self.assertTrue(friend == self.team[2] or friend == self.team[3])

    def test_random_friends(self):
        self.clean_start()
        self.team[2] = self.spawner.spawn(5)
        friends = self.team.random_friends(2, 1)
        self.assertTrue(friends is None)

        self.team[3] = self.spawner.spawn(1)
        friends = self.team.random_friends(2, 1)
        self.assertTrue(self.team[3] == friends[0])

        self.team[4] = self.spawner.spawn(3)
        self.team[0] = self.spawner.spawn(4)
        for _ in range(10):
            friends = self.team.random_friends(2, 2)

            for friend in friends:
                self.assertTrue(friend != self.team[2])
                self.assertTrue(friend in self.team.animals)
                self.assertTrue(not isinstance(friend, Empty))

        for _ in range(10):
            friends = self.team.random_friends(0, 2)

            for friend in friends:
                self.assertTrue(friend != self.team[0])
                self.assertTrue(friend in self.team.animals)
                self.assertTrue(not isinstance(friend, Empty))

    def test_random_unit(self):
        self.clean_start()
        unit = self.team.random_unit()
        self.assertTrue(unit is None)

        self.team[2] = self.spawner.spawn(4)
        unit = self.team.random_unit()
        self.assertTrue(unit == self.team[2], f"guaranteed to be {self.team[2]}")

        self.team[3] = self.spawner.spawn(6)
        unit = self.team.random_unit()
        self.assertTrue(unit == self.team[3] or unit == self.team[2])

        self.team[0] = self.spawner.spawn(2)
        for _ in range(20):
            unit = self.team.random_unit()
            self.assertTrue(unit is not None)

        for _ in range(20):
            unit = self.team.random_unit()
            self.assertTrue(unit == self.team[2] or unit == self.team[3] or unit == self.team[0])

        self.team[1] = self.spawner.spawn(3)
        self.team[4] = self.spawner.spawn(2)

        for _ in range(20):
            unit = self.team.random_unit()
            self.assertTrue(unit in self.team.animals)

    def test_random_units(self):
        self.clean_start()
        units = self.team.random_units(2)
        self.assertTrue(units is None)

        self.team[3] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(5)
        units = self.team.random_units(2)

        self.assertTrue(self.team[2] in units)
        self.assertTrue(self.team[3] in units)
        self.assertTrue(len(units) == 2)

        self.team[0] = self.spawner.spawn(4)
        units = self.team.random_units(2)
        animals = [self.team[0], self.team[2], self.team[3]]
        for unit in units:
            self.assertTrue(unit in animals)
            self.assertTrue(unit is not None)

        self.team[1] = self.spawner.spawn(6)
        self.team[4] = self.spawner.spawn(4)

        units = self.team.random_units(4)
        for unit in units:
            self.assertTrue(unit in self.team.animals)
            self.assertTrue(unit is not None)

        units = self.team.random_units(5)
        for unit in units:
            self.assertTrue(unit in self.team.animals)
            self.assertTrue(unit is not None)

    def test_random_units_idx(self):
        self.clean_start()
        units = self.team.random_units_idx(2)
        self.assertTrue(units is None)

        self.team[3] = self.spawner.spawn(3)
        self.team[2] = self.spawner.spawn(5)
        units = self.team.random_units_idx(2)

        self.assertTrue(2 in units, "guaranteed present by picking 2 of 2")
        self.assertTrue(3 in units, "guaranteed present")
        self.assertTrue(len(units) == 2)

        self.team[0] = self.spawner.spawn(4)
        units = self.team.random_units_idx(2)
        animals = [0, 2, 3]
        for unit in units:
            self.assertTrue(unit in animals)
            self.assertTrue(unit is not None)

        self.team[1] = self.spawner.spawn(6)
        self.team[4] = self.spawner.spawn(4)

        units = self.team.random_units_idx(4)
        units_seen = []
        for unit in units:
            self.assertTrue(unit not in units_seen)
            units_seen.append(unit)
            self.assertTrue(unit in list(range(5)))
            self.assertTrue(unit is not None)

        units = self.team.random_units_idx(5)
        units_seen = []
        for unit in units:
            self.assertTrue(unit not in units_seen)
            units_seen.append(unit)
            self.assertTrue(unit in list(range(5)))
            self.assertTrue(unit is not None)

    def test_ret_diff_tiers(self):
        self.clean_start()
        self.team[4] = self.spawner.spawn_tier(3)
        self.team[2] = self.spawner.spawn_tier(3)
        self.team[3] = self.spawner.spawn_tier(5)
        self.team[1] = self.spawner.spawn_tier(1)
        self.team[0] = self.spawner.spawn_tier(5)

        units = self.team.ret_diff_tiers()
        animals = [self.team[4], self.team[3], self.team[1]]
        for unit in units:
            self.assertTrue(unit in animals)
            self.assertTrue(unit is not None)
        self.assertTrue(len(units) == 3)

        self.team[2] = self.spawner.spawn_tier(4)

        units = self.team.ret_diff_tiers()
        animals = [self.team[4], self.team[3], self.team[2], self.team[1]]
        for unit in units:
            self.assertTrue(unit in animals)
            self.assertTrue(unit is not None)
        self.assertTrue(len(units) == 4)

        self.clean_start()

        units = self.team.ret_diff_tiers()
        self.assertTrue(units is None)

        self.team[4] = self.spawner.spawn_tier(4)
        units = self.team.ret_diff_tiers()
        self.assertTrue(units[0] == self.team[4])

    def test_summon(self):
        self.clean_start()

        first = self.spawner.spawn(4)
        self.team[0] = first

        second = self.spawner.spawn(5)
        self.team.summon(second, 0)
        self.assertTrue(self.team[0] == second)
        self.assertTrue(self.team[1] == first)
        self.assertTrue(isinstance(self.team[2], Empty))
        self.assertTrue(isinstance(self.team[3], Empty))
        self.assertTrue(isinstance(self.team[4], Empty))

        third = self.spawner.spawn(6)
        self.team.summon(third, 3)
        self.assertTrue(self.team[0] == second)
        self.assertTrue(self.team[1] == first)
        self.assertTrue(isinstance(self.team[2], Empty))
        self.assertTrue(self.team[3] == third)
        self.assertTrue(isinstance(self.team[4], Empty))

        fourth = self.spawner.spawn(3)
        self.team.summon(fourth, 0)
        self.assertTrue(self.team[0] == fourth)
        self.assertTrue(self.team[1] == second)
        self.assertTrue(self.team[2] == first)
        self.assertTrue(self.team[3] == third)
        self.assertTrue(isinstance(self.team[4], Empty))

        fifth = self.spawner.spawn(2)
        self.team.summon(fifth, 3)
        self.assertTrue(self.team[0] == fourth)
        self.assertTrue(self.team[1] == second)
        self.assertTrue(self.team[2] == first)
        self.assertTrue(self.team[3] == fifth)
        self.assertTrue(self.team[4] == third)

        sixth = self.spawner.spawn(1)
        self.team.summon(sixth, 1)
        self.assertTrue(self.team[0] == fourth)
        self.assertTrue(self.team[1] == second)
        self.assertTrue(self.team[2] == first)
        self.assertTrue(self.team[3] == fifth)
        self.assertTrue(self.team[4] == third)

    def test_units(self):
        self.clean_start()
        units = self.team.units()
        self.assertTrue(units is None)

        self.team[3] = self.spawner.spawn(4)
        units = self.team.units()
        self.assertTrue(units[0] == self.team[3])
        self.assertTrue(units[0] is not None)

        self.team[4] = self.spawner.spawn(5)
        units = self.team.units()
        animals = [3, 4]
        for i, unit in enumerate(units):
            self.assertTrue(unit == self.team[animals[i]])
            self.assertTrue(unit is not None)

        self.team[1] = self.spawner.spawn(2)
        animals = [1, 3, 4]
        units = self.team.units()
        for i, unit in enumerate(units):
            self.assertTrue(unit == self.team[animals[i]])
            self.assertTrue(unit is not None)

        self.team[2] = self.spawner.spawn(4)
        animals = [1, 2, 3, 4]
        units = self.team.units()
        for i, unit in enumerate(units):
            self.assertTrue(unit == self.team[animals[i]])
            self.assertTrue(unit is not None)

        self.team[0] = self.spawner.spawn(6)
        animals = list(range(5))
        units = self.team.units()
        for i, unit in enumerate(units):
            self.assertTrue(unit == self.team[animals[i]])
            self.assertTrue(unit is not None)
