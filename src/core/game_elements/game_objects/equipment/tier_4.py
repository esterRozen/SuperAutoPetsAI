from ...abstract_elements import Equipment


class _Tier4(Equipment):
    def __init__(self):
        super(_Tier4, self).__init__()

    @property
    def tier(self):
        return 4


class Canned_Food(_Tier4):
    id = 408
    is_targeted = False


class Pear(_Tier4):
    id = 409
