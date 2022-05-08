from typing import List, Union
from Core.GameElements.AbstractElements import Animal, Team, Spawner
from Core.GameElements import Shop, GameSystem


# all messages flow through the agent
class BaseAgent:
    def __init__(self, mode):
        self.controller = GameSystem(mode)
        self.spawner = Spawner(mode)
        self.team = Team()
        # TODO make a copy of team when End Turn is reached,
        # all battle logic will use the original team,
        # the backup will be returned at Start Turn, at which point
        # all battle_hp/atk buffs will revert to hp/atk
        self.team_backup = None
        self.enemy = Team()
        self.shop = Shop(mode, 3, 1)

        self.lvl = 0
        self.gold = 0
        self.turn = 1
        self.battle_lost = False
        self.in_shop = True

        # animal that triggered the event is the event_raiser
        # animal that responded to event is the acting animal
        self.event_raiser = 0

    def load(self, team, turn, gold=10, shop=None, hearts=4, battle_lost=False):
        pass

    def trigger_message(self, message):
        pass

    def handle_message(self, message):
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
