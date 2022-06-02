from typing import TYPE_CHECKING, Tuple

from ....game_elements.abstract_elements import Animal
from ....game_elements.game_objects.equipment import Weak, Milk, Better_Milk, Best_Milk

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier5:
    @staticmethod
    def chicken(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.shop.perm_buff(1, 1)
        elif agent.actor(actor).level == 2:
            agent.shop.perm_buff(2, 2)
        else:
            agent.shop.perm_buff(3, 3)

    # add cow's milk to shop
    @staticmethod
    def cow(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        for slot in agent.shop.roster[5:]:
            # guard clause from rest
            if not slot.is_enabled:
                pass

            elif agent.actor(actor).level == 1:
                slot.item = Milk()
            elif agent.actor(actor).level == 2:
                slot.item = Better_Milk()
            elif agent.actor(actor).level == 3:
                slot.item = Best_Milk()

    # deal 7/14/21 damage to last enemy
    @staticmethod
    def crocodile(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        target = agent.team_opposing_(actor).leftmost_unit
        if actor[0] == "team":
            target_tup = ("enemy", agent.team_opposing_(actor).animals.index(target))
        else:
            target_tup = ("team", agent.team_opposing_(actor).animals.index(target))

        agent.deal_ability_damage_handle_hurt(7 * agent.actor(actor).level,
                                              actor, target_tup)

    @staticmethod
    def eagle(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        unit: Animal = agent.shop[0].spawner.spawn_tier(6)

        # set stats with multiplier
        unit.battle_atk *= agent.actor(actor).level
        unit.battle_hp *= agent.actor(actor).level

        if agent.actor(actor).level == 1:
            unit.xp = 0
        if agent.actor(actor).level == 2:
            unit.xp = 2
        if agent.actor(actor).level == 3:
            unit.xp = 5

        agent.summon(unit, actor)

    # limited activation count stored in Goat object
    @staticmethod
    def goat(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.gold += 1

    @staticmethod
    def microbe(agent: 'MessageAgent'):
        for unit in agent.team.units():
            unit.held = Weak()
        for unit in agent.enemy.units():
            unit.held = Weak()

    @staticmethod
    def monkey(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        animal_to_buff = agent.team.rightmost_unit()
        if agent.actor(actor).level == 1:
            agent.buff(animal_to_buff, 2, 2)
        elif agent.actor(actor).level == 2:
            agent.buff(animal_to_buff, 4, 4)
        else:
            agent.buff(animal_to_buff, 6, 6)

    # copy ability should be stored in the parrot object
    @staticmethod
    def parrot(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        # TODO
        pass

    @staticmethod
    def rhino(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        target = agent.team_opposing_(actor).leftmost_unit
        if actor[0] == "team":
            target_tup = ("enemy", agent.team_opposing_(actor).animals.index(target))
        else:
            target_tup = ("team", agent.team_opposing_(actor).animals.index(target))

        agent.deal_ability_damage_handle_hurt(4 * agent.actor(actor).level,
                                              actor, target_tup)

    @staticmethod
    def scorpion(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        pass

    @staticmethod
    def seal(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        friends = agent.team.random_friends(actor[1], 2)
        if agent.actor(actor).level == 1:
            agent.buff(friends, 1, 1)
        elif agent.actor(actor).level == 2:
            agent.buff(friends, 2, 2)
        else:
            agent.buff(friends, 3, 3)

    @staticmethod
    def shark(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.buff(agent.actor(actor), 2, 1)
        elif agent.event_raising_animal.level == 2:
            agent.buff(agent.actor(actor), 4, 2)
        else:
            agent.buff(agent.actor(actor), 6, 3)

    @staticmethod
    def turkey(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.buff(agent.actor(actor), 3, 3)
        elif agent.actor(actor).level == 2:
            agent.buff(agent.actor(actor), 6, 6)
        else:
            agent.buff(agent.actor(actor), 9, 9)
