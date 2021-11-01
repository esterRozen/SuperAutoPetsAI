from Core.Animals.baseClasses import Animal, Equipment
# paid_1 pack


class _Tier1(Animal):
    def __init__(self, atk, hp):
        super(_Tier1, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 1


class Ant(_Tier1):
    def __init__(self):
        super(Ant, self).__init__(2, 1)

    def trigger(self, name):
        if name == "on faint":
            return [1] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Beaver(_Tier1):
    def __init__(self):
        super(Beaver, self).__init__(2, 2)

    def trigger(self, name):
        if name == "sell":
            return [2] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Beetle(_Tier1):
    def __init__(self):
        super(Beetle, self).__init__(2, 3)

    def trigger(self, name):
        if name == "eat food":
            return [3] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Bluebird(_Tier1):
    def __init__(self):
        super(Bluebird, self).__init__(2, 1)

    def trigger(self, name):
        if name == "end turn":
            return [4] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Cricket(_Tier1):
    def __init__(self):
        super(Cricket, self).__init__(1, 2)

    def trigger(self, name):
        if name == "on faint":
            return [5] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Fish(_Tier1):
    def __init__(self):
        super(Fish, self).__init__(2, 3)

    def trigger(self, name):
        if name == "on level":
            return [7] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Ladybug(_Tier1):
    def __init__(self):
        super(Ladybug, self).__init__(1, 3)

    def trigger(self, name):
        if name == "buy food":
            return [9] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Mosquito(_Tier1):
    def __init__(self):
        super(Mosquito, self).__init__(2, 2)

    def trigger(self, name):
        if name == "start battle":
            return [10] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Pig(_Tier1):
    def __init__(self):
        super(Pig, self).__init__(2, 2)

    def trigger(self, name):
        if name == "sell":
            return [12] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]
