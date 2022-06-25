# must have a way to save and load states
from typing import TYPE_CHECKING, Optional
import random as rand

from .game_elements.abstract_elements import Team
from .game_elements.game_objects import GameObjects
from .game_elements.game_objects.animals import Ant
from .game_elements.game_objects.game_objects import pack_names
from .game_systems import BattleSystem, ShopSystem
from .game_systems.fightbuffer import FightBuffer
from .overseer import *

if TYPE_CHECKING:
    from . import State


class Engine:
    """
    This engine makes no attempt to prevent an actor from stalling.
    In implementing AI with this engine, you should ensure the agent cannot
    stall by placing limits on number of total actions
    """

    def __init__(self, mode: Optional[str] = None):
        # loads the GameObjects singleton, so it doesn't need to be loaded again
        if mode is None:
            mode = rand.choice(pack_names)
        self.__units = GameObjects()

        self._messenger = MessageAgent(mode)
        self._messenger.debug_mode_no_handle_queue = False

        self._battle_director = BattleSystem(self._messenger)
        self._shop_director = ShopSystem(self._messenger)

        self._fight_buffer = FightBuffer()
        team = Team()
        team.animals[0] = Ant()
        for i in range(1, 21):
            self._fight_buffer.push(team, i)

    @property
    def messenger(self) -> MessageAgent:
        return self._messenger

    @property
    def fight_buffer(self) -> FightBuffer:
        return self._fight_buffer

    def save(self, include_shop: bool = True) -> 'State':
        return self._messenger.save(include_shop)

    def load(self, state: 'State'):
        self._messenger = MessageAgent.load(state)
        self._battle_director = BattleSystem(self._messenger)
        self._shop_director = ShopSystem(self._messenger)

    def move(self, roster_init: int, roster_final: int) -> int:
        # moves init to final position, moving occupying unit toward space unit was moved from

        return self._shop_director.move(roster_init, roster_final)

    def combine(self, roster_init: int, roster_final: int) -> int:
        # place init unit *onto* final unit, if possible

        return self._shop_director.combine(roster_init, roster_final)

    def sell(self, unit: int) -> int:
        # sell unit in occupying space

        return self._shop_director.sell(unit)

    def buy(self, shop_init: int, roster_final: int) -> int:
        # buy unit from shop position and summon to team position
        # will prefer in order:
        # combining unit with occupying unit
        # move occupying unit left if possible
        # move occupying unit right if possible
        # cancel

        return self._shop_director.buy(shop_init, roster_final)

    def freeze(self, shop_pos: int) -> int:
        # toggle freeze of shop position

        return self._shop_director.toggle_freeze(shop_pos)

    def reroll(self) -> int:
        # reroll shop if you have gold

        return self._shop_director.reroll()

    def end_turn(self) -> int:
        # end your turn

        self._shop_director.end_turn()
        enemy = self._fight_buffer.pop(self._messenger.turn)
        if self._messenger.team.size != 0:
            self._fight_buffer.push(self._messenger.team, self._messenger.turn)
        self._battle_director.start_battle(enemy)
        if self._messenger.life == 0 or self._messenger.wins == 10 or self._messenger.turn == 20:
            return -1

        self._shop_director.start_turn()
        return 0
