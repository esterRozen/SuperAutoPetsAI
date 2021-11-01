from Core.Animals.baseClasses import Animal, Equipment
# base pack


class _Tier2(Animal):
    def __init__(self, atk, hp):
        super(_Tier2, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 2


class Crab(_Tier2):
    def __init__(self):
        super(Crab, self).__init__(3, 3)

    def trigger(self, name):
        if name == "start battle":
            return [14] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Dodo(_Tier2):
    def __init__(self):
        super(Dodo, self).__init__(1, 3)

    def trigger(self, name):
        if name == "start battle":
            return [15] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Dog(_Tier2):
    def __init__(self):
        super(Dog, self).__init__(2, 2)

    def trigger(self, name):
        if name == "friend summoned (battle)" or "friend summoned (shop)":
            return [16] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Elephant(_Tier2):
    def __init__(self):
        super(Elephant, self).__init__(3, 5)

    def trigger(self, name):
        if name == "before attack":
            return [18] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Flamingo(_Tier2):
    def __init__(self):
        super(Flamingo, self).__init__(3, 1)

    def trigger(self, name):
        if name == "on faint":
            return [19] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Hedgehog(_Tier2):
    def __init__(self):
        super(Hedgehog, self).__init__(3, 2)

    def trigger(self, name):
        if name == "on faint":
            return [20] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Peacock(_Tier2):
    def __init__(self):
        super(Peacock, self).__init__(1, 5)

    def trigger(self, name):
        if name == "hurt":
            return [21] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Rat(_Tier2):
    def __init__(self):
        super(Rat, self).__init__(4, 5)

    def trigger(self, name):
        if name == "on faint":
            return [22] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Shrimp(_Tier2):
    def __init__(self):
        super(Shrimp, self).__init__(2, 1)

    def trigger(self, name):
        if name == "friend sold":
            return [23] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Spider(_Tier2):
    def __init__(self):
        super(Spider, self).__init__(2, 2)

    def trigger(self, name):
        if name == "on faint":
            return [24] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Swan(_Tier2):
    def __init__(self):
        super(Swan, self).__init__(3, 4)

    def trigger(self, name):
        if name == "start turn":
            return [25] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]
