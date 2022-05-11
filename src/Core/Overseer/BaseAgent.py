import copy
from abc import abstractmethod
from typing import List, Union, Tuple, Optional

from ..GameElements.AbstractElements import Animal, Team, Spawner
from ..GameElements import Shop
from ..eventnames import *
from ..GameSystems import BattleSystem, ShopSystem


# all messages flow through the agent
class BaseAgent:
    def __init__(self, mode):
        self.__mode = mode
        self.__battler: Optional[BattleSystem] = None
        self.__shopper: Optional[ShopSystem] = None

        self.spawner = Spawner(mode)

        # all that is needed to define current state
        self.team = Team()
        self.life = 10
        self.lvl = 0
        self.gold = 0
        self.turn = 1
        self.battle_lost = False
        self.in_shop = True

        self.team_backup = None
        # another message agent has the enemy as their own team
        # maintains synchronization between the two
        self.enemy = Team()

        self.shop = Shop(mode, 3, 1)

        # animal that triggered the event is the event_raiser
        # animal that responded to event is the acting animal
        self.event_raiser: Tuple[str, int] = ("team", 0)
        self.target: Tuple[str, int] = ("team", 0)

    # re-enter shop from a given state
    # used for simulation and replay
    @staticmethod
    @abstractmethod
    def load(mode, team, turn, gold=10, life=10, battle_lost=False, shop=None) -> 'BaseAgent':
        pass

    def save(self, include_shop: bool) -> Tuple:
        if include_shop:
            state = (self.__mode, self.team, self.turn, self.gold,
                     self.life, self.battle_lost, self.shop)
        else:
            state = (self.__mode, self.team, self.turn, self.gold,
                     self.life, self.battle_lost)
        return state

    @abstractmethod
    def handle_event(self, message, event_raiser=None, target=None):
        pass

    @abstractmethod
    def trigger_ability(self, message):
        pass

    def store_backup(self):
        self.team_backup = copy.deepcopy(self.team)

    def load_backup(self):
        if self.team_backup is not None:
            self.team = copy.deepcopy(self.team_backup)
            self.team_backup = None

    def set_battler(self, battle_system: BattleSystem):
        self.__battler = battle_system

    def set_shopper(self, game_system: ShopSystem):
        self.__shopper = game_system

    def reset_temp_stats(self):
        for animal in self.team.animals:
            animal.reset_temp_stats()

    def _nop(self):
        pass

    def buff(self, unit: Union[List[Animal], Animal], atk, hp):
        if self.in_shop:
            if isinstance(unit, Animal):
                unit.permanent_buff(atk, hp)
            else:
                for animal in unit:
                    animal.permanent_buff(atk, hp)
        else:
            if isinstance(unit, Animal):
                unit.temp_buff(atk, hp)
            else:
                for animal in unit:
                    animal.temp_buff(atk, hp)
        return

    def damage(self, damage: int):
        if self.event_raiser[0] == "team":
            self.team.animals[self.event_raiser[1]].battle_hp -= damage
            if self.team.animals[self.event_raiser[1]].battle_hp < 1:
                self.faint()
            else:
                self.handle_event(HURT)
        elif self.event_raiser[0] == "enemy":
            self.team.animals[self.event_raiser[1]].battle_hp -= damage
            if self.enemy.animals[self.event_raiser[1]].battle_hp < 1:
                self.faint()
            else:
                self.handle_event(HURT)

    def faint(self):
        # assume current event raiser is the one to faint!
        # assume *target* is current unit to have attacked!
        if self.event_raiser[0] == "team":
            self.handle_event(ON_FAINT)

            self.handle_event(FRIEND_AHEAD_FAINTS)

            self.event_raiser = ("enemy", self.target[1])
            self.handle_event(KNOCK_OUT)
        elif self.event_raiser[0] == "enemy":
            self.handle_event(ON_FAINT)

            self.handle_event(FRIEND_AHEAD_FAINTS)

            self.event_raiser = ("team", self.target[1])
            self.handle_event(KNOCK_OUT)

    def summon(self, unit: Animal):
        self.__battler.summon(unit)
