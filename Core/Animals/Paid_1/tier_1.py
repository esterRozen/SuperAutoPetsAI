from Core.Animals.animal import Animal
# paid_1 pack


class Tier1(Animal):
    def __init__(self, atk, hp):
        super(Tier1, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 1


class Ant(Tier1):
    def __init__(self):
        super(Ant, self).__init__(2, 1)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Beaver(Tier1):
    def __init__(self):
        super(Beaver, self).__init__(2, 2)

    def trigger(self, name):
        if name == "sell":
            return NotImplementedError
        return NotImplementedError


class Beetle(Tier1):
    def __init__(self):
        super(Beetle, self).__init__(2, 3)

    def trigger(self, name):
        if name == "eat food":
            return NotImplementedError
        return NotImplementedError


class Bluebird(Tier1):
    def __init__(self):
        super(Bluebird, self).__init__(2, 1)

    def trigger(self, name):
        if name == "end turn":
            return NotImplementedError
        return NotImplementedError


class Cricket(Tier1):
    def __init__(self):
        super(Cricket, self).__init__(1, 2)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Fish(Tier1):
    def __init__(self):
        super(Fish, self).__init__(2, 3)

    def trigger(self, name):
        if name == "on level":
            return NotImplementedError
        return NotImplementedError


class Ladybug(Tier1):
    def __init__(self):
        super(Ladybug, self).__init__(1, 3)

    def trigger(self, name):
        if name == "buy food":
            return NotImplementedError
        return NotImplementedError


class Mosquito(Tier1):
    def __init__(self):
        super(Mosquito, self).__init__(2, 2)

    def trigger(self, name):
        if name == "start battle":
            return NotImplementedError
        return NotImplementedError


class Pig(Tier1):
    def __init__(self):
        super(Pig, self).__init__(2, 2)

    def trigger(self, name):
        if name == "sell":
            return NotImplementedError
        return NotImplementedError
