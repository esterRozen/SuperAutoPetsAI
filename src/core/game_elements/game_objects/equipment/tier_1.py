from ...abstract_elements import Equipment


class _Tier1(Equipment):
    def __init__(self):
        super(_Tier1, self).__init__()

    @property
    def tier(self):
        return 1


class Apple(_Tier1):
    def trigger(self, name):
        if name == "buy":
            return 80


class Honey(_Tier1):
    def trigger(self, name):
        if name == "buy":
            return 80
