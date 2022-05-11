from ...AbstractElements import Animal
from ....eventnames import *
# base pack


class _Tier1(Animal):
    def __init__(self, atk, hp):
        super(_Tier1, self).__init__(atk, hp)

    @property
    def tier(self):
        return 1


class Ant(_Tier1):
    id = 1

    def __init__(self):
        super(Ant, self).__init__(2, 1)

    def trigger(self, name):
        if name == ON_FAINT:
            return 1
        return 0


class Beaver(_Tier1):
    id = 2

    def __init__(self):
        super(Beaver, self).__init__(2, 2)

    def trigger(self, name):
        if name == SELL:
            return 2
        return 0


class Bee(_Tier1):
    id = 0

    def __init__(self):
        super(Bee, self).__init__(1, 1)


class Cricket(_Tier1):
    id = 5

    def __init__(self):
        super(Cricket, self).__init__(1, 2)

    def trigger(self, name):
        if name == SELL:
            return 5
        return 0


class Duck(_Tier1):
    id = 6
    def __init__(self):
        super(Duck, self).__init__(1, 2)

    def trigger(self, name):
        if name == SELL:
            return 6
        return 0


class Fish(_Tier1):
    id = 7

    def __init__(self):
        super(Fish, self).__init__(2, 3)

    def trigger(self, name):
        if name == ON_LEVEL:
            return 7
        return 0


class Horse(_Tier1):
    id = 8

    def __init__(self):
        super(Horse, self).__init__(1, 1)

    def trigger(self, name):
        if name == FRIEND_SUMMONED_BATTLE:
            return 8
        return 0


class Mosquito(_Tier1):
    id = 10

    def __init__(self):
        super(Mosquito, self).__init__(2, 2)

    def trigger(self, name):
        if name == START_BATTLE:
            return 10
        return 0


class Otter(_Tier1):
    id = 11

    def __init__(self):
        super(Otter, self).__init__(1, 2)

    def trigger(self, name):
        if name == BUY:
            return 11
        return 0


class Pig(_Tier1):
    id = 12

    def __init__(self):
        super(Pig, self).__init__(2, 2)

    def trigger(self, name):
        if name == SELL:
            return 12
        return 0


class Sloth(_Tier1):
    id = 0

    def __init__(self):
        super(Sloth, self).__init__(1, 1)


class ZombieCricket(_Tier1):
    id = 0

    def __init__(self):
        super(ZombieCricket, self).__init__(1, 1)
