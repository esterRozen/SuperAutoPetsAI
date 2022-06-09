from typing import TYPE_CHECKING, Tuple

from ....game_elements.abstract_elements import Animal
from ....game_elements.game_objects.animals import Zombie_Cricket
if TYPE_CHECKING:
    from ... import MessageAgent


class Tier1:
    @staticmethod
    def nop(*args):
        return

    @staticmethod
    def ant(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        #  buff random animal on team.
        friend = agent.team_of_(actor).random_friend(actor[1])
        if not friend:
            return

        if fainted.level == 1:
            agent.buff(friend, 2, 1)
        elif fainted.level == 2:
            agent.buff(friend, 4, 2)
        else:
            agent.buff(friend, 6, 3)

    # on sell give 2 +1/2/3 hp
    @staticmethod
    def beaver(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        friends = agent.team.random_friends(actor[1], 2)
        if not friends:
            return

        if agent.actor(actor).level == 1:
            [friend.permanent_buff(0, 1) for friend in friends]
        elif agent.actor(actor).level == 2:
            [friend.permanent_buff(0, 2) for friend in friends]
        else:
            [friend.permanent_buff(0, 3) for friend in friends]

    @staticmethod
    def beetle(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.shop.leftmost_pet(1)[0].permanent_buff(0, 1)
        elif agent.actor(actor).level == 2:
            agent.shop.leftmost_pet(1)[0].permanent_buff(0, 2)
        else:
            agent.shop.leftmost_pet(1)[0].permanent_buff(0, 3)

    # give leftmost friend 1, 2, 3 atk
    @staticmethod
    def bluebird(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.team.leftmost_unit.permanent_buff(1, 0)
        elif agent.actor(actor).level == 2:
            agent.team.leftmost_unit.permanent_buff(2, 0)
        else:
            agent.team.leftmost_unit.permanent_buff(3, 0)

    # summons handled via fainted argument
    @staticmethod
    def cricket(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        unit = Zombie_Cricket()

        unit.battle_atk = fainted.level
        unit.atk = fainted.level
        unit.battle_hp = fainted.level
        unit.hp = fainted.level

        agent.summon(unit, actor)

    @staticmethod
    def duck(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.shop.buff(0, 1)
        elif agent.actor(actor).level == 2:
            agent.shop.buff(0, 2)
        else:
            agent.shop.buff(0, 3)

    # on level give all friends +1/1, +2/2, X
    @staticmethod
    def fish(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            raise ValueError("this shouldn't happen! fish lvl 1 trigger")
        if agent.actor(actor).level == 2:
            agent.buff(agent.team.friends(actor[1]), 1, 1)
        elif agent.actor(actor).level == 3:
            agent.buff(agent.team.friends(actor[1]), 2, 2)

    # friend summoned, give +1/2/3 atk until end of battle
    @staticmethod
    def horse(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(target).temp_buff(1, 0)
        elif agent.actor(actor).level == 2:
            agent.actor(target).temp_buff(2, 0)
        else:
            agent.actor(target).temp_buff(3, 0)

    # buy food, gain x/x until end of battle
    @staticmethod
    def ladybug(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(actor).temp_buff(1, 1)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).temp_buff(2, 2)
        else:
            agent.actor(actor).temp_buff(3, 3)

    # start of battle deal 1/2/3 damage to random enemy
    @staticmethod
    def mosquito(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], backup: Animal):
        units = agent.team_opposing_(actor).random_units_idx(1)

        if units is None:
            return

        if actor[0] == "team":
            agent.deal_ability_damage_handle_hurt(backup.level,
                                                  backup, ("enemy", units[0]))
        elif actor[0] == "enemy":
            agent.deal_ability_damage_handle_hurt(backup.level,
                                                  backup, ("team", units[0]))

    # buy, give a random friend +1/1, 2/2, 3/3
    @staticmethod
    def otter(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.team.random_friend(actor[1]).permanent_buff(1, 1)
        elif agent.actor(actor).level == 2:
            agent.team.random_friend(actor[1]).permanent_buff(2, 2)
        else:
            agent.team.random_friend(actor[1]).permanent_buff(3, 3)

    # gain extra +1/2/3 gold on sell
    @staticmethod
    def pig(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.gold += 1
        elif agent.actor(actor).level == 2:
            agent.gold += 2
        else:
            agent.gold += 3

    # sloth automatically no ops
    @staticmethod
    def sloth(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass
