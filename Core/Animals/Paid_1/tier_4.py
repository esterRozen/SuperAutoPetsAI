from Core.Animals.baseClasses import Animal, Equipment
# paid_1 pack


class _Tier4(Animal):
    def __init__(self, atk, hp):
        super(_Tier4, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 4


class Bison(_Tier4):
    def __init__(self):
        super(Bison, self).__init__(6, 6)

    def trigger(self, name):
        if name == "end turn":
            return [43] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Buffalo(_Tier4):
    def __init__(self):
        super(Buffalo, self).__init__(5, 5)

    def trigger(self, name):
        if name == "friend bought":
            return [44] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Deer(_Tier4):
    def __init__(self):
        super(Deer, self).__init__(1, 1)

    def trigger(self, name):
        if name == "on faint":
            return [45] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Llama(_Tier4):
    def __init__(self):
        super(Llama, self).__init__(2, 5)

    def trigger(self, name):
        if name == "end turn":
            return [48] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Lobster(_Tier4):
    def __init__(self):
        super(Lobster, self).__init__(3, 3)

    def trigger(self, name):
        if name == "friend summoned (shop)":
            return [49] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Poodle(_Tier4):
    def __init__(self):
        super(Poodle, self).__init__(4, 2)

    def trigger(self, name):
        if name == "end turn":
            return [52] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Rooster(_Tier4):
    def __init__(self):
        super(Rooster, self).__init__(3, 3)

    def trigger(self, name):
        if name == "on faint":
            return [53] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Skunk(_Tier4):
    def __init__(self):
        super(Skunk, self).__init__(3, 5)

    def trigger(self, name):
        if name == "start battle":
            return [54] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Squirrel(_Tier4):
    def __init__(self):
        super(Squirrel, self).__init__(2, 2)

    def trigger(self, name):
        if name == "buy":
            return [55] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Worm(_Tier4):
    def __init__(self):
        super(Worm, self).__init__(1, 1)

    def trigger(self, name):
        if name == "eat food":
            return [56] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]
