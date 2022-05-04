from ...AbstractElements import Equipment


class _Tier3(Equipment):
    def __init__(self):
        super(_Tier3, self).__init__()

    @property
    def tier(self):
        return 3


class Garlic(_Tier3):
    pass


class SaladBowl(_Tier3):
    pass
