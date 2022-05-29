from ...abstract_elements import Equipment


class _Tier1(Equipment):
    def __init__(self):
        super(_Tier1, self).__init__()

    @property
    def tier(self):
        return 1


class Apple(_Tier1):
    id = 400


class Honey(_Tier1):
    id = 401
