from typing import TYPE_CHECKING

from ....game_elements.game_objects.base_pack import Bus, Chick
from ....game_elements.game_objects.equipment import Chili

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier4:
    @staticmethod
    def bison(agent: 'MessageAgent'):
        if not agent.team.has_lvl3():
            return
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].permanent_buff(2, 2)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].permanent_buff(4, 4)
        else:
            agent.team.animals[agent.team.acting].permanent_buff(6, 6)

    @staticmethod
    def buffalo(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].permanent_buff(1, 1)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].permanent_buff(2, 2)
        else:
            agent.team.animals[agent.team.acting].permanent_buff(3, 3)

    @staticmethod
    def deer(agent: 'MessageAgent'):
        unit = Bus()
        unit.hp = 5 * agent.lvl
        unit.atk = 5 * agent.lvl
        unit.held = Chili()

        agent.summon(unit)

    @staticmethod
    def dolphin(agent: 'MessageAgent'):
        # TODO
        animal = agent.enemy.lowest_health_unit()
        if agent.lvl == 1:
            pass
        elif agent.lvl == 2:
            pass
        else:
            pass

    @staticmethod
    def hippo(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].temp_buff(2, 2)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].temp_buff(4, 4)
        else:
            agent.team.animals[agent.team.acting].temp_buff(6, 6)

    @staticmethod
    def llama(agent: 'MessageAgent'):
        if agent.team.size() > 4:
            return
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].permanent_buff(2, 2)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].permanent_buff(4, 4)
        else:
            agent.team.animals[agent.team.acting].permanent_buff(6, 6)

    @staticmethod
    def lobster(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.event_raiser].permanent_buff(2, 2)
        elif agent.lvl == 2:
            agent.team.animals[agent.event_raiser].permanent_buff(4, 4)
        else:
            agent.team.animals[agent.event_raiser].permanent_buff(6, 6)
        pass

    @staticmethod
    def penguin(agent: 'MessageAgent'):
        animals_to_buff = agent.team.other_lvl2_or_3()
        if agent.lvl == 1:
            agent.buff(animals_to_buff, 1, 1)
        elif agent.lvl == 2:
            agent.buff(animals_to_buff, 2, 2)
        else:
            agent.buff(animals_to_buff, 3, 3)

    @staticmethod
    def poodle(agent: 'MessageAgent'):
        animals_to_buff = agent.team.ret_diff_tiers()
        if agent.lvl == 1:
            for animal in animals_to_buff:
                animal.permanent_buff(1, 1)
        elif agent.lvl == 2:
            for animal in animals_to_buff:
                animal.permanent_buff(2, 2)
        else:
            for animal in animals_to_buff:
                animal.permanent_buff(3, 3)

    @staticmethod
    def rooster(agent: 'MessageAgent'):
        unit = Chick()
        unit.hp = 1
        unit.atk = agent.event_raising_animal.atk // 2

        for _ in range(agent.lvl):
            agent.summon(unit.__copy__())

    @staticmethod
    def skunk(agent: 'MessageAgent'):
        if agent.event_raiser[0] == "team":
            target = agent.enemy.highest_health_unit()
            target.battle_hp = max(1, target.battle_hp * (agent.lvl / 3))
        else:
            target = agent.team.highest_health_unit()
            target.battle_hp = max(1, target.battle_hp * (agent.lvl / 3))

    @staticmethod
    def squirrel(agent: 'MessageAgent'):
        food_slot = agent.shop.roster[-1]
        for slot in agent.shop.roster:
            slot.item = food_slot.spawn(agent.shop.tier)

    @staticmethod
    def whale(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def worm(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].permanent_buff(1, 1)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].permanent_buff(2, 2)
        else:
            agent.team.animals[agent.team.acting].permanent_buff(3, 3)
