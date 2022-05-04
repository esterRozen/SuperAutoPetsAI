from Core.GameElements.AbstractElements.SimpleClasses import Animal
# base pack


class _Tier1(Animal):
    def __init__(self, atk, hp):
        super(_Tier1, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 1


class Ant(_Tier1):
    def __init__(self):
        super(Ant, self).__init__(2, 1)

    def trigger(self, name):
        if name == "on faint":
            return 1
        return 0


class Beaver(_Tier1):
    def __init__(self):
        super(Beaver, self).__init__(2, 2)

    def trigger(self, name):
        if name == "sell":
            return 2
        return 0


class Bee(_Tier1):
    def __init__(self):
        super(Bee, self).__init__(1, 1)


class Cricket(_Tier1):
    def __init__(self):
        super(Cricket, self).__init__(1, 2)

    def trigger(self, name):
        if name == "on faint":
            return 5
        return 0


class Duck(_Tier1):
    def __init__(self):
        super(Duck, self).__init__(1, 2)

    def trigger(self, name):
        if name == "sell":
            return 6
        return 0


class Fish(_Tier1):
    def __init__(self):
        super(Fish, self).__init__(2, 3)

    def trigger(self, name):
        if name == "on level":
            return 7
        return 0


class Horse(_Tier1):
    def __init__(self):
        super(Horse, self).__init__(1, 1)

    def trigger(self, name):
        if name == "friend summoned (battle)":
            return 8
        return 0


class Mosquito(_Tier1):
    def __init__(self):
        super(Mosquito, self).__init__(2, 2)

    def trigger(self, name):
        if name == "start battle":
            return 10
        return 0


class Otter(_Tier1):
    def __init__(self):
        super(Otter, self).__init__(1, 2)

    def trigger(self, name):
        if name == "buy":
            return 11
        return 0


class Pig(_Tier1):
    def __init__(self):
        super(Pig, self).__init__(2, 2)

    def trigger(self, name):
        if name == "sell":
            return 12
        return 0


class Sloth(_Tier1):
    def __init__(self):
        super(Sloth, self).__init__(1, 1)


class ZombieCricket(_Tier1):
    def __init__(self):
        super(ZombieCricket, self).__init__(1, 1)
