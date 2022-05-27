from typing import TYPE_CHECKING

from ...abstract_elements import Equipment, Animal
if TYPE_CHECKING:
    from ....overseer import MessageAgent


class _Tier2(Equipment):
    def __init__(self):
        super(_Tier2, self).__init__()

    @property
    def tier(self):
        return 2


class Cupcake(_Tier2):
    pass


class MeatBone(_Tier2):
    is_consumable = False

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "outgoing":
            return damage + 5
        return damage


class SleepingPill(_Tier2):
    cost = 1


class Weak(_Tier2):
    is_consumable = False
    rollable = False

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "incoming":
            return damage + 3
        return damage
    pass
