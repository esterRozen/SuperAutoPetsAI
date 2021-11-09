from Core.GameElements.SimpleClasses import Equipment


class _Tier1(Equipment):
    def __init__(self):
        super(_Tier1, self).__init__()

    @staticmethod
    def tier():
        return 1


class Apple(_Tier1):
    def trigger(self, name):
        if name == "buy":
            return 80

    pass


class Honey(_Tier1):
    def trigger(self, name):
        if name == "buy":
            return 80

    pass
