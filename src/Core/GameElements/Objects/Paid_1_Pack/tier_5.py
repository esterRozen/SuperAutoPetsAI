from ...AbstractElements import Animal


# paid_1 pack


class _Tier5(Animal):
    def __init__(self, atk, hp):
        super(_Tier5, self).__init__(atk, hp)

    @property
    def tier(self):
        return 5


class Chicken(_Tier5):
    id = 57

    def __init__(self):
        super(Chicken, self).__init__(3, 4)

    def trigger(self, name):
        if name == "buy t1 pet":
            return self.id
        return 0


class Cow(_Tier5):
    id = 58

    def __init__(self):
        super(Cow, self).__init__(4, 6)

    def trigger(self, name):
        if name == "buy":
            return self.id
        return 0


class Eagle(_Tier5):
    id = 60

    def __init__(self):
        super(Eagle, self).__init__(6, 5)

    def trigger(self, name):
        if name == "on faint":
            return self.id
        return 0


class Goat(_Tier5):
    id = 61

    def __init__(self):
        super(Goat, self).__init__(4, 5)
        self.limit = 1

    def trigger(self, name):
        if name == "friend bought":
            self.limit -= 1
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


class Poodle(_Tier5):
    id = 63

    def __init__(self):
        super(Poodle, self).__init__(4, 2)

    def trigger(self, name):
        if name == "end turn":
            return self.id
        return 0


class Rhino(_Tier5):
    id = 64

    def __init__(self):
        super(Rhino, self).__init__(5, 6)

    def trigger(self, name):
        if name == "knock out":
            return self.id
        return 0


class Scorpion(_Tier5):
    id = 65

    def __init__(self):
        super(Scorpion, self).__init__(1, 1)

    def trigger(self, name):
        return 0


class Seal(_Tier5):
    id = 66

    def __init__(self):
        super(Seal, self).__init__(3, 6)

    def trigger(self, name):
        if name == "eat food":
            return self.id
        return 0
