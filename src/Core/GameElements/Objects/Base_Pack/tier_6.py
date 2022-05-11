from ...AbstractElements import Animal
from ....eventnames import *
# base pack


class _Tier6(Animal):
    def __init__(self, atk, hp):
        super(_Tier6, self).__init__(atk, hp)

    @property
    def tier(self):
        return 6


class Boar(_Tier6):
    id = 69

    def __init__(self):
        super(Boar, self).__init__(8, 6)

    def trigger(self, name):
        if name == BEFORE_ATTACK:
            return self.id
        return 0


class Cat(_Tier6):
    id = 70

    def __init__(self):
        super(Cat, self).__init__(4, 5)

    def trigger(self, name):
        if name == BUY_FOOD:
            return self.id
        return 0


class Dragon(_Tier6):
    id = 71

    def __init__(self):
        super(Dragon, self).__init__(6, 8)

    def trigger(self, name):
        if name == BUY_T1_PET:
            return self.id
        return 0


class FlyFriend(_Tier6):
    id = 0

    def __init__(self):
        super(FlyFriend, self).__init__(2, 2)


class Fly(_Tier6):
    id = 72

    def __init__(self):
        super(Fly, self).__init__(2, 2)

    def trigger(self, name):
        if name == FRIEND_FAINTS:
            return self.id
        return 0


class Gorilla(_Tier6):
    id = 73

    def __init__(self):
        super(Gorilla, self).__init__(6, 6)

    def trigger(self, name):
        if name == HURT:
            return self.id
        return 0


class Leopard(_Tier6):
    id = 74

    def __init__(self):
        super(Leopard, self).__init__(6, 4)

    def trigger(self, name):
        if name == START_BATTLE:
            return self.id
        return 0


class Mammoth(_Tier6):
    id = 75

    def __init__(self):
        super(Mammoth, self).__init__(2, 6)

    def trigger(self, name):
        if name == ON_FAINT:
            return self.id
        return 0


class Snake(_Tier6):
    id = 78

    def __init__(self):
        super(Snake, self).__init__(6, 6)

    def trigger(self, name):
        if name == FRIEND_AHEAD_ATTACKS:
            return self.id
        return 0


class Tiger(_Tier6):
    id = 79

    def __init__(self):
        super(Tiger, self).__init__(4, 3)

    def trigger(self, name):
        # how to make it trigger animal in front's ability twice
        return self.id
