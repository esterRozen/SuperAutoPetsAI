from ...AbstractElements import Animal


# paid_1 pack


class _Tier2(Animal):
    def __init__(self, atk, hp):
        super(_Tier2, self).__init__(atk, hp)

    @staticmethod
    def tier():
        return 2


class Bat(_Tier2):
    def __init__(self):
        super(Bat, self).__init__(1, 2)

    def trigger(self, name):
        if name == "start battle":
            return 13
        return 0


class DirtyRat(_Tier2):
    def __init__(self):
        super(DirtyRat, self).__init__(1, 1)

    def trigger(self, name):
        if name == "next unit attacks":
            return NotImplemented
        return 0


class Dog(_Tier2):
    def __init__(self):
        super(Dog, self).__init__(2, 2)

    def trigger(self, name):
        if name == "friend summoned (battle)" or "friend summoned (shop)":
            return 16
        return 0


class Dromedary(_Tier2):
    def __init__(self):
        super(Dromedary, self).__init__(2, 4)

    def trigger(self, name):
        if name == "start turn":
            return 17
        return 0


class Flamingo(_Tier2):
    def __init__(self):
        super(Flamingo, self).__init__(3, 1)

    def trigger(self, name):
        if name == "on faint":
            return 19
        return 0


class Hedgehog(_Tier2):
    def __init__(self):
        super(Hedgehog, self).__init__(3, 2)

    def trigger(self, name):
        if name == "on faint":
            return 20
        return 0


class Peacock(_Tier2):
    def __init__(self):
        super(Peacock, self).__init__(1, 5)

    def trigger(self, name):
        if name == "hurt":
            return 21
        return 0


class Rat(_Tier2):
    def __init__(self):
        super(Rat, self).__init__(4, 5)

    def trigger(self, name):
        if name == "on faint":
            return 22
        return 0


class Shrimp(_Tier2):
    def __init__(self):
        super(Shrimp, self).__init__(2, 1)

    def trigger(self, name):
        if name == "friend sold":
            return 23
        return 0


class Spider(_Tier2):
    def __init__(self):
        super(Spider, self).__init__(2, 2)

    def trigger(self, name):
        if name == "on faint":
            return 24
        return 0


class Swan(_Tier2):
    def __init__(self):
        super(Swan, self).__init__(3, 4)

    def trigger(self, name):
        if name == "start turn":
            return 25
        return 0


class TabbyCat(_Tier2):
    def __init__(self):
        super(TabbyCat, self).__init__(4, 3)

    def trigger(self, name):
        if name == "eat food":
            return 26
        return 0
