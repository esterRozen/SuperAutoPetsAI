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
        self.agent = agent
        self.agent.set_battler(self)

    def _add_event(self, event: str, actor=None, target=None):
        self.agent.enqueue_event(event, actor, target)

    def start_battle(self, enemy: Team) -> int:
        """
        returns a result of the agent's team fighting the provided enemy

        Args:
            enemy: team to fight
        Returns:    1 if result is a win
                    0 if result is a draw
                    -1 if result is a loss

        """
        # make backup of team
        self.agent.store_backup()
        self.agent.enemy = enemy

        # the opponent needs no inter-turn backup as
        # opponent is randomized each turn and
        # opponent team state stored in experience replay

        # start battle trigger
        # handles start of battle for both teams
        self._add_event(eventnames.START_BATTLE)
        self.agent.handle_events()

        # loop: (interleave team and enemy events)

        while self.agent.team.size > 0 and self.agent.enemy.size > 0:
            # before attack (team)
            # before attack (enemy)

            self._add_event(eventnames.BEFORE_ATTACK, actor=("team", 0))
            self._add_event(eventnames.BEFORE_ATTACK, actor=("enemy", 0))
            self.agent.handle_events()

            # attack (team)
            # attack (enemy)
            self._add_event(eventnames.ATTACK, actor=("team", 0), target=("enemy", 0))
            self._add_event(eventnames.ATTACK, actor=("enemy", 0), target=("team", 0))
            self.agent.handle_events()
            # friend ahead attacks (team)
            # friend ahead attacks (enemy)

            self._add_event(eventnames.FRIEND_AHEAD_ATTACKS, actor=("team", 0))
            self._add_event(eventnames.FRIEND_AHEAD_ATTACKS, actor=("enemy", 0))
            self.agent.handle_events()

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

        # handle win, loss, draw actions
        return 0
    
    def summon(self, unit: Animal, target: Tuple[str, int]):
        self.agent.team_of_(target).summon(unit, target[1])
