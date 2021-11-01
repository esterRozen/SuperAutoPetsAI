from Core.Animals.baseClasses import Animal, Equipment
# base pack


class _Tier6(Animal):
    def __init__(self, atk, hp):
        super(_Tier6, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 6


class Cat(_Tier6):
    def __init__(self):
        super(Cat, self).__init__(4, 5)

    def trigger(self, name):
        if name == "buy food":
            return [69] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Dragon(_Tier6):
    def __init__(self):
        super(Dragon, self).__init__(6, 8)

    def trigger(self, name):
        if name == "buy t1 pet":
            return [70] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Fly(_Tier6):
    def __init__(self):
        super(Fly, self).__init__(2, 2)

    def trigger(self, name):
        if name == "friend faints":
            return [71] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Gorilla(_Tier6):
    def __init__(self):
        super(Gorilla, self).__init__(6, 6)

    def trigger(self, name):
        if name == "hurt":
            return [72] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Leopard(_Tier6):
    def __init__(self):
        super(Leopard, self).__init__(6, 4)

    def trigger(self, name):
        if name == "start battle":
            return [73] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Mammoth(_Tier6):
    def __init__(self):
        super(Mammoth, self).__init__(2, 6)

    def trigger(self, name):
        if name == "on faint":
            return [74] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Snake(_Tier6):
    def __init__(self):
        super(Snake, self).__init__(6, 6)

    def trigger(self, name):
        if name == "friend ahead attacks":
            return [77] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]


class Tiger(_Tier6):
    def __init__(self):
        super(Tiger, self).__init__(4, 3)

    def trigger(self, name):
        # how to make it trigger animal in front's ability twice
        if name == "start battle":
            return [78] + [self.equipment.trigger(name)]
        return [0] + [self.equipment.trigger(name)]
