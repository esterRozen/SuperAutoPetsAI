from ...AbstractElements import Equipment


class _Tier5(Equipment):
    def __init__(self):
        super(_Tier5, self).__init__()

    @property
    def tier(self):
        return 5


class Chili(_Tier5):
    pass


class Chocolate(_Tier5):
    pass


class Milk(_Tier5):
    cost = 0


class BetterMilk(_Tier5):
    cost = 0


class BestMilk(_Tier5):
    cost = 0
