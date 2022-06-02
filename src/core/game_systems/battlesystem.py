from typing import Tuple, TYPE_CHECKING

from ..game_elements.abstract_elements import Team, Animal
from .. import eventnames

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

    def _add_event(self, event: str, actor=None, target=None):
        self.__agent.enqueue_event(event, actor, target)

    def start_battle(self, enemy: Team):
        # make backup of team
        self.__agent.store_backup()
        self.__agent.enemy = enemy

        # the opponent needs no inter-turn backup as
        # opponent is randomized each turn and
        # opponent team state stored in experience replay

        # start battle trigger
        # handles start of battle for both teams
        self._add_event(eventnames.START_BATTLE)
        self.__agent.handle_events()

        # loop: (interleave team and enemy events)

        while self.__agent.team.size > 0 and self.__agent.enemy.size > 0:
            # before attack (team)
            # before attack (enemy)

            self._add_event(eventnames.BEFORE_ATTACK, event_raiser=("team", 0))
            self._add_event(eventnames.BEFORE_ATTACK, event_raiser=("enemy", 0))
            self.__agent.handle_events()

            # attack (team)
            # attack (enemy)
            self._add_event(eventnames.ATTACK, event_raiser=("team", 0), target=("enemy", 0))
            self._add_event(eventnames.ATTACK, event_raiser=("enemy", 0), target=("team", 0))
            # friend ahead attacks (team)
            # friend ahead attacks (enemy)

            self._add_event(eventnames.FRIEND_AHEAD_ATTACKS, event_raiser=("team", 0))
            self._add_event(eventnames.FRIEND_AHEAD_ATTACKS, event_raiser=("enemy", 0))
            self.__agent.handle_events()

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

    def summon(self, unit: Animal, target: Tuple[str, int]):
        self.__agent.team_of_(target).summon(unit, target[1])
