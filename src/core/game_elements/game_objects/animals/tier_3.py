from ...abstract_elements import Animal
from .... import eventnames
# base pack


class _Tier3(Animal):
    def __init__(self, atk, hp):
        super(_Tier3, self).__init__(atk, hp)

    @property
    def tier(self):
        return 3


class Badger(_Tier3):
    id = 26

    def __init__(self):
        super(Badger, self).__init__(5, 3)

    def trigger(self, name):
        if name == eventnames.ON_FAINT:
            return self.id
        return 0


class Blowfish(_Tier3):
    id = 27

    def __init__(self):
        super(Blowfish, self).__init__(3, 5)

    def trigger(self, name):
        if name == eventnames.HURT:
            return self.id
        return 0


class Camel(_Tier3):
    id = 28

    def __init__(self):
        super(Camel, self).__init__(2, 6)

    def trigger(self, name):
        if name == eventnames.HURT:
            return self.id
        return 0


class Dog(_Tier3):
    id = 29

    def __init__(self):
        super(Dog, self).__init__(3, 3)

    def trigger(self, name):
        if name == eventnames.FRIEND_SUMMONED_BATTLE or name == eventnames.FRIEND_SUMMONED_SHOP:
            return self.id
        return 0


class Giraffe(_Tier3):
    id = 30

    def __init__(self):
        super(Giraffe, self).__init__(2, 4)

    def trigger(self, name):
        if name == eventnames.END_TURN:
            return self.id
        return 0


class Hatching_Chick(_Tier3):
    id = 31

    def __init__(self):
        super(Hatching_Chick, self).__init__(1, 1)

    def trigger(self, name):
        if name == eventnames.END_TURN and self.level < 3:
            return self.id
        elif name == eventnames.START_TURN and self.level == 3:
            return self.id
        return 0


class Kangaroo(_Tier3):
    id = 32

    def __init__(self):
        super(Kangaroo, self).__init__(1, 2)

    def trigger(self, name):
        if name == eventnames.FRIEND_AHEAD_ATTACKS:
            return self.id
        return 0


class Owl(_Tier3):
    id = 33

    def __init__(self):
        super(Owl, self).__init__(5, 3)

    def trigger(self, name):
        if name == eventnames.SELL:
            return self.id
        return 0


class Ox(_Tier3):
    id = 34

    def __init__(self):
        super(Ox, self).__init__(1, 3)

    def trigger(self, name):
        if name == eventnames.FRIEND_AHEAD_FAINTS:
            return self.id
        return 0


class Puppy(_Tier3):
    id = 35

    def __init__(self):
        super(Puppy, self).__init__(1, 1)

    def trigger(self, name):
        if name == eventnames.END_TURN:
            return self.id
        return 0


class Rabbit(_Tier3):
    id = 36

    def __init__(self):
        super(Rabbit, self).__init__(1, 2)

    def trigger(self, name):
        if name == eventnames.EAT_FOOD:
            return self.id
        if name == eventnames.FRIEND_EATS_FOOD:
            return self.id
        return 0


class Sheep(_Tier3):
    id = 37

    def __init__(self):
        super(Sheep, self).__init__(2, 2)

    def trigger(self, name):
        if name == eventnames.ON_FAINT:
            return self.id
        return 0


class Snail(_Tier3):
    id = 38

    def __init__(self):
        super(Snail, self).__init__(2, 2)

    def trigger(self, name):
        if name == eventnames.BUY:
            return self.id
        return 0


class Tropical_Fish(_Tier3):
    id = 39

    def __init__(self):
        super(Tropical_Fish, self).__init__(2, 4)

    def trigger(self, name):
        if name == "end turn":
            return self.id
        return 0


class Turtle(_Tier3):
    id = 40

    def __init__(self):
        super(Turtle, self).__init__(1, 2)

    def trigger(self, name):
        if name == eventnames.ON_FAINT:
            return self.id
        return 0


class Ram(_Tier3):
    rollable = False
    id = 85

    def __init__(self):
        super(Ram, self).__init__(2, 2)
