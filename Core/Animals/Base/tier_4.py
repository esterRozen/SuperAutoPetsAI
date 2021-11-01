from Core.Animals.animal import Animal
# base pack


class Tier4(Animal):
    def __init__(self, atk, hp):
        super(Tier4, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 4


class Bison(Tier4):
    def __init__(self):
        super(Bison, self).__init__(6, 6)

    def trigger(self, name):
        if name == "end turn":
            return NotImplementedError
        return NotImplementedError


class Deer(Tier4):
    def __init__(self):
        super(Deer, self).__init__(1, 1)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Dolphin(Tier4):
    def __init__(self):
        super(Dolphin, self).__init__(4, 6)

    def trigger(self, name):
        if name == "start battle":
            return NotImplementedError
        return NotImplementedError


class Hippo(Tier4):
    def __init__(self):
        super(Hippo, self).__init__(4, 7)

    def trigger(self, name):
        if name == "knock out":
            return NotImplementedError
        return NotImplementedError


class Monkey(Tier4):
    def __init__(self):
        super(Monkey, self).__init__(3, 3)

    def trigger(self, name):
        if name == "end turn":
            return NotImplementedError
        return NotImplementedError


class Penguin(Tier4):
    def __init__(self):
        super(Penguin, self).__init__(1, 2)

    def trigger(self, name):
        if name == "end turn":
            return NotImplementedError
        return NotImplementedError


class Rooster(Tier4):
    def __init__(self):
        super(Rooster, self).__init__(3, 3)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Skunk(Tier4):
    def __init__(self):
        super(Skunk, self).__init__(3, 5)

    def trigger(self, name):
        if name == "start battle":
            return NotImplementedError
        return NotImplementedError


class Squirrel(Tier4):
    def __init__(self):
        super(Squirrel, self).__init__(2, 2)

    def trigger(self, name):
        if name == "buy":
            return NotImplementedError
        return NotImplementedError


class Worm(Tier4):
    def __init__(self):
        super(Worm, self).__init__(1, 1)
