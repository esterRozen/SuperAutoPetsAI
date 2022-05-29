from typing import TYPE_CHECKING

from ...abstract_elements import Equipment, Animal
if TYPE_CHECKING:
    from ....overseer import MessageAgent


class _Tier5(Equipment):
    def __init__(self):
        super(_Tier5, self).__init__()

    @property
    def tier(self):
        return 5


class Chili(_Tier5):
    id = 410

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "outgoing":
            #  TODO damage second member of enemy team
            return damage
        return damage


class Chocolate(_Tier5):
    id = 411


class Peanut(_Tier5):
    id = 412
    rollable = False

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "outgoing":
            damage += 50
            return damage
        return damage


class Sushi(_Tier5):
    id = 413
    is_targeted = False


class Milk(_Tier5):
    id = 414
    rollable = False
    cost = 0


class Better_Milk(_Tier5):
    id = 415
    rollable = False
    cost = 0


class Best_Milk(_Tier5):
    id = 416
    rollable = False
    cost = 0
