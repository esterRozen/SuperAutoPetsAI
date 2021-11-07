# noinspection PyUnusedLocal,PyMethodMayBeStatic
class Animal:
    xp = 0
    battle_hp = 0
    battle_atk = 0
    cost = 3

    tier = 0

    def __init__(self, atk, hp):
        self.hp = hp
        self.atk = atk

        self.battle_hp = hp
        self.battle_atk = atk

    @property
    def level(self):
        return min(self.xp // 3 + 1, 3)

    def permanent_buff(self, hp, atk):
        self.hp += hp
        self.atk += atk

        self.battle_hp += hp
        self.battle_atk += atk
        return

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


# noinspection PyUnusedLocal,PyMethodMayBeStatic
class Equipment:
    cost = 3

    def trigger(self, name):
        return 0