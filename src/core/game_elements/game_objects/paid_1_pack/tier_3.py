from ...abstract_elements import Animal
from ....eventnames import *


# paid_1 pack


class _Tier3(Animal):
    def __init__(self, atk, hp):
        super(_Tier3, self).__init__(atk, hp)

    @property
    def tier(self):
        return 3


class Blowfish(_Tier3):
    id = 27

    def __init__(self):
        super(Blowfish, self).__init__(3, 5)

    def trigger(self, name):
        if name == HURT:
            return self.id
        return 0


class Butterfly(_Tier3):
    rollable = False
    id = 81

    def __init__(self):
        super(Butterfly, self).__init__(1, 1)

    def trigger(self, name):
        if name == IS_SUMMONED:
            return NotImplemented
        return 0


class Caterpillar(_Tier3):
    id = 29

    def __init__(self):
        super(Caterpillar, self).__init__(1, 4)

    def trigger(self, name):
        if name == START_TURN:
            return self.id
        return 0


class Dog(_Tier3):
    id = 30

    def __init__(self):
        super(Dog, self).__init__(2, 2)

    def trigger(self, name):
        if name == FRIEND_SUMMONED_BATTLE or FRIEND_SUMMONED_SHOP:
            return self.id
        return 0


class HatchingChick(_Tier3):
    id = 32

    def __init__(self):
        super(HatchingChick, self).__init__(1, 1)

    def trigger(self, name):
        if name == END_TURN and self.level < 3:
            return self.id
        elif name == START_TURN and self.level == 3:
            return self.id
        return 0


class Owl(_Tier3):
    id = 34

    def __init__(self):
        super(Owl, self).__init__(5, 3)

    def trigger(self, name):
        if name == SELL:
            return self.id
        return 0


class Puppy(_Tier3):
    id = 36

    def __init__(self):
        super(Puppy, self).__init__(1, 1)

    def trigger(self, name):
        if name == END_TURN:
            return self.id
        return 0


class Rabbit(_Tier3):
    id = 37

    def __init__(self):
        super(Rabbit, self).__init__(3, 2)

    def trigger(self, name):
        if name == FRIEND_EATS_FOOD:
            return self.id
        return 0


class Ram(_Tier3):
    rollable = False
    id = 0

    def __init__(self):
        super(Ram, self).__init__(2, 2)


class Sheep(_Tier3):
    id = 38

    def __init__(self):
        super(Sheep, self).__init__(2, 2)

    def trigger(self, name):
        if name == ON_FAINT:
            return self.id
        return 0


class Snail(_Tier3):
    id = 39

    def __init__(self):
        super(Snail, self).__init__(2, 2)

    def trigger(self, name):
        if name == BUY:
            return self.id
        return 0


class TropicalFish(_Tier3):
    id = 40

    def __init__(self):
        super(TropicalFish, self).__init__(2, 4)

    def trigger(self, name):
        if name == "end turn":
            return self.id
        return 0


class Turtle(_Tier3):
    id = 41

    def __init__(self):
        super(Turtle, self).__init__(2, 4)

    def trigger(self, name):
        if name == ON_FAINT:
            return self.id
        return 0
