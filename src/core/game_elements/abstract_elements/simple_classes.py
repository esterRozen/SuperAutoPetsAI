import copy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...overseer import MessageAgent


class Animal:
    rollable: bool = True
    xp: int = 0
    battle_hp: int = 0
    battle_atk: int = 0
    cost: int = 3

    tier: int = 0
    id: int = 0

    def __init__(self, atk: int, hp: int):
        self.held: Equipment = Unarmed()

        self.hp: int = hp
        self.atk: int = atk

        self.battle_hp = hp
        self.battle_atk = atk

    def __copy__(self):
        return copy.deepcopy(self)

    def __lt__(self, other):
        if self.battle_atk < other.battle_atk:
            return True
        elif self.battle_atk == other.battle_atk:
            if self.battle_hp < other.battle_hp:
                return True
            elif self.battle_hp == other.battle_hp:
                if self.tier < other.tier:
                    return True
        return False

    def __repr__(self):
        return f"({self.__class__.__name__}): " \
               f"perm.{self.atk}/{self.hp}, " \
               f"temp.{self.battle_atk}/{self.battle_hp}"

    def is_identical(self, other: 'Animal') -> bool:
        if type(other) != type(self):
            return False
        for key in other.__dict__:
            if key in self.__dict__:
                if self.__dict__[key] != other.__dict__[key]:
                    return False
            else:
                return False
        return True

    @property
    def level(self) -> int:
        return min((self.xp + 1) // 3 + 1, 3)

    def trigger(self, name: str) -> int:
        return 0

    def damage_modifier(self, agent: 'MessageAgent', amount: int, message: str):
        """
        calculates the damage to deal or be dealt by/to a unit based on held item
        Args:
            agent: message agent, used for some cases to affect other animals
            amount: attack power
            message: incoming damage: "incoming"
                     outgoing damage: "physical", "ability"
        Returns: int damage
        """
        return self.held.query(self, agent, amount, message)

    def permanent_buff(self, atk: int, hp: int):
        # accounts for negative buffs
        # which leave with minimum 1 atk or hp
        self.hp = max(self.hp + hp, 1)
        self.atk = max(self.atk + atk, 1)

        self.battle_hp = max(self.battle_hp + hp, 1)
        self.battle_atk = max(self.battle_atk + atk, 1)
        return self

    def temp_buff(self, atk: int, hp: int):
        self.battle_hp = max(self.battle_hp + hp, 1)
        self.battle_atk = max(self.battle_atk + atk, 1)
        return self

    def reset_temp_stats(self):
        self.battle_hp = self.hp
        self.battle_atk = self.atk
        return self

    def increase_xp(self, n: int):
        if self.xp == 5 or n == 0:
            return self
        self.permanent_buff(1, 1)
        self.xp += 1
        return self.increase_xp(n-1)


class Empty(Animal):
    rollable = False
    cost = 0

    def __init__(self):
        super(Empty, self).__init__(0, 0)

    def __eq__(self, other):
        return isinstance(other, Empty)

    def permanent_buff(self, atk: int, hp: int):
        return self

    def temp_buff(self, atk: int, hp: int):
        return self

    def increase_xp(self, n: int):
        return self

    @property
    def level(self):
        return 0

    def reset_temp_stats(self):
        return self

    def trigger(self, name: str) -> int:
        return 0


# noinspection PyUnusedLocal,PyMethodMayBeStatic
class Equipment:
    rollable: bool = True
    cost = 3
    id = 0
    is_targeted = True

    def __eq__(self, other: 'Equipment') -> bool:
        for key in self.__dict__:
            if key in self.__dict__:
                if self.__dict__[key] != other.__dict__[key]:
                    return False
            else:
                return False
        return True

    @property
    def tier(self):
        return 0

    def trigger(self, name: str):
        return 0

    def query(self, animal: Animal, agent: 'MessageAgent', damage: int, message: str):
        return damage


class Unarmed(Equipment):
    cost = 0
    id = 0
