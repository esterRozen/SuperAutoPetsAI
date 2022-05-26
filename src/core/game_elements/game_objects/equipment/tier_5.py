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
    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "outgoing":
            #  TODO damage second member of enemy team
            return damage
        return damage


class Chocolate(_Tier5):
    pass


class Peanut(_Tier5):
    rollable = False

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "outgoing":
            damage += 50
            return damage
        return damage


class Sushi(_Tier5):
    pass


class Milk(_Tier5):
    rollable = False
    cost = 0


class BetterMilk(_Tier5):
    rollable = False
    cost = 0


class BestMilk(_Tier5):
    rollable = False
    cost = 0
