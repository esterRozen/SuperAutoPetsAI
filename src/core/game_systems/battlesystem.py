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

        self._add_event(eventnames.BEFORE_BATTLE)
        self.agent.handle_events()

        # start battle trigger
        # handles start of battle for both teams
        self._add_event(eventnames.START_BATTLE)
        self.agent.handle_events()

        # loop: (interleave team and enemy events)

        while self.agent.team.size > 0 and self.agent.enemy.size > 0:
            # before attack (team)
            # before attack (enemy)
            self.agent.team.push_forward()
            self.agent.enemy.push_forward()

            self._add_event(eventnames.BEFORE_ATTACK, actor=("team", 0))
            self._add_event(eventnames.BEFORE_ATTACK, actor=("enemy", 0))
            self.agent.handle_events()

            # attack (team)
            # attack (enemy)
            self._add_event(eventnames.ATTACK, actor=("team", 0), target=("enemy", 0))
            self.agent.handle_events()
            # friend ahead attacks (team)
            # friend ahead attacks (enemy)

            self._add_event(eventnames.FRIEND_AHEAD_ATTACKS, actor=("team", 0))
            self._add_event(eventnames.FRIEND_AHEAD_ATTACKS, actor=("enemy", 0))
            self.agent.handle_events()

        # handle end of battle conditions.
        if self.agent.team.size == 0 and self.agent.enemy.size == 0:
            # draw, overwrite battle_lost
            self.agent.battle_lost = False
            return 0
        elif self.agent.team.size == 0:
            # loss, remove life
            self.agent.life -= min(3, (self.agent.turn + 1) // 2)
            self.agent.battle_lost = True
            return -1
        else:
            # win, gain 1 trophy
            self.agent.wins += 1
            self.agent.battle_lost = False
            return 1

    def summon(self, unit: Animal, target: Tuple[str, int]):
        success = self.agent.team_of_(target).summon(unit, target[1])

        if not success:
            return

        self.agent.enqueue_event(eventnames.IS_SUMMONED,
                                 actor=target,
                                 target=target)

        self.agent.enqueue_event(eventnames.FRIEND_SUMMONED_BATTLE,
                                 actor=target,
                                 target=target)
