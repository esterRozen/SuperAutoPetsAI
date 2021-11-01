from Core.Animals.baseClasses import Animal, Equipment
# paid_1 pack


class _Tier3(Animal):
    def __init__(self, atk, hp):
        super(_Tier3, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 3


class Blowfish(_Tier3):
    def __init__(self):
        super(Blowfish, self).__init__(3, 5)

    def trigger(self, name):
        if name == "hurt":
            return [28] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Caterpillar(_Tier3):
    def __init__(self):
        super(Caterpillar, self).__init__(1, 4)

    def trigger(self, name):
        if name == "start turn":
            return [30] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class HatchingChick(_Tier3):
    def __init__(self):
        super(HatchingChick, self).__init__(1, 1)

    def trigger(self, name):
        if name == "end turn" and self.level < 3:
            return [32] + [self.equipment.trigger(name)]
        elif name == "start turn" and self.level == 3:
            return [32] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Owl(_Tier3):
    def __init__(self):
        super(Owl, self).__init__(5, 3)

    def trigger(self, name):
        if name == "sell":
            return [34] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Puppy(_Tier3):
    def __init__(self):
        super(Puppy, self).__init__(1, 1)

    def trigger(self, name):
        if name == "end turn":
            return [36] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Rabbit(_Tier3):
    def __init__(self):
        super(Rabbit, self).__init__(3, 2)

    def trigger(self, name):
        if name == "friend eats food":
            return [37] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Sheep(_Tier3):
    def __init__(self):
        super(Sheep, self).__init__(2, 2)

    def trigger(self, name):
        if name == "on faint":
            return [38] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Snail(_Tier3):
    def __init__(self):
        super(Snail, self).__init__(2, 2)

    def trigger(self, name):
        if name == "buy":
            return [39] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class TropicalFish(_Tier3):
    def __init__(self):
        super(TropicalFish, self).__init__(2, 4)

    def trigger(self, name):
        if name == "end turn":
            return [40] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Turtle(_Tier3):
    def __init__(self):
        super(Turtle, self).__init__(2, 4)

    def trigger(self, name):
        if name == "on faint":
            return [41] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]
