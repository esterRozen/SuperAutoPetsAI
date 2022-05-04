from Core.GameElements.AbstractElements.SimpleClasses import Equipment


class _Tier5(Equipment):
    def __init__(self):
        super(_Tier5, self).__init__()

    @staticmethod
    def tier():
        return 5


class Chili(_Tier5):
    pass


class Chocolate(_Tier5):
    pass


class Milk(_Tier5):
    cost = 0