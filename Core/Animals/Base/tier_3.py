from Core.Animals.animal import Animal
# base pack


class Tier3(Animal):
    def __init__(self, atk, hp):
        super(Tier3, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 3


class Badger(Tier3):
    def __init__(self):
        super(Badger, self).__init__(5, 4)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Blowfish(Tier3):
    def __init__(self):
        super(Blowfish, self).__init__(3, 5)

    def trigger(self, name):
        if name == "hurt":
            return NotImplementedError
        return NotImplementedError


class Camel(Tier3):
    def __init__(self):
        super(Camel, self).__init__(2, 5)

    def trigger(self, name):
        if name == "hurt":
            return NotImplementedError
        return NotImplementedError


class Giraffe(Tier3):
    def __init__(self):
        super(Giraffe, self).__init__(1, 3)

    def trigger(self, name):
        if name == "end turn":
            return NotImplementedError
        return NotImplementedError


class Kangaroo(Tier3):
    def __init__(self):
        super(Kangaroo, self).__init__(2, 3)

    def trigger(self, name):
        if name == "friend ahead attacks":
            return NotImplementedError
        return NotImplementedError


class Ox(Tier3):
    def __init__(self):
        super(Ox, self).__init__(1, 4)

    def trigger(self, name):
        if name == "friend ahead faints":
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


class Turtle(Tier3):
    def __init__(self):
        super(Turtle, self).__init__(2, 4)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Whale(Tier3):
    def __init__(self):
        super(Whale, self).__init__(2, 6)

    def trigger(self, name):
        if name == "start battle":
            return NotImplementedError
        return NotImplementedError
