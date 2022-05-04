# noinspection PyUnusedLocal
class Animal:
    xp: int = 0
    battle_hp: int = 0
    battle_atk: int = 0
    cost: int = 3

    tier: int = 0
    id: int = 0

    def __init__(self, atk: int, hp: int):
        self.hp: int = hp
        self.atk: int = atk

        self.battle_hp = hp
        self.battle_atk = atk

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

    def increase_xp(self, n: int):
        if self.xp == 5 or n == 0:
            return self
        self.permanent_buff(1, 1)
        self.xp += 1
        return self.increase_xp(n-1)

    @property
    def level(self) -> int:
        return min((self.xp + 1) // 3 + 1, 3)

    def reset_stats(self):
        self.battle_hp = self.hp
        self.battle_atk = self.atk
        return self

    def trigger(self, name: int):
        return 0

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


class Empty(Animal):
    def __init__(self):
        super(Empty, self).__init__(0, 0)

    def permanent_buff(self, atk: int, hp: int):
        return self

    def temp_buff(self, atk: int, hp: int):
        return self

    def increase_xp(self, n: int):
        return self

    @property
    def level(self):
        return 0

    def reset_stats(self):
        return self

    def trigger(self, name: int):
        return 0


# noinspection PyUnusedLocal,PyMethodMayBeStatic
class Equipment:
    cost = 3
    id = 0

    def trigger(self, name: int):
        return 0


class Unarmed(Equipment):
    cost = 0
    id = 0
