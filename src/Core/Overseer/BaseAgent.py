from typing import List, Union, Tuple
from abc import abstractmethod
from Core.GameElements.AbstractElements import Animal, Team, Spawner
from Core.GameElements import Shop, ShopSystem
from ..GameSystems import BattleSystem


# all messages flow through the agent
class BaseAgent:
    def __init__(self, mode):
        self.__mode = mode
        self.__battler = None
        self.__shopper = None

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
    def handle_event(self, message, event_raiser, target=None):
        pass

    @abstractmethod
    def trigger_ability(self, message):
        pass

    def set_battler(self, battle_system: BattleSystem):
        self.__battler = battle_system

    def set_shopper(self, game_system: ShopSystem):
        self.__shopper = game_system

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
