from Core.Animals.animal import Animal
# base pack


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


class Cricket(Tier1):
    def __init__(self):
        super(Cricket, self).__init__(1, 2)

    def trigger(self, name):
        if name == "on faint":
            return NotImplementedError
        return NotImplementedError


class Duck(Tier1):
    def __init__(self):
        super(Duck, self).__init__(1, 2)

    def trigger(self, name):
        if name == "sell":
            return NotImplementedError
        return NotImplementedError


class Fish(Tier1):
    def __init__(self):
        super(Fish, self).__init__(2, 3)

    def trigger(self, name):
        if name == "on level":
            return NotImplementedError
        return NotImplementedError


class Horse(Tier1):
    def __init__(self):
        super(Horse, self).__init__(1, 1)

    def trigger(self, name):
        if name == "friend summoned (battle)":
            return NotImplementedError
        return NotImplementedError


class Otter(Tier1):
    def __init__(self):
        super(Otter, self).__init__(1, 2)

    def trigger(self, name):
        if name == "buy":
            return NotImplementedError
        return NotImplementedError
