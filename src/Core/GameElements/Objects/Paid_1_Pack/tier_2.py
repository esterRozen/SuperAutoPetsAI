from ...AbstractElements import Animal
from ....Overseer.Handlers.Items.eventnames import *


# paid_1 pack


class _Tier2(Animal):
    def __init__(self, atk, hp):
        super(_Tier2, self).__init__(atk, hp)

    @property
    def tier(self):
        return 2


class Bat(_Tier2):
    id = 13

    def __init__(self):
        super(Bat, self).__init__(1, 2)

    def trigger(self, name):
        if name == START_BATTLE:
            return self.id
        return 0


class DirtyRat(_Tier2):
    id = 0

    def __init__(self):
        super(DirtyRat, self).__init__(1, 1)

    def trigger(self, name):
        if name == ENEMY_ATTACKS:
            # TODO figure this out
            return NotImplemented
        return 0


class Dromedary(_Tier2):
    id = 16

    def __init__(self):
        super(Dromedary, self).__init__(2, 4)

    def trigger(self, name):
        if name == START_TURN:
            return self.id
        return 0


class Flamingo(_Tier2):
    id = 18

    def __init__(self):
        super(Flamingo, self).__init__(3, 1)

    def trigger(self, name):
        if name == ON_FAINT:
            return self.id
        return 0


class Hedgehog(_Tier2):
    id = 19

    def __init__(self):
        super(Hedgehog, self).__init__(3, 2)

    def trigger(self, name):
        if name == ON_FAINT:
            return self.id
        return 0


class Peacock(_Tier2):
    id = 20

    def __init__(self):
        super(Peacock, self).__init__(1, 5)

    def trigger(self, name):
        if name == HURT:
            return self.id
        return 0


class Rat(_Tier2):
    id = 21

    def __init__(self):
        super(Rat, self).__init__(4, 5)

    def trigger(self, name):
        if name == ON_FAINT:
            return self.id
        return 0


class Shrimp(_Tier2):
    id = 22

    def __init__(self):
        super(Shrimp, self).__init__(2, 1)

    def trigger(self, name):
        if name == FRIEND_SOLD:
            return self.id
        return 0


class Spider(_Tier2):
    id = 23

    def __init__(self):
        super(Spider, self).__init__(2, 2)

    def trigger(self, name):
        if name == ON_FAINT:
            return self.id
        return 0


class Swan(_Tier2):
    id = 24

    def __init__(self):
        super(Swan, self).__init__(3, 4)

    def trigger(self, name):
        if name == START_TURN:
            return self.id
        return 0


class TabbyCat(_Tier2):
    id = 25

    def __init__(self):
        super(TabbyCat, self).__init__(4, 3)

    def trigger(self, name):
        if name == EAT_FOOD:
            return self.id
        return 0
