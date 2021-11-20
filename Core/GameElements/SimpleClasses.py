# noinspection PyUnusedLocal
class Animal:
    xp = 0
    battle_hp = 0
    battle_atk = 0
    cost = 3

    tier = 0
    id = 0

    def __init__(self, atk, hp):
        self.hp = hp
        self.atk = atk

        self.battle_hp = hp
        self.battle_atk = atk

    def permanent_buff(self, atk, hp):
        self.hp += hp
        self.atk += atk

        self.battle_hp += hp
        self.battle_atk += atk
        return

    def temp_buff(self, atk, hp):
        self.battle_hp += hp
        self.battle_atk += atk
        return

    def increase_xp(self, n):
        self.xp = min(6, self.xp+n)

    def level(self):
        return min(self.xp // 3 + 1, 3)

    def reset_stats(self):
        self.battle_hp = self.hp
        self.battle_atk = self.atk

    def trigger(self, name):
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

    def level(self):
        return 0


# noinspection PyUnusedLocal,PyMethodMayBeStatic
class Equipment:
    cost = 3
    id = 0

    def trigger(self, name):
        return 0


class Unarmed(Equipment):
    pass
