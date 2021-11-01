from Core.Animals.animal import Animal
# base pack


class Tier6(Animal):
    def __init__(self, atk, hp):
        super(Tier6, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 6


class Cat(Tier6):
    def __init__(self):
        super(Cat, self).__init__(4, 5)

    def trigger(self, name):
        if name == "buy food":
            return NotImplementedError
        return NotImplementedError


class Dragon(Tier6):
    def __init__(self):
        super(Dragon, self).__init__(6, 8)

    def trigger(self, name):
        if name == "buy t1 pet":
            return NotImplementedError
        return NotImplementedError


class Fly(Tier6):
    def __init__(self):
        super(Fly, self).__init__(2, 2)

    def trigger(self, name):
        if name == "friend faints":
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


class Snake(Tier6):
    def __init__(self):
        super(Snake, self).__init__(6, 6)

    def trigger(self, name):
        if name == "friend ahead attacks":
            return NotImplementedError
        return NotImplementedError


class Tiger(Tier6):
    def __init__(self):
        super(Tiger, self).__init__(4, 3)
