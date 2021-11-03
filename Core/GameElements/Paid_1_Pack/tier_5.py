from Core.GameElements.simpleClasses import Animal


# paid_1 pack


class _Tier5(Animal):
    def __init__(self, atk, hp):
        super(_Tier5, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 5


class Chicken(_Tier5):
    def __init__(self):
        super(Chicken, self).__init__(3, 4)

    def trigger(self, name):
        if name == "buy t1 pet":
            return 57
        return 0


class Cow(_Tier5):
    def __init__(self):
        super(Cow, self).__init__(4, 6)

    def trigger(self, name):
        if name == "buy":
            return 58
        return 0


class Eagle(_Tier5):
    def __init__(self):
        super(Eagle, self).__init__(6, 5)

    def trigger(self, name):
        if name == "on faint":
            return 60
        return 0


class Goat(_Tier5):
    def __init__(self):
        super(Goat, self).__init__(4, 5)

    def trigger(self, name):
        if name == "friend bought":
            return 61
        return 0


class Microbe(_Tier5):
    def __init__(self):
        super(Microbe, self).__init__(1, 1)

    def trigger(self, name):
        if name == "on faint":
            return 62
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
