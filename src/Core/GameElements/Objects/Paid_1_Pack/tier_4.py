from ...AbstractElements import Animal


# paid_1 pack


class _Tier4(Animal):
    def __init__(self, atk, hp):
        super(_Tier4, self).__init__(atk, hp)

    @property
    def tier(self):
        return 4


class Bison(_Tier4):
    id = 42

    def __init__(self):
        super(Bison, self).__init__(6, 6)

    def trigger(self, name):
        if name == "end turn":
            return self.id
        return 0


class Buffalo(_Tier4):
    id = 43

    def __init__(self):
        super(Buffalo, self).__init__(5, 5)

    def trigger(self, name):
        if name == "friend bought":
            return self.id
        return 0


class Bus(_Tier4):
    id = 0

    def __init__(self):
        super(Bus, self).__init__(5, 5)


class Chick(_Tier4):
    id = 0

    def __init__(self):
        super(Chick, self).__init__(1, 1)


class Deer(_Tier4):
    id = 44

    def __init__(self):
        super(Deer, self).__init__(1, 1)

    def trigger(self, name):
        if name == "on faint":
            return self.id
        return 0


class Dolphin(_Tier4):
    id = 45

    def __init__(self):
        super(Dolphin, self).__init__(4, 6)

    def trigger(self, name: str):
        if name == "start turn":
            return self.id
        return 0


class Llama(_Tier4):
    id = 47

    def __init__(self):
        super(Llama, self).__init__(2, 5)

    def trigger(self, name):
        if name == "end turn":
            return self.id
        return 0


class Lobster(_Tier4):
    id = 48

    def __init__(self):
        super(Lobster, self).__init__(3, 3)

    def trigger(self, name):
        if name == "friend summoned (shop)":
            return self.id
        return 0


class Microbe(_Tier4):
    id = 49

    def __init__(self):
        super(Microbe, self).__init__(1, 1)

    def trigger(self, name):
        if name == "faint":
            return self.id
        return 0


class Rooster(_Tier4):
    id = 52

    def __init__(self):
        super(Rooster, self).__init__(3, 3)

    def trigger(self, name):
        if name == "on faint":
            return self.id
        return 0


class Skunk(_Tier4):
    id = 53

    def __init__(self):
        super(Skunk, self).__init__(3, 5)

    def trigger(self, name):
        if name == "start battle":
            return self.id
        return 0


class Squirrel(_Tier4):
    id = 54

    def __init__(self):
        super(Squirrel, self).__init__(2, 2)

    def trigger(self, name):
        if name == "buy":
            return self.id
        return 0


class Worm(_Tier4):
    id = 56

    def __init__(self):
        super(Worm, self).__init__(1, 1)

    def trigger(self, name):
        if name == "eat food":
            return self.id
        return 0
