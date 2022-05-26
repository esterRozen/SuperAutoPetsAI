from typing import TYPE_CHECKING

from ...abstract_elements import Equipment, Animal
if TYPE_CHECKING:
    from ....overseer import MessageAgent


class _Tier3(Equipment):
    def __init__(self):
        super(_Tier3, self).__init__()

    @property
    def tier(self):
        return 3


class Garlic(_Tier3):
    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "incoming":
            return max(1, damage - 2)
        return damage


class SaladBowl(_Tier3):
    pass
