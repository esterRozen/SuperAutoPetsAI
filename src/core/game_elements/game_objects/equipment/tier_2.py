from ...abstract_elements import Equipment


class _Tier2(Equipment):
    def __init__(self):
        super(_Tier2, self).__init__()

    @property
    def tier(self):
        return 2


class Cupcake(_Tier2):
    pass


class MeatBone(_Tier2):
    pass


class SleepingPill(_Tier2):
    cost = 1


class Weak(_Tier2):
    pass