from Core.Animals.simpleClasses import Equipment


class _Tier2(Equipment):
    def __init__(self):
        super(_Tier2, self).__init__()

    @staticmethod
    def tier():
        return 2
