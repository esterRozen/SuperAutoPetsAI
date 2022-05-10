from ...AbstractElements import Animal
from ....Overseer.Handlers.Items.eventnames import *
# base pack


class _Tier5(Animal):
    def __init__(self, atk, hp):
        super(_Tier5, self).__init__(atk, hp)

    @property
    def tier(self):
        return 5


class Cow(_Tier5):
    id = 58

    def __init__(self):
        super(Cow, self).__init__(4, 6)

    def trigger(self, name):
        if name == BUY:
            return self.id
        return 0


class Crocodile(_Tier5):
    id = 59

    def __init__(self):
        super(Crocodile, self).__init__(6, 3)

    def trigger(self, name):
        if name == START_BATTLE:
            return self.id
        return 0


class Monkey(_Tier5):
    id = 62

    def __init__(self):
        super(Monkey, self).__init__(3, 3)

    def trigger(self, name):
        if name == END_TURN:
            return self.id
        return 0


class Rhino(_Tier5):
    id = 64

    def __init__(self):
        super(Rhino, self).__init__(5, 6)

    def trigger(self, name):
        if name == KNOCK_OUT:
            return self.id
        return 0


class Scorpion(_Tier5):
    id = 65

    def __init__(self):
        super(Scorpion, self).__init__(1, 1)

    def trigger(self, name):
        return 0


class Seal(_Tier5):
    id = 66

    def __init__(self):
        super(Seal, self).__init__(3, 6)

    def trigger(self, name):
        if name == EAT_FOOD:
            return self.id
        return 0


class Shark(_Tier5):
    id = 67

    def __init__(self):
        super(Shark, self).__init__(4, 4)

    def trigger(self, name):
        if name == FRIEND_FAINTS:
            return self.id
        return 0


class Turkey(_Tier5):
    id = 68

    def __init__(self):
        super(Turkey, self).__init__(3, 4)

    def trigger(self, name):
        if name == FRIEND_SUMMONED_BATTLE or FRIEND_SUMMONED_SHOP:
            return self.id
        return 0
