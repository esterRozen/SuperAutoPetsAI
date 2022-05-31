from typing import Tuple, TYPE_CHECKING

from ..game_elements.abstract_elements import Team, Animal
from ..eventnames import *

if TYPE_CHECKING:
    from ..overseer import MessageAgent


class BattleSystem:
    def __init__(self, agent: 'MessageAgent'):
        """

        Args:
            agent (MessageAgent):
        """
        self.__agent = agent
        self.__agent.set_battler(self)
        self.__er: Tuple[str, int] = self.__agent.event_raiser

    def _set_er(self, event_raiser: Tuple[str, int]):
        self.__agent.event_raiser = event_raiser

    def _set_target(self, target: Tuple[str, int]):
        self.__agent.target = target

    def _event(self, event: str, event_raiser=None, target=None):
        self.__agent.handle_event(event, event_raiser=event_raiser, target=target)

    def start_battle(self, enemy: Team):
        # make backup of team
        self.__agent.store_backup()
        self.__agent.enemy = enemy

        # the opponent needs no inter-turn backup as
        # opponent is randomized each turn and
        # opponent team state stored in experience replay

        # start battle trigger
        # handles start of battle for both teams
        self._event(START_BATTLE)

        # loop: (interleave team and enemy events)

        # before attack (team)
        # before attack (enemy)

        self._event(BEFORE_ATTACK, event_raiser=("team", 0))
        self._event(BEFORE_ATTACK, event_raiser=("enemy", 0))

        # attack (team)
        # attack (enemy)
        self._event(ATTACK, event_raiser=("team", 0), target=("enemy", 0))
        self._event(ATTACK, event_raiser=("enemy", 0), target=("team", 0))
        # friend ahead attacks (team)
        # friend ahead attacks (enemy)

        self._event(FRIEND_AHEAD_ATTACKS, event_raiser=("team", 0))
        self._event(FRIEND_AHEAD_ATTACKS, event_raiser=("enemy", 0))

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
        self.__agent.target_team.summon(unit, self.__agent.target[1])
