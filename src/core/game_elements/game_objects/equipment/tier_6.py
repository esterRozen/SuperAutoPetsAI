from typing import TYPE_CHECKING

from ...abstract_elements import Equipment, Animal, Unarmed
from .... import eventnames

if TYPE_CHECKING:
    from ....overseer import MessageAgent


class _Tier6(Equipment):
    def __init__(self):
        super(_Tier6, self).__init__()

    @property
    def tier(self):
        return 6


class Coconut(_Tier6):
    id = 417
    is_holdable = True
    rollable = False

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "incoming":
            animal.held = Unarmed()
            return 0
        return damage


class Melon(_Tier6):
    id = 418
    is_holdable = True

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "incoming":
            damage = max(0, damage - 20)
            animal.held = Unarmed()
            return damage
        return damage


class Mushroom(_Tier6):
    id = 419
    is_holdable = True

    def trigger(self, name: str) -> int:
        if name == eventnames.ON_FAINT:
            return self.id
        return 0


class Pizza(_Tier6):
    id = 420
    is_targeted = False


class Steak(_Tier6):
    id = 421
    is_holdable = True

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "outgoing":
            damage += 20
            animal.held = Unarmed()
            return damage
        return damage
