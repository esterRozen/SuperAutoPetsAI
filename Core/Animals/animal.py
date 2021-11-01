# noinspection PyUnusedLocal
class Animal:
    xp = 0
    battle_hp = 0
    battle_atk = 0

    def __init__(self, atk, hp):
        self.hp = hp
        self.atk = atk

        self.battle_hp = hp
        self.battle_atk = atk

    @property
    def level(self):
        return min(self.xp//3 + 1, 3)

    def reset_stats(self):
        self.battle_hp = self.hp
        self.battle_atk = self.atk

    def trigger(self, name):
        return NotImplementedError
