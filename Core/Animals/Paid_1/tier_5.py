from Core.Animals.animal import Animal
# paid_1 pack


class Tier5(Animal):
    def __init__(self, atk, hp):
        super(Tier5, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 5


class Chicken(Tier5):
    def __init__(self):
        super(Chicken, self).__init__(3, 4)

    def trigger(self, name):
        if name == "buy t1 pet":
            return NotImplementedError
        return NotImplementedError


class Cow(Tier5):
    def __init__(self):
        super(Cow, self).__init__(4, 6)


class Eagle(Tier5):
    def __init__(self):
        super(Eagle, self).__init__(6, 5)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Goat(Tier5):
    def __init__(self):
        super(Goat, self).__init__(4, 5)

    def trigger(self, name):
        if name == "friend bought":
            return NotImplementedError
        return NotImplementedError


class Microbe(Tier5):
    def __init__(self):
        super(Microbe, self).__init__(1, 1)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Rhino(Tier5):
    def __init__(self):
        super(Rhino, self).__init__(5, 6)

    def trigger(self, name):
        if name == "knock out":
            return NotImplementedError
        return NotImplementedError


class Scorpion(Tier5):
    def __init__(self):
        super(Scorpion, self).__init__(1, 1)


class Seal(Tier5):
    def __init__(self):
        super(Seal, self).__init__(3, 6)

    def trigger(self, name):
        if name == "eat food":
            return NotImplementedError
        return NotImplementedError
