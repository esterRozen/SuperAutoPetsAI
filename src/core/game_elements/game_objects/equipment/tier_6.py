from typing import TYPE_CHECKING

from ...abstract_elements import Equipment, Animal, Unarmed

if TYPE_CHECKING:
    from ....overseer import MessageAgent


class _Tier6(Equipment):
    def __init__(self):
        super(_Tier6, self).__init__()

    @property
    def tier(self):
        return 6


class Coconut(_Tier6):
    is_edible = False

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "incoming":
            agent.target_animal.held = Unarmed()
            return 0
        return damage


class Melon(_Tier6):
    is_edible = False

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "incoming":
            damage = max(0, damage - 20)
            agent.target_animal.held = Unarmed()
            return damage
        return damage


class Mushroom(_Tier6):
    is_edible = False


class Pizza(_Tier6):
    is_targeted = False


class Steak(_Tier6):
    is_instant = False

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str) -> int:
        if message == "outgoing":
            damage += 20
            agent.target_animal.held = Unarmed()
            return damage
        return damage
