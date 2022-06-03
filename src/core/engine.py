# must have a way to save and load states
from typing import TYPE_CHECKING

from .game_systems import BattleSystem, ShopSystem
from .game_elements.abstract_elements import Team
from .overseer import *

if TYPE_CHECKING:
    from . import State


class Engine:
    def __init__(self, mode):
        self.__messenger = MessageAgent(mode)
        self.__battle_director = BattleSystem(self.__messenger)
        self.__shop_director = ShopSystem(self.__messenger)

        self.__messenger.set_battler(self.__battle_director)
        self.__messenger.set_shopper(self.__shop_director)

    @property
    def save(self, include_shop: bool = True) -> 'State':
        return self.__messenger.save(include_shop)

    def load(self, state: 'State'):
        self.__messenger.load(state)

    def move(self, roster_init: int, roster_final: int):
        # moves init unit to *left* side of final unit

        self.__shop_director.move(roster_init, roster_final)

    def combine(self, roster_init: int, roster_final: int):
        # place init unit *onto* final unit

        self.__shop_director.combine(roster_init, roster_final)

    def sell(self, unit: int):
        self.__shop_director.sell(unit)

    def buy(self, shop_init, roster_final):
        self.__shop_director.buy(shop_init, roster_final)

    def freeze(self, shop_pos):
        self.__shop_director.toggle_freeze(shop_pos)

    def reroll(self):
        self.__shop_director.reroll()

    def end_turn(self):
        self.__shop_director.end_turn()

    def fight(self, team: Team):
        outcome = self.__battle_director.start_battle(team)

        # TODO using outcome of fight ->
        #  return info on state (team, wins, life, etc)

    def start_turn(self):
        self.__shop_director.start_turn()
