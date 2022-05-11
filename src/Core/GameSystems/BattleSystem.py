from typing import Tuple

from ..GameElements.AbstractElements import Team, Animal
from ..Overseer import *


class BattleSystem:
    def __init__(self, agent: MessageAgent):
        self.__agent = agent
        self.__er: Tuple[str, int] = self.__agent.event_raiser

    def start_battle(self, enemy: Team):
        # make backup of team
        self.__agent.store_backup()
        self.__agent.enemy = enemy

        # opponent needs no inter-turn backup as
        # opponent is randomized each turn and
        # opponent team state stored in experience replay

        # start battle trigger

        # loop:
        # (team)
        # before attack trigger,
        # friend ahead attacks,
        # enemy attacks,
        # (enemy)
        # before attack,
        # friend ahead attacks,
        # enemy attacks

        # if team unit still above 0 hp:
        # hurt

        # if enemy unit still above 0 hp:
        # hurt (enemy)

        # if team unit not above 0 hp:
        # on faint (team)
        # friend faints
        # friend ahead faints
        # knock out (on enemy team)

        # if enemy unit not above 0 hp:
        # on faint (enemy)
        # friend faints (enemy)
        # friend ahead faints (enemy)
        # knock out (on friendly team)
        pass

    def summon(self, unit: Animal, position: int):
        pass
