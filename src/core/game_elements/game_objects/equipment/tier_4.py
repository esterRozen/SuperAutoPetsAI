from ...abstract_elements import Equipment


class _Tier4(Equipment):
    def __init__(self):
        super(_Tier4, self).__init__()

    @property
    def tier(self):
        return 4


class CannedFood(_Tier4):
    pass


class Pear(_Tier4):
    pass
