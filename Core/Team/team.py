from typing import List

from Core.GameElements.simpleClasses import Animal, Equipment, Empty
import random


class Team:
    def __init__(self, roster: List[Animal], equipment: List[Equipment]):
        self.animals = roster
        self.equipment = equipment
        self.acting = 0

    def level(self):
        # level of currently acting team member
        return self.animals[self.acting].level()

    def random_friend(self):
        a: List[int] = list(range(0, 5))
        a.remove(self.acting)
        for i in a:
            if isinstance(self.animals[i], Empty):
                a.remove(i)
        if a == []:
            return None
        return self.animals[random.choice(a)]

    def friends(self):
        a: List[int] = list(range(0, 5))
        a.remove(self.acting)
        for i in a:
            if isinstance(self.animals[i], Empty):
                a.remove(i)
        return [self.animals[i] for i in a]

    def random_friends(self, n):
        a = list(range(0, 5))
        a.remove(self.acting)
        for i in a:
            if isinstance(self.animals[i], Empty):
                a.remove(i)
        if a == []:
            return []
        if len(a) < n:
            return [self.animals[i] for i in a]
        else:
            return random.sample([self.animals[i] for i in a], n)

    def random_unit(self):
        a = list(range(0, 5))
        for i in a:
            if isinstance(self.animals[i], Empty):
                a.remove(i)

        return self.animals[random.choice(list(range(0, 5)))]

    def random_units(self, n):
        a = list(range(0, 5))
        for i in a:
            if isinstance(self.animals[i], Empty):
                a.remove(i)
        if a == []:
            return []
        if len(a) < n:
            return [self.animals[i] for i in a]
        else:
            return random.sample([self.animals[i] for i in a], n)
