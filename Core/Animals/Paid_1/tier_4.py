from Core.Animals.animal import Animal
# paid_1 pack


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


class Buffalo(Tier4):
    def __init__(self):
        super(Buffalo, self).__init__(5, 5)

    def trigger(self, name):
        if name == "friend bought":
            return NotImplementedError
        return NotImplementedError


class Deer(Tier4):
    def __init__(self):
        super(Deer, self).__init__(1, 1)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Llama(Tier4):
    def __init__(self):
        super(Llama, self).__init__(2, 5)

    def trigger(self, name):
        if name == "end turn":
            return NotImplementedError
        return NotImplementedError


class Lobster(Tier4):
    def __init__(self):
        super(Lobster, self).__init__(3, 3)

    def trigger(self, name):
        if name == "friend summoned (shop)":
            return NotImplementedError
        return NotImplementedError


class Poodle(Tier4):
    def __init__(self):
        super(Poodle, self).__init__(4, 2)

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

    def trigger(self, name):
        if name == "eat food":
            return NotImplementedError
        return NotImplementedError
