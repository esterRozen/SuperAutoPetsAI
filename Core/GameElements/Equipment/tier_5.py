from Core.GameElements.simpleClasses import Equipment


class _Tier5(Equipment):
    def __init__(self):
        super(_Tier5, self).__init__()

    @staticmethod
    def tier():
        return 5
