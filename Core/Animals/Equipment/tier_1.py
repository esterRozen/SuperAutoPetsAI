from Core.Animals.baseClasses import Equipment


class _Tier1(Equipment):
    def __init__(self):
        super(_Tier1, self).__init__()

    @staticmethod
    def tier():
        return 1
