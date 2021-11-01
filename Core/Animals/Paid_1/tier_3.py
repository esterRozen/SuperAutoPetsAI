from Core.Animals.animal import Animal
# paid_1 pack


class Tier3(Animal):
    def __init__(self, atk, hp):
        super(Tier3, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 3


class Blowfish(Tier3):
    def __init__(self):
        super(Blowfish, self).__init__(3, 5)

    def trigger(self, name):
        if name == "hurt":
            return NotImplementedError
        return NotImplementedError


class Caterpillar(Tier3):
    def __init__(self):
        super(Caterpillar, self).__init__(1, 4)

    def trigger(self, name):
        if name == "start turn":
            return NotImplementedError
        return NotImplementedError


class HatchingChick(Tier3):
    def __init__(self):
        super(HatchingChick, self).__init__(1, 1)

    def trigger(self, name):
        if name == "end turn" and self.level < 3:
            return NotImplementedError
        elif name == "start turn" and self.level == 3:
            return NotImplementedError
        return NotImplementedError


class Owl(Tier3):
    def __init__(self):
        super(Owl, self).__init__(5, 3)

    def trigger(self, name):
        if name == "sell":
            return NotImplementedError
        return NotImplementedError


class Puppy(Tier3):
    def __init__(self):
        super(Puppy, self).__init__(1, 1)

    def trigger(self, name):
        if name == "end turn":
            return NotImplementedError
        return NotImplementedError


class Rabbit(Tier3):
    def __init__(self):
        super(Rabbit, self).__init__(3, 2)

    def trigger(self, name):
        if name == "friend eats food":
            return NotImplementedError
        return NotImplementedError


class Sheep(Tier3):
    def __init__(self):
        super(Sheep, self).__init__(2, 2)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Snail(Tier3):
    def __init__(self):
        super(Snail, self).__init__(2, 2)

    def trigger(self, name):
        if name == "buy":
            return NotImplementedError
        return NotImplementedError


class TropicalFish(Tier3):
    def __init__(self):
        super(TropicalFish, self).__init__(2, 4)

    def trigger(self, name):
        if name == "end turn":
            return NotImplementedError
        return NotImplementedError


class Turtle(Tier3):
    def __init__(self):
        super(Turtle, self).__init__(2, 4)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError
