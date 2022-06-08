from ...abstract_elements import Animal
from .... import eventnames


# base pack
class _Tier1(Animal):
    def __init__(self, atk, hp):
        super(_Tier1, self).__init__(atk, hp)

    @property
    def tier(self):
        return 1


class Nop(_Tier1):
    def __init__(self):
        super().__init__(0, 0)
        return

    @property
    def tier(self):
        return 0

    def trigger(self, name: str) -> int:
        return 0


class Ant(_Tier1):
    id = 1

    def __init__(self):
        super(Ant, self).__init__(2, 1)

    def trigger(self, name):
        if name == eventnames.ON_FAINT:
            return self.id
        return 0


class Beaver(_Tier1):
    id = 2

    def __init__(self):
        super(Beaver, self).__init__(3, 2)

    def trigger(self, name):
        if name == eventnames.SELL:
            return self.id
        return 0


class Beetle(_Tier1):
    id = 3

    def __init__(self):
        super(Beetle, self).__init__(2, 3)

    def trigger(self, name):
        if name == eventnames.EAT_FOOD:
            return self.id
        return 0


class Bluebird(_Tier1):
    id = 4

    def __init__(self):
        super(Bluebird, self).__init__(2, 1)

    def trigger(self, name):
        if name == eventnames.END_TURN:
            return self.id
        return 0


class Cricket(_Tier1):
    id = 5

    def __init__(self):
        super(Cricket, self).__init__(1, 2)

    def trigger(self, name):
        if name == eventnames.ON_FAINT:
            return self.id
        return 0


class Duck(_Tier1):
    id = 6

    def __init__(self):
        super(Duck, self).__init__(2, 3)

    def trigger(self, name):
        if name == eventnames.SELL:
            return self.id
        return 0


class Fish(_Tier1):
    id = 7

    def __init__(self):
        super(Fish, self).__init__(2, 2)

    def trigger(self, name):
        if name == eventnames.ON_LEVEL:
            return self.id
        return 0


class Horse(_Tier1):
    id = 8

    def __init__(self):
        super(Horse, self).__init__(2, 1)

    def trigger(self, name):
        if name == eventnames.FRIEND_SUMMONED_BATTLE:
            return self.id
        return 0


class Ladybug(_Tier1):
    id = 9

    def __init__(self):
        super(Ladybug, self).__init__(1, 3)

    def trigger(self, name):
        if name == eventnames.BUY_FOOD:
            return self.id
        return 0


class Mosquito(_Tier1):
    id = 10

    def __init__(self):
        super(Mosquito, self).__init__(2, 2)

    def trigger(self, name):
        if name == eventnames.START_BATTLE:
            return self.id
        return 0


class Otter(_Tier1):
    id = 11

    def __init__(self):
        super(Otter, self).__init__(1, 2)

    def trigger(self, name):
        if name == eventnames.BUY:
            return self.id
        return 0


class Pig(_Tier1):
    id = 12

    def __init__(self):
        super(Pig, self).__init__(2, 2)

    def trigger(self, name):
        if name == eventnames.SELL:
            return self.id
        return 0


class Bee(_Tier1):
    rollable = False
    id = 0

    def __init__(self):
        super(Bee, self).__init__(1, 1)


class Sloth(_Tier1):
    rollable = False
    id = 0

    def __init__(self):
        super(Sloth, self).__init__(1, 1)


class Zombie_Cricket(_Tier1):
    rollable = False
    id = 0

    def __init__(self):
        super(Zombie_Cricket, self).__init__(1, 1)
