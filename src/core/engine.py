# must have a way to save and load states
from typing import TYPE_CHECKING

from .game_systems import BattleSystem, ShopSystem
from .game_elements.abstract_elements import Team
from .overseer import *

if TYPE_CHECKING:
    from . import State


class Engine:
    def __init__(self, mode):
        self._messenger = MessageAgent(mode)
        self._messenger.debug_mode_no_handle_queue = False
        self._battle_director = BattleSystem(self._messenger)
        self._shop_director = ShopSystem(self._messenger)

    @property
    def save(self, include_shop: bool = True) -> 'State':
        return self._messenger.save(include_shop)

    def load(self, state: 'State'):
        self._messenger.load(state)

    def move(self, roster_init: int, roster_final: int):
        # moves init to final position, moving occupying unit toward space unit was moved from

        self._shop_director.move(roster_init, roster_final)

    def combine(self, roster_init: int, roster_final: int):
        # place init unit *onto* final unit, if possible

        self._shop_director.combine(roster_init, roster_final)

    def sell(self, unit: int):
        # sell unit in occupying space

        self._shop_director.sell(unit)

    def buy(self, shop_init, roster_final):
        # buy unit from shop position and summon to team position
        # will prefer in order:
        # combining unit with occupying unit
        # move occupying unit left if possible
        # move occupying unit right if possible
        # cancel

        self._shop_director.buy(shop_init, roster_final)

    def freeze(self, shop_pos):
        # toggle freeze of shop position

        self._shop_director.toggle_freeze(shop_pos)

    def reroll(self):
        # reroll shop if you have gold

        self._shop_director.reroll()

    def end_turn(self):
        # end your turn

        self._shop_director.end_turn()

    def fight(self, team: Team):
        # fight the provided team

        outcome = self._battle_director.start_battle(team)

        # TODO using outcome of fight ->
        #  return info on state (team, wins, life, etc)

    def start_turn(self):
        # start your turn

        self._shop_director.start_turn()
