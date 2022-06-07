from math import ceil
from typing import TYPE_CHECKING, Tuple

from ....game_elements.abstract_elements import Animal, Equipment
from ....game_elements.game_objects.animals import Bus, Butterfly, Chick
from ....game_elements.game_objects.equipment import Chili

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier4:
    @staticmethod
    def bison(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if not agent.team.has_lvl3:
            return
        if agent.actor(actor).level == 1:
            agent.actor(actor).permanent_buff(2, 2)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).permanent_buff(4, 4)
        else:
            agent.actor(actor).permanent_buff(6, 6)

    @staticmethod
    def buffalo(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(actor).permanent_buff(1, 1)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).permanent_buff(2, 2)
        else:
            agent.actor(actor).permanent_buff(3, 3)

    @staticmethod
    def caterpillar(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(actor).xp += 1
        elif agent.actor(actor).level == 2:
            agent.actor(actor).xp += 1
        else:
            agent.team_of_(actor).animals[actor[1]] = Butterfly()

    @staticmethod
    def deer(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        unit = Bus()

        unit.hp = 5 * fainted.level
        unit.battle_hp = 5 * fainted.level
        unit.atk = 5 * fainted.level
        unit.battle_atk = 5 * fainted.level

        unit.held = Chili()

        agent.summon(unit, actor)

    @staticmethod
    def dolphin(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        animal = agent.team_opposing_(actor).lowest_health_unit()
        if actor[0] == "team":
            target = ("enemy", agent.enemy.animals.index(animal))
        else:
            target = ("team", agent.team.animals.index(animal))

        agent.deal_ability_damage_handle_hurt(5 * agent.actor(actor).level,
                                              actor, target)

    @staticmethod
    def hippo(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        if agent.actor(actor).level == 1:
            agent.actor(actor).temp_buff(3, 3)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).temp_buff(6, 6)
        else:
            agent.actor(actor).temp_buff(9, 9)

    @staticmethod
    def llama(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.team.size > 4:
            return
        if agent.actor(actor).level == 1:
            agent.actor(actor).permanent_buff(2, 2)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).permanent_buff(4, 4)
        else:
            agent.actor(actor).permanent_buff(6, 6)

    @staticmethod
    def lobster(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.shop.buff(2, 2)
        elif agent.actor(actor).level == 2:
            agent.shop.buff(4, 4)
        else:
            agent.shop.buff(6, 6)

    @staticmethod
    def penguin(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        animals_to_buff = agent.team.other_lvl2_or_3(actor[1])
        if agent.actor(actor).level == 1:
            agent.buff(animals_to_buff, 1, 1)
        elif agent.actor(actor).level == 2:
            agent.buff(animals_to_buff, 2, 2)
        else:
            agent.buff(animals_to_buff, 3, 3)

    @staticmethod
    def poodle(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        animals_to_buff = agent.team.ret_diff_tiers()
        if agent.actor(actor).level == 1:
            for animal in animals_to_buff:
                animal.permanent_buff(1, 1)
        elif agent.actor(actor).level == 2:
            for animal in animals_to_buff:
                animal.permanent_buff(2, 2)
        else:
            for animal in animals_to_buff:
                animal.permanent_buff(3, 3)

    @staticmethod
    def rooster(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        unit = Chick()
        unit.hp = 1
        unit.battle_hp = 1
        unit.atk = fainted.atk // 2
        unit.battle_atk = fainted.atk // 2

        for _ in range(fainted.level):
            agent.summon(unit.__copy__(), actor)

    @staticmethod
    def skunk(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        target = agent.team_opposing_(actor).highest_health_unit()
        target.battle_hp = max(1, ceil(target.battle_hp * (agent.actor(actor).level / 3)))

    @staticmethod
    def squirrel(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        for slot in agent.shop.roster:
            if isinstance(slot.item, Equipment):
                slot.item.cost = max(0, slot.item.cost - agent.actor(actor).level)

    @staticmethod
    def whale(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        # TODO
        pass

    @staticmethod
    def worm(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(actor).permanent_buff(1, 1)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).permanent_buff(2, 2)
        else:
            agent.actor(actor).permanent_buff(3, 3)
