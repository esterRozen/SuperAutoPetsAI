import random
from typing import List, Optional, Dict

from . import Animal, Empty


# attacking animal is in position 0
class Team:
    def __init__(self):
        self.animals: List[Animal] = [Empty() for _ in range(5)]
        self.acting = 0
        self.__max_capacity = 5
        # random.seed(1)

    def __delitem__(self, key):
        self.animals[key] = Empty()

    def __getitem__(self, item: int) -> Animal:
        return self.animals[item]

    def __setitem__(self, idx: int, value: Animal):
        self.animals[idx] = value

    @property
    def has_lvl3(self) -> bool:
        for animal in self.animals:
            if animal.level == 3:
                return True
        return False

    @property
    def has_summon_space(self) -> bool:
        return self.size < self.__max_capacity

    @property
    def leftmost_unit(self) -> Optional[Animal]:
        if self.size == 0:
            return None

        i = len(self.animals)-1
        while isinstance(self.animals[i], Empty):
            i -= 1
        return self.animals[i]

    @property
    def level_of_actor(self) -> int:
        # level of currently acting team member
        return self.animals[self.acting].level

    @property
    def rightmost_unit(self) -> Optional[Animal]:
        if self.size == 0:
            return None
        i = 0
        while isinstance(self.animals[i], Empty):
            # TODO will probably have to make it check for battle hp?
            i += 1
        return self.animals[i]

    @property
    def second_unit(self) -> Optional[Animal]:
        if self.size <= 1:
            return None
        j = 0
        i = 0
        while j != 2 and i < self.__max_capacity:
            if not isinstance(self.animals[i], Empty):
                j += 1
            i += 1
        return self.animals[i - 1]

    @property
    def size(self) -> int:
        i = 0
        for animal in self.animals:
            if not isinstance(animal, Empty):
                i += 1
        return i

    def faint(self, event_raiser: int):
        """
        does not handle faint effects or held items that trigger on faint!
        Args:
            event_raiser:
        Returns:
        """
        self.animals[event_raiser] = Empty()

    def friends(self) -> Optional[List[Animal]]:
        a = list(range(0, 5))
        a.remove(self.acting)
        for i in a.copy():
            if isinstance(self.animals[i], Empty):
                a.remove(i)
        if not a:
            return None
        return [self.animals[i] for i in a]

    def friend_ahead(self) -> Optional[Animal]:
        for j in range(self.acting-1, -1, -1):
            if not isinstance(self.animals[j], Empty):
                return self.animals[j]
        return None

    def friends_ahead(self, n) -> Optional[List[Animal]]:
        ret = []
        i = 0
        for j in range(self.acting-1, -1, -1):
            if not isinstance(self.animals[j], Empty):
                if i < n:
                    ret += [self.animals[j]]
                    i += 1
        if not ret:
            return None
        return ret

    def friend_behind(self) -> Optional[Animal]:
        for j in range(self.acting+1, len(self.animals)):
            if not isinstance(self.animals[j], Empty):
                return self.animals[j]
        return None

    def friends_behind(self, n) -> Optional[List[Animal]]:
        ret = []
        i = 0
        for j in range(self.acting+1, len(self.animals)):
            if not isinstance(self.animals[j], Empty):
                if i < n:
                    ret += [self.animals[j]]
                    i += 1
        if not ret:
            return None
        return ret

    def lowest_health_unit(self):
        return min(self.animals, key=lambda animal: animal.battle_hp)

    def other_lvl2_or_3(self) -> Optional[List[Animal]]:
        a = list(range(0, 5))
        a.remove(self.acting)
        for i in a.copy():
            if self.animals[i].level == 1:
                a.remove(i)
        if not a:
            return None
        return [self.animals[i] for i in a]

    # TODO fix these to have None-case in event of no valid outputs
    def push_forward(self):
        # TODO push_forward
        return self

    def random_friend(self) -> Optional[Animal]:
        a = list(range(0, 5))
        a.remove(self.acting)
        for i in a.copy():
            if isinstance(self.animals[i], Empty):
                a.remove(i)
        if not a:
            return None
        return self.animals[random.choice(a)]

    def random_friends(self, n) -> Optional[List[Animal]]:
        a = list(range(0, 5))
        a.remove(self.acting)
        for i in a.copy():
            if isinstance(self.animals[i], Empty):
                a.remove(i)
        if not a:
            return None
        if len(a) < n:
            return [self.animals[i] for i in a]
        else:
            return random.sample([self.animals[i] for i in a], n)

    def random_unit(self) -> Optional[Animal]:
        if self.size == 0:
            return None

        a = list(range(0, 5))
        for i in a.copy():
            if isinstance(self.animals[i], Empty):
                a.remove(i)

        return self.animals[random.choice(a)]

    def random_units(self, n) -> Optional[List[Animal]]:
        if self.size == 0:
            return None

        a = list(range(0, 5))
        for i in a.copy():
            if isinstance(self.animals[i], Empty):
                a.remove(i)
        if not a:
            return []
        if len(a) <= n:
            return [self.animals[i] for i in a]
        else:
            return random.sample([self.animals[i] for i in a], n)

    def random_units_idx(self, n) -> Optional[List[int]]:
        a = list(range(0, 5))
        for i in a.copy():
            if isinstance(self.animals[i], Empty):
                a.remove(i)
        if not a:
            return None
        if len(a) <= n:
            return a
        else:
            return random.sample(a, n)

    def ret_diff_tiers(self) -> Optional[List[Animal]]:
        animals: Dict = {}
        for animal in self.animals:
            animals[animal.tier] = animal

        animals: List[Animal] = list(animals.values())
        if not animals:
            return None
        return animals

    def summon(self, animal, position):
        # TODO fix this
        if self.size == 5:
            return self
        # insert unit to that position, if there would be too many units, insert and delete excess.
        self.animals.insert(animal, position)
