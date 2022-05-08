from ...AbstractElements import Animal
# paid_1 pack


class _Tier6(Animal):
    def __init__(self, atk, hp):
        super(_Tier6, self).__init__(atk, hp)

    @property
    def tier(self):
        return 6


class Boar(_Tier6):
    id = 69

    def __init__(self):
        super(Boar, self).__init__(8, 6)

    def trigger(self, name):
        if name == "before attack":
            return self.id
        return


class Dragon(_Tier6):
    id = 71

    def __init__(self):
        super(Dragon, self).__init__(6, 8)

    def trigger(self, name):
        if name == "buy t1 pet":
            return self.id
        return 0


class Gorilla(_Tier6):
    id = 73

    def __init__(self):
        super(Gorilla, self).__init__(6, 6)

    def trigger(self, name):
        if name == "hurt":
            return self.id
        return 0


class Leopard(_Tier6):
    id = 74

    def __init__(self):
        super(Leopard, self).__init__(6, 4)

    def trigger(self, name):
        if name == "start battle":
            return self.id
        return 0


class Mammoth(_Tier6):
    id = 75

    def __init__(self):
        super(Mammoth, self).__init__(2, 6)

    def trigger(self, name):
        if name == "on faint":
            return self.id
        return 0


class Octopus(_Tier6):
    id = 76

    def __init__(self):
        super(Octopus, self).__init__(8, 8)

    def trigger(self, name):
        if self.level == 3 and name == "before attack":
            return self.id
        elif name == "on level":
            return self.id
        return 0


class Sauropod(_Tier6):
    id = 77

    def __init__(self):
        super(Sauropod, self).__init__(4, 12)
        self.limit = 1

    def trigger(self, name):
        if name == "buy food":
            if self.limit < 0:
                return 0
            return self.id
        elif name == "start turn":
            self.limit = self.level
            return 0
        elif name == "on level":
            self.limit += 1
            return 0
        return 0


class Tiger(_Tier6):
    id = 79

    def __init__(self):
        super(Tiger, self).__init__(4, 3)


class Tyrannosaurus(_Tier6):
    id = 80

    def __init__(self):
        super(Tyrannosaurus, self).__init__(9, 4)

    def trigger(self, name):
        if name == "end turn":
            return self.id
        return 0

