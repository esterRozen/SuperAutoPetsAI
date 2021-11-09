from Core.GameElements.SimpleClasses import Equipment


class _Tier4(Equipment):
    def __init__(self):
        super(_Tier4, self).__init__()

    @staticmethod
    def tier():
        return 4


class CannedFood(_Tier4):
    pass


class Pear(_Tier4):
    pass
