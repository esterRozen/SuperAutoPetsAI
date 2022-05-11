from typing import Tuple

from ..GameElements.AbstractElements import Team, Animal
from ..Overseer import *
from ..Overseer.Handlers.Items.eventnames import *


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
        # handles start of battle for both teams
        self.__agent.handle_event(START_BATTLE)

        # loop: (interleave team and enemy events)
        # team events
        # before attack
        # friend ahead attacks,
        # enemy attacks,

        # enemy events
        # before attack,
        # friend ahead attacks,
        # enemy attacks

        self.__er = ("team", 0)
        self.__agent.handle_event(BEFORE_ATTACK)
        self.__er = ("enemy", 0)
        self.__agent.handle_event(BEFORE_ATTACK)

        # handle hurt and faint triggers in *response* to attack events.
        # if team unit still above 0 hp:
        # hurt

        # if enemy unit still above 0 hp:
        # hurt (enemy)

        self.__er = ("team", 0)
        self.__agent.handle_event(FRIEND_AHEAD_ATTACKS)
        self.__er = ("enemy", 0)
        self.__agent.handle_event(FRIEND_AHEAD_ATTACKS)

        self.__er = ("enemy", 0)
        self.__agent.handle_event(ENEMY_ATTACKS)
        self.__er = ("team", 0)
        self.__agent.handle_event(ENEMY_ATTACKS)

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

    def summon(self, unit: Animal):
        pass
