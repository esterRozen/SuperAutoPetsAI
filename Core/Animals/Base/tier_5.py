from Core.Animals.baseClasses import Animal, Equipment
# base pack


class _Tier5(Animal):
    def __init__(self, atk, hp):
        super(_Tier5, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 5


class Cow(_Tier5):
    def __init__(self):
        super(Cow, self).__init__(4, 6)

    def trigger(self, name):
        if name == "buy":
            return [58] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Crocodile(_Tier5):
    def __init__(self):
        super(Crocodile, self).__init__(6, 3)

    def trigger(self, name):
        if name == "start battle":
            return [59] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Parrot(_Tier5):
    def __init__(self):
        super(Parrot, self).__init__(3, 2)

    def trigger(self, name):
        if name == "end turn":
            return [63] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Rhino(_Tier5):
    def __init__(self):
        super(Rhino, self).__init__(5, 6)

    def trigger(self, name):
        if name == "knock out":
            return [64] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Scorpion(_Tier5):
    def __init__(self):
        super(Scorpion, self).__init__(1, 1)

    def trigger(self, name):
        return [0] + [self.equipment.trigger(name)]


class Seal(_Tier5):
    def __init__(self):
        super(Seal, self).__init__(3, 6)

    def trigger(self, name):
        if name == "eat food":
            return [66] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Shark(_Tier5):
    def __init__(self):
        super(Shark, self).__init__(4, 4)

    def trigger(self, name):
        if name == "friend faints":
            return [67] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Turkey(_Tier5):
    def __init__(self):
        super(Turkey, self).__init__(3, 4)

    def trigger(self, name):
        if name == "friend summoned (battle)" or "friend summoned (shop)":
            return [68] + [self.equipment.trigger(name)]
        return 0
