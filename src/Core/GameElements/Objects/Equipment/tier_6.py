from ...AbstractElements import Equipment


class _Tier6(Equipment):
    def __init__(self):
        super(_Tier6, self).__init__()

    @property
    def tier(self):
        return 6


class Melon(_Tier6):
    pass


class Mushroom(_Tier6):
    pass


class Pizza(_Tier6):
    pass


class Steak(_Tier6):
    pass
