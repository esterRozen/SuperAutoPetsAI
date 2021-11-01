from Core.Animals.animal import Animal
# base pack


class Tier5(Animal):
    def __init__(self, atk, hp):
        super(Tier5, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 5


class Cow(Tier5):
    def __init__(self):
        super(Cow, self).__init__(4, 6)


class Crocodile(Tier5):
    def __init__(self):
        super(Crocodile, self).__init__(6, 3)

    def trigger(self, name):
        if name == "start battle":
            return NotImplementedError
        return NotImplementedError


class Parrot(Tier5):
    def __init__(self):
        super(Parrot, self).__init__(3, 2)

    def trigger(self, name):
        if name == "end turn":
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


class Shark(Tier5):
    def __init__(self):
        super(Shark, self).__init__(4, 4)

    def trigger(self, name):
        if name == "friend faints":
            return NotImplementedError
        return NotImplementedError


class Turkey(Tier5):
    def __init__(self):
        super(Turkey, self).__init__(3, 4)

    def trigger(self, name):
        if name == "friend summoned (battle)" or "friend summoned (shop)":
            return NotImplementedError
        return NotImplementedError
