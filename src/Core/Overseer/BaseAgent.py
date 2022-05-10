from typing import List, Union, Tuple
from abc import abstractmethod
from Core.GameElements.AbstractElements import Animal, Team, Spawner
from Core.GameElements import Shop, GameSystem


# all messages flow through the agent
class BaseAgent:
    def __init__(self, mode):
        self.__mode = mode
        self.spawner = Spawner(mode)
        self.team = Team()
        # TODO make a copy of team when End Turn is reached,
        # all battle logic will use the original team,
        # TODO load backup at start of turn
        # also reset all battle-only buffs
        self.team_backup = None
        self.enemy = Team()
        self.shop = Shop(mode, 3, 1)

        self.life = 10
        self.lvl = 0
        self.gold = 0
        self.turn = 1
        self.battle_lost = False
        self.in_shop = True

        # animal that triggered the event is the event_raiser
        # animal that responded to event is the acting animal
        self.event_raiser: Tuple[str, int] = ("team", 0)
        self.target: Tuple[str, int] = ("team", 0)

    # re-enter shop from a given state
    # used for simulation and replay
    @staticmethod
    def load(mode, team, turn, gold=10, life=10, battle_lost=False, shop=None):
        agent = BaseAgent(mode)
        agent.team = team
        agent.turn = turn
        agent.gold = gold
        agent.life = life
        agent.battle_lost = battle_lost
        if shop is not None:
            agent.shop = shop
        return agent

    @abstractmethod
    def handle_event(self, message, event_raiser, target=None):
        pass

    @abstractmethod
    def trigger_ability(self, message):
        pass

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
