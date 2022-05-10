# must have a way to save and load states
from .BattleSystem import *
from .GameElements import GameSystem
from .GameElements.AbstractElements.Team import Team
from .Overseer import *


class Engine:
    def __init__(self, mode):
        self.messenger = MessageAgent(mode)
        self.battle_director = BattleSystem(self.messenger)
        self.shop_director = GameSystem(self.messenger)

        self.messenger.set_battler(self.battle_director)
        self.messenger.set_shopper(self.shop_director)

    def move(self, roster_init, roster_final):
        # moves init unit to *left* side of final unit
        pass

    def combine(self, roster_init, roster_final):
        # place init unit *onto* final unit
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
