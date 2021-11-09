from Core.GameElements.SimpleClasses import Equipment


class _Tier2(Equipment):
    def __init__(self):
        super(_Tier2, self).__init__()

    @staticmethod
    def tier():
        return 2


class Cupcake(_Tier2):
    pass


class MeatBone(_Tier2):
    pass


class SleepingPill(_Tier2):
    pass
