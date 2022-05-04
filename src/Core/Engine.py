# must have a way to save and load states
from Core.BattleSystem import *
from Core.Team.Team import Team
from Core.Overseer import *


class Engine:
    def __init__(self, mode):
        self.system = MessageAgent(mode)
        self.battle_director = BattleSystem(self.system)

    def move(self, roster_init, roster_final):
        pass

    def combine(self, roster_init, roster_final):
        pass

    def sell(self, unit):
        pass

    def buy(self, shop_init, roster_final):
        pass

    def freeze(self, shop_pos):
        pass

    def reroll(self):
        pass

    def end_turn(self):
        pass

    def fight(self, team: Team):
        pass
