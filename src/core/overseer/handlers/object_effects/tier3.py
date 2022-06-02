from typing import TYPE_CHECKING, List, Tuple

from ....game_elements.abstract_elements import Animal
from ....game_elements.game_objects.animals import Butterfly, Ram
from ....game_elements.game_objects.equipment import Melon

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier3:
    # triggers hurt ugh
    @staticmethod
    def badger(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        # TODO
        pass

    # triggers hurt
    @staticmethod
    def blowfish(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        # TODO
        pass

    @staticmethod
    def camel(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.buff(agent.team_of_(actor).friend_behind(actor[1]), 1, 2)
        elif agent.actor(actor).level == 2:
            agent.buff(agent.team_of_(actor).friend_behind(actor[1]), 2, 4)
        else:
            agent.buff(agent.team_of_(actor).friend_behind(actor[1]), 3, 6)

    @staticmethod
    def caterpillar(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(actor).xp += 1
        elif agent.actor(actor).level == 2:
            agent.actor(actor).xp += 1
        else:
            agent.team_of_(actor).animals[actor[1]] = Butterfly()

    @staticmethod
    def dog(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(actor).permanent_buff(1, 1)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).permanent_buff(2, 2)
        else:
            agent.actor(actor).permanent_buff(3, 3)

    @staticmethod
    def giraffe(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.buff(agent.team_of_(actor).friends_ahead(actor[1], 1), 1, 1)
        elif agent.actor(actor).level == 2:
            agent.buff(agent.team_of_(actor).friends_ahead(actor[1], 2), 1, 1)
        else:
            agent.buff(agent.team_of_(actor).friends_ahead(actor[1], 3), 1, 1)

    @staticmethod
    def hatching_chick(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.team_of_(actor).friend_ahead(actor[1]).temp_buff(5, 5)
        elif agent.actor(actor).level == 2:
            agent.team_of_(actor).friend_ahead(actor[1]).permanent_buff(2, 2)
        else:
            agent.team_of_(actor).friend_ahead(actor[1]).increase_xp(1)

    @staticmethod
    def kangaroo(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(actor).temp_buff(2, 2)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).temp_buff(4, 4)
        else:
            agent.actor(actor).temp_buff(6, 6)

    @staticmethod
    def owl(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.team_of_(actor).random_friend(actor[1]).permanent_buff(2, 2)
        elif agent.actor(actor).level == 2:
            agent.team_of_(actor).random_friend(actor[1]).permanent_buff(4, 4)
        else:
            agent.team_of_(actor).random_friend(actor[1]).permanent_buff(6, 6)

    @staticmethod
    def ox(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.actor(actor).permanent_buff(agent.actor(actor).level, 0)
        agent.actor(actor).held = Melon()

    @staticmethod
    def puppy(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.gold < 2:
            return
        if agent.actor(actor).level == 1:
            agent.actor(actor).permanent_buff(2, 2)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).permanent_buff(4, 4)
        else:
            agent.actor(actor).permanent_buff(6, 6)

    @staticmethod
    def rabbit(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.team_of_(actor).animals[target[1]].permanent_buff(0, 1)
        elif agent.actor(actor).level == 2:
            agent.team_of_(actor).animals[target[1]].permanent_buff(0, 2)
        else:
            agent.team_of_(actor).animals[target[1]].permanent_buff(0, 3)

    @staticmethod
    def sheep(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        unit = Ram()
        unit.hp = 2 * agent.actor(actor).level
        unit.atk = 2 * agent.actor(actor).level

        agent.summon(unit.__copy__(), actor)
        agent.summon(unit.__copy__(), actor)

    @staticmethod
    def snail(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if not agent.battle_lost:
            return
        if agent.actor(actor).level == 1:
            agent.buff(agent.team_of_(actor).friends(actor[1]), 2, 1)
        elif agent.actor(actor).level == 2:
            agent.buff(agent.team_of_(actor).friends(actor[1]), 4, 2)
        else:
            agent.buff(agent.team_of_(actor).friends(actor[1]), 6, 3)

    @staticmethod
    def tropical_fish(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.team_of_(actor).friend_ahead(actor[1]).permanent_buff(0, agent.actor(actor).level)
        agent.team_of_(actor).friend_behind(actor[1]).permanent_buff(0, agent.actor(actor).level)

    @staticmethod
    def turtle(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        units: List[Animal] = agent.team_of_(actor).friends_behind(actor[1], agent.actor(actor).level)
        for unit in units:
            unit.held = Melon()
