from Core.Animals.baseClasses import Animal, Equipment
# base pack


class _Tier3(Animal):
    def __init__(self, atk, hp):
        super(_Tier3, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 3


class Badger(_Tier3):
    def __init__(self):
        super(Badger, self).__init__(5, 4)

    def trigger(self, name):
        if name == "on faint":
            return [27] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Blowfish(_Tier3):
    def __init__(self):
        super(Blowfish, self).__init__(3, 5)

    def trigger(self, name):
        if name == "hurt":
            return [28] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Camel(_Tier3):
    def __init__(self):
        super(Camel, self).__init__(2, 5)

    def trigger(self, name):
        if name == "hurt":
            return [29] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Giraffe(_Tier3):
    def __init__(self):
        super(Giraffe, self).__init__(1, 3)

    def trigger(self, name):
        if name == "end turn":
            return [31] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Kangaroo(_Tier3):
    def __init__(self):
        super(Kangaroo, self).__init__(2, 3)

    def trigger(self, name):
        if name == "friend ahead attacks":
            return [33] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Ox(_Tier3):
    def __init__(self):
        super(Ox, self).__init__(1, 4)

    def trigger(self, name):
        if name == "friend ahead faints":
            return [35] + [self.equipment.trigger(name)]
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


class Turtle(_Tier3):
    def __init__(self):
        super(Turtle, self).__init__(2, 4)

    def trigger(self, name):
        if name == "on faint":
            return [41] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Whale(_Tier3):
    def __init__(self):
        super(Whale, self).__init__(2, 6)

    def trigger(self, name):
        if name == "start battle":
            return [42] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]
