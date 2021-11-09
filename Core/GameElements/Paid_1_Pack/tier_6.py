from Core.GameElements.SimpleClasses import Animal


# paid_1 pack


class _Tier6(Animal):
    def __init__(self, atk, hp):
        super(_Tier6, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 6


class Dragon(_Tier6):
    def __init__(self):
        super(Dragon, self).__init__(6, 8)

    def trigger(self, name):
        if name == "buy t1 pet":
            return 70
        return 0


class Gorilla(_Tier6):
    def __init__(self):
        super(Gorilla, self).__init__(6, 6)

    def trigger(self, name):
        if name == "hurt":
            return 72
        return 0


class Leopard(_Tier6):
    def __init__(self):
        super(Leopard, self).__init__(6, 4)

    def trigger(self, name):
        if name == "start battle":
            return 73
        return 0


class Mammoth(_Tier6):
    def __init__(self):
        super(Mammoth, self).__init__(2, 6)

    def trigger(self, name):
        if name == "on faint":
            return 74
        return 0


class Octopus(_Tier6):
    def __init__(self):
        super(Octopus, self).__init__(8, 8)

    def trigger(self, name):
        if self.level() == 3 and name == "before attack":
            return 75
        elif name == "on level":
            return 75
        return 0


class Sauropod(_Tier6):
    def __init__(self):
        super(Sauropod, self).__init__(4, 12)
        self.limit = 1

    def trigger(self, name):
        if name == "buy food":
            if self.limit < 0:
                return 0
            return 76
        elif name == "start turn":
            self.limit = self.level()
            return 0
        elif name == "on level":
            self.limit += 1
            return 0
        return 0


class Tyrannosaurus(_Tier6):
    def __init__(self):
        super(Tyrannosaurus, self).__init__(9, 4)

    def trigger(self, name):
        if name == "end turn":
            return 79
        return 0

