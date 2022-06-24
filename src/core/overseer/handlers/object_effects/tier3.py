from typing import TYPE_CHECKING, List, Tuple
from random import random

from ....game_elements.abstract_elements import Animal, Empty
from ....game_elements.game_objects.animals import Ram
from ....game_elements.game_objects.equipment import Melon

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier3:
    # triggers hurt ugh
    @staticmethod
    def badger(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        damage = fainted.level * fainted.battle_atk // 2
        if actor[0] == "team":
            team = agent.team
            target = "enemy"
        else:
            team = agent.enemy
            target = "team"

        behind = (actor[0], team.animals.index(team.friend_behind(actor[1])))
        teammate_ahead = team.friend_ahead(actor[1])

        # deal damage to unit behind
        agent.deal_ability_damage_handle_hurt(damage, actor, behind, fainted)

        if isinstance(teammate_ahead, Empty):
            enemy_pos = agent.team_opposing_(actor).animals.index(agent.team_opposing_(actor).rightmost_unit)
            target = (target, enemy_pos)
        else:
            target = (actor[0], team.animals.index(teammate_ahead))

        # deal damage to unit ahead
        agent.deal_ability_damage_handle_hurt(damage, actor, target, fainted)

    # triggers hurt
    @staticmethod
    def blowfish(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if actor[0] == "enemy":
            opponent = "team"
        else:
            opponent = "enemy"

        target = (opponent, agent.team_opposing_(actor).random_units_idx(1)[0])
        agent.deal_ability_damage_handle_hurt(
            agent.actor(actor).level * 2,
            actor, target)

    @staticmethod
    def camel(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.buff(agent.team_of_(actor).friend_behind(actor[1]), 2, 2)
        elif agent.actor(actor).level == 2:
            agent.buff(agent.team_of_(actor).friend_behind(actor[1]), 4, 4)
        else:
            agent.buff(agent.team_of_(actor).friend_behind(actor[1]), 6, 6)

    @staticmethod
    def dog(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if random() < 0.5:
            agent.buff(agent.actor(actor), 0, agent.actor(actor).level)
        else:
            agent.buff(agent.actor(actor), agent.actor(actor).level, 0)

    @staticmethod
    def giraffe(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.buff(agent.team_of_(actor).friends_ahead(actor[1], agent.actor(actor).level),
                   1, 1)

    @staticmethod
    def hatching_chick(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.team.friend_ahead(actor[1]).temp_buff(5, 5)
        elif agent.actor(actor).level == 2:
            agent.team.friend_ahead(actor[1]).permanent_buff(2, 2)
        else:
            agent.team.friend_ahead(actor[1]).increase_xp(1)

    @staticmethod
    def kangaroo(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        buff_amt = 2 * agent.actor(actor).level
        agent.actor(actor).temp_buff(buff_amt, buff_amt)

    @staticmethod
    def owl(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], removed: Animal):
        if removed.level == 1:
            agent.team.random_friend(actor[1]).permanent_buff(2, 2)
        elif removed.level == 2:
            agent.team.random_friend(actor[1]).permanent_buff(4, 4)
        else:
            agent.team.random_friend(actor[1]).permanent_buff(6, 6)

    @staticmethod
    def ox(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        animal = agent.actor(actor)
        agent.buff(animal, animal.level, 0)
        animal.held = Melon()

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
            agent.team_of_(actor)[target[1]].permanent_buff(0, 1)
        elif agent.actor(actor).level == 2:
            agent.team_of_(actor)[target[1]].permanent_buff(0, 2)
        else:
            agent.team_of_(actor)[target[1]].permanent_buff(0, 3)

    @staticmethod
    def sheep(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        unit = Ram()
        unit.hp = 2 * fainted.level
        unit.battle_hp = 2 * fainted.level
        unit.atk = 2 * fainted.level
        unit.battle_atk = 2 * fainted.level

        agent.summon(unit.__copy__(), actor)
        agent.summon(unit.__copy__(), actor)

    @staticmethod
    def snail(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if not agent.battle_lost:
            return

        if agent.actor(actor).level == 1:
            agent.buff(agent.team_of_(actor).friends(actor[1]), 1, 1)
        elif agent.actor(actor).level == 2:
            agent.buff(agent.team_of_(actor).friends(actor[1]), 2, 2)
        else:
            agent.buff(agent.team_of_(actor).friends(actor[1]), 3, 3)

    @staticmethod
    def tropical_fish(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.team.friend_ahead(actor[1]).permanent_buff(0, agent.actor(actor).level)
        agent.team.friend_behind(actor[1]).permanent_buff(0, agent.actor(actor).level)

    @staticmethod
    def turtle(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        units: List[Animal] = agent.team_of_(actor).friends_behind(actor[1], fainted.level)
        for unit in units:
            unit.held = Melon()
