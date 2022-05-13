# must have a way to save and load states
from dataclasses import dataclass

from .GameSystems import BattleSystem, ShopSystem
from .GameElements.AbstractElements import Team
from .GameElements import Shop
from .Overseer import *


@dataclass
class State:
    mode: str
    turn: int
    life: int
    battle_lost: bool
    team: Team
    shop: Shop = None
    gold: int = 10


class Engine:
    def __init__(self, mode):
        self.messenger = MessageAgent(mode)
        self.battle_director = BattleSystem(self.messenger)
        self.shop_director = ShopSystem(self.messenger)

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
        self.shop_director.freeze(shop_pos)

    def reroll(self):
        self.shop_director.reroll()

    def end_turn(self):
        self.shop_director.end_turn()

    def fight(self, team: Team):
        outcome = self.battle_director.start_battle(team)

        # TODO using outcome of fight ->
        #  return info on state (team, wins, life, etc)

    def start_turn(self):
        self.shop_director.start_turn()
