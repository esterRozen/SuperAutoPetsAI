from typing import Optional, Callable

from ...abstract_elements import Animal
from .... import eventnames


# base pack


class _Tier4(Animal):
    def __init__(self, atk, hp):
        super(_Tier4, self).__init__(atk, hp)

    @property
    def tier(self):
        return 4


class Bison(_Tier4):
    id = 41

    def __init__(self):
        super(Bison, self).__init__(4, 4)

    def trigger(self, name):
        if name == eventnames.END_TURN:
            return self.id
        return 0


class Buffalo(_Tier4):
    id = 42

    def __init__(self):
        super(Buffalo, self).__init__(4, 4)

    def trigger(self, name):
        if name == eventnames.FRIEND_BOUGHT:
            return self.id
        return 0


class Caterpillar(_Tier4):
    id = 43

    def __init__(self):
        super(Caterpillar, self).__init__(2, 2)

    def trigger(self, name):
        if name == eventnames.START_TURN and self.level != 3:
            return self.id
        elif name == eventnames.START_BATTLE and self.level == 3:
            return self.id
        return 0


class Deer(_Tier4):
    id = 44

    def __init__(self):
        super(Deer, self).__init__(1, 1)

    def trigger(self, name):
        if name == eventnames.ON_FAINT:
            return self.id
        return 0


class Dolphin(_Tier4):
    id = 45

    def __init__(self):
        super(Dolphin, self).__init__(4, 6)

    def trigger(self, name):
        if name == eventnames.START_BATTLE:
            return self.id
        return 0


class Hippo(_Tier4):
    id = 46

    def __init__(self):
        super(Hippo, self).__init__(4, 7)

    def trigger(self, name):
        if name == eventnames.KNOCK_OUT:
            return self.id
        return 0


class Llama(_Tier4):
    id = 47

    def __init__(self):
        super(Llama, self).__init__(3, 6)

    def trigger(self, name):
        if name == eventnames.END_TURN:
            return self.id
        return 0


class Lobster(_Tier4):
    id = 48

    def __init__(self):
        super(Lobster, self).__init__(4, 5)

    def trigger(self, name):
        if name == eventnames.FRIEND_SUMMONED_SHOP:
            return self.id
        return 0


class Microbe(_Tier4):
    id = 49

    def __init__(self):
        super(Microbe, self).__init__(1, 1)

    def trigger(self, name):
        if name == eventnames.ON_FAINT:
            return self.id
        return 0


class Parrot(_Tier4):
    id = 50
    stored: Optional[Callable[[str], int]] = None
    locked: bool = True

    def __init__(self):
        super(Parrot, self).__init__(4, 2)

    def trigger(self, name):
        # start of shop turn, remove state
        if name == eventnames.BATTLE_END:
            self.locked = True
            self.stored = None
            return 0

        # maintain null state until the shop turn ends
        # then copy ability of unit ahead.
        elif name == eventnames.BEFORE_BATTLE:
            self.locked = False
            return self.id

        # do not allow anything to edit state during shop phase
        elif self.locked:
            return

        return self.stored(name)


class Penguin(_Tier4):
    id = 51

    def __init__(self):
        super(Penguin, self).__init__(1, 2)

    def trigger(self, name):
        if name == eventnames.END_TURN:
            return self.id
        return 0


class Rooster(_Tier4):
    id = 52

    def __init__(self):
        super(Rooster, self).__init__(5, 3)

    def trigger(self, name):
        if name == eventnames.ON_FAINT:
            return self.id
        return 0


class Skunk(_Tier4):
    id = 53

    def __init__(self):
        super(Skunk, self).__init__(3, 5)

    def trigger(self, name):
        if name == eventnames.START_BATTLE:
            return self.id
        return 0


class Squirrel(_Tier4):
    id = 54

    def __init__(self):
        super(Squirrel, self).__init__(2, 5)

    def trigger(self, name):
        if name == eventnames.START_TURN:
            return self.id
        return 0


class Whale(_Tier4):
    id = 55
    stored: Optional[Animal] = None

    def __init__(self):
        super(Whale, self).__init__(3, 8)

    def trigger(self, name):
        if name == eventnames.START_BATTLE:
            return self.id
        return 0


class Worm(_Tier4):
    id = 56

    def __init__(self):
        super(Worm, self).__init__(3, 3)

    def trigger(self, name):
        if name == eventnames.EAT_FOOD:
            return self.id
        return 0


class Bus(_Tier4):
    rollable = False
    id = 0

    def __init__(self):
        super(Bus, self).__init__(5, 5)


class Butterfly(_Tier4):
    rollable = False
    id = 81

    def __init__(self):
        super(Butterfly, self).__init__(1, 1)

    def trigger(self, name):
        if name == eventnames.IS_SUMMONED:
            return self.id
        return 0


class Chick(_Tier4):
    rollable = False
    id = 0

    def __init__(self):
        super(Chick, self).__init__(1, 1)
