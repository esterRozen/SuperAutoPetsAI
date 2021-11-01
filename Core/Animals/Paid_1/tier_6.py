from Core.Animals.animal import Animal
# paid_1 pack


class Tier6(Animal):
    def __init__(self, atk, hp):
        super(Tier6, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 6


class Dragon(Tier6):
    def __init__(self):
        super(Dragon, self).__init__(6, 8)

    def trigger(self, name):
        if name == "buy t1 pet":
            return NotImplementedError
        return NotImplementedError


class Gorilla(Tier6):
    def __init__(self):
        super(Gorilla, self).__init__(6, 6)

    def trigger(self, name):
        if name == "hurt":
            return NotImplementedError
        return NotImplementedError


class Leopard(Tier6):
    def __init__(self):
        super(Leopard, self).__init__(6, 4)

    def trigger(self, name):
        if name == "start battle":
            return NotImplementedError
        return NotImplementedError


class Mammoth(Tier6):
    def __init__(self):
        super(Mammoth, self).__init__(2, 6)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Octopus(Tier6):
    def __init__(self):
        super(Octopus, self).__init__(8, 8)

    def trigger(self, name):
        if self.level == 3 and name == "before attack":
            return NotImplementedError
        elif name == "on level":
            return NotImplementedError

        return NotImplementedError


class Sauropod(Tier6):
    def __init__(self):
        super(Sauropod, self).__init__(4, 12)

    def trigger(self, name):
        if name == "buy food":
            return NotImplementedError
        return NotImplementedError


class Tyrannosaurus(Tier6):
    def __init__(self):
        super(Tyrannosaurus, self).__init__(9, 4)

    def trigger(self, name):
        if name == "end turn":
            return NotImplementedError
        return NotImplementedError
