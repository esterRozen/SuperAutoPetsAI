from ...AbstractElements import Animal
# base pack


class _Tier5(Animal):
    def __init__(self, atk, hp):
        super(_Tier5, self).__init__(atk, hp)

    @property
    def tier(self):
        return 5


class Cow(_Tier5):
    def __init__(self):
        super(Cow, self).__init__(4, 6)

    def trigger(self, name):
        if name == "buy":
            return 58
        return 0


class Crocodile(_Tier5):
    def __init__(self):
        super(Crocodile, self).__init__(6, 3)

    def trigger(self, name):
        if name == "start battle":
            return 59
        return 0


class Monkey(_Tier5):
    def __init__(self):
        super(Monkey, self).__init__(3, 3)

    def trigger(self, name):
        if name == "end turn":
            return 50
        return 0


class Rhino(_Tier5):
    def __init__(self):
        super(Rhino, self).__init__(5, 6)

    def trigger(self, name):
        if name == "knock out":
            return 64
        return 0


class Scorpion(_Tier5):
    def __init__(self):
        super(Scorpion, self).__init__(1, 1)

    def trigger(self, name):
        return 0


class Seal(_Tier5):
    def __init__(self):
        super(Seal, self).__init__(3, 6)

    def trigger(self, name):
        if name == "eat food":
            return 66
        return 0


class Shark(_Tier5):
    def __init__(self):
        super(Shark, self).__init__(4, 4)

    def trigger(self, name):
        if name == "friend faints":
            return 67
        return 0


class Turkey(_Tier5):
    def __init__(self):
        super(Turkey, self).__init__(3, 4)

    def trigger(self, name):
        if name == "friend summoned (battle)" or "friend summoned (shop)":
            return 68
        return 0
