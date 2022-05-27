from ...abstract_elements import Animal
from ....eventnames import *
# base pack


class _Tier4(Animal):
    def __init__(self, atk, hp):
        super(_Tier4, self).__init__(atk, hp)

    @property
    def tier(self):
        return 4


class Bison(_Tier4):
    id = 42

    def __init__(self):
        super(Bison, self).__init__(6, 6)

    def trigger(self, name):
        if name == END_TURN:
            return self.id
        return 0


class Deer(_Tier4):
    id = 44

    def __init__(self):
        super(Deer, self).__init__(1, 1)

    def trigger(self, name):
        if name == ON_FAINT:
            return self.id
        return 0


class Dolphin(_Tier4):
    id = 45

    def __init__(self):
        super(Dolphin, self).__init__(4, 6)

    def trigger(self, name):
        if name == START_BATTLE:
            return self.id
        return 0


class Hippo(_Tier4):
    id = 46

    def __init__(self):
        super(Hippo, self).__init__(4, 7)

    def trigger(self, name):
        if name == KNOCK_OUT:
            return self.id
        return 0


class Parrot(_Tier4):
    id = 50

    def __init__(self):
        super(Parrot, self).__init__(3, 2)

    def trigger(self, name):
        if name == END_TURN:
            return self.id
        return 0


class Penguin(_Tier4):
    id = 51

    def __init__(self):
        super(Penguin, self).__init__(1, 2)

    def trigger(self, name):
        if name == END_TURN:
            return self.id
        return 0


class Rooster(_Tier4):
    id = 52

    def __init__(self):
        super(Rooster, self).__init__(3, 3)

    def trigger(self, name):
        if name == ON_FAINT:
            return self.id
        return 0


class Skunk(_Tier4):
    id = 53

    def __init__(self):
        super(Skunk, self).__init__(3, 5)

    def trigger(self, name):
        if name == START_BATTLE:
            return self.id
        return 0


class Squirrel(_Tier4):
    id = 54

    def __init__(self):
        super(Squirrel, self).__init__(2, 2)

    def trigger(self, name):
        if name == START_TURN:
            return self.id
        return 0


class Whale(_Tier4):
    id = 55

    def __init__(self):
        super(Whale, self).__init__(2, 6)

    def trigger(self, name):
        if name == START_BATTLE:
            return self.id
        return 0


class Worm(_Tier4):
    id = 56

    def __init__(self):
        super(Worm, self).__init__(1, 1)

    def trigger(self, name):
        if name == EAT_FOOD:
            return self.id
        return 0


class Bus(_Tier4):
    rollable = False
    id = 0

    def __init__(self):
        super(Bus, self).__init__(5, 5)


class Chick(_Tier4):
    rollable = False
    id = 0

    def __init__(self):
        super(Chick, self).__init__(1, 1)
