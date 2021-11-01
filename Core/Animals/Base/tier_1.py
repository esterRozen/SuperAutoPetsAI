from Core.Animals.baseClasses import Animal
# base pack


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


class Cricket(_Tier1):
    def __init__(self):
        super(Cricket, self).__init__(1, 2)

    def trigger(self, name):
        if name == "on faint":
            return [5] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Duck(_Tier1):
    def __init__(self):
        super(Duck, self).__init__(1, 2)

    def trigger(self, name):
        if name == "sell":
            return [6] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Fish(_Tier1):
    def __init__(self):
        super(Fish, self).__init__(2, 3)

    def trigger(self, name):
        if name == "on level":
            return [7] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Horse(_Tier1):
    def __init__(self):
        super(Horse, self).__init__(1, 1)

    def trigger(self, name):
        if name == "friend summoned (battle)":
            return [8] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Otter(_Tier1):
    def __init__(self):
        super(Otter, self).__init__(1, 2)

    def trigger(self, name):
        if name == "buy":
            return [11] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]
