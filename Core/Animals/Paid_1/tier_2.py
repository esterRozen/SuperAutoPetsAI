from Core.Animals.animal import Animal
# paid_1 pack


class Tier2(Animal):
    def __init__(self, atk, hp):
        super(Tier2, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 2


class Bat(Tier2):
    def __init__(self):
        super(Bat, self).__init__(1, 2)

    def trigger(self, name):
        if name == "start battle":
            return NotImplementedError
        return NotImplementedError


class Dog(Tier2):
    def __init__(self):
        super(Dog, self).__init__(2, 2)

    def trigger(self, name):
        if name == "friend summoned (battle)" or "friend summoned (shop)":
            return NotImplementedError
        return NotImplementedError


class Dromedary(Tier2):
    def __init__(self):
        super(Dromedary, self).__init__(2, 4)

    def trigger(self, name):
        if name == "start turn":
            return NotImplementedError
        return NotImplementedError


class Flamingo(Tier2):
    def __init__(self):
        super(Flamingo, self).__init__(3, 1)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Hedgehog(Tier2):
    def __init__(self):
        super(Hedgehog, self).__init__(3, 2)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Peacock(Tier2):
    def __init__(self):
        super(Peacock, self).__init__(1, 5)

    def trigger(self, name):
        if name == "hurt":
            return NotImplementedError
        return NotImplementedError


class Rat(Tier2):
    def __init__(self):
        super(Rat, self).__init__(4, 5)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Shrimp(Tier2):
    def __init__(self):
        super(Shrimp, self).__init__(2, 1)

    def trigger(self, name):
        if name == "friend sold":
            return NotImplementedError
        return NotImplementedError


class Spider(Tier2):
    def __init__(self):
        super(Spider, self).__init__(2, 2)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Swan(Tier2):
    def __init__(self):
        super(Swan, self).__init__(3, 4)

    def trigger(self, name):
        if name == "start turn":
            return NotImplementedError
        return NotImplementedError


class TabbyCat(Tier2):
    def __init__(self):
        super(TabbyCat, self).__init__(4, 3)

    def trigger(self, name):
        if name == "eat food":
            return NotImplementedError
        return NotImplementedError
