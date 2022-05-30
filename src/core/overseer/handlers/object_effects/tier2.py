from typing import TYPE_CHECKING

from ....game_elements.abstract_elements import Animal
from ....game_elements.game_objects.animals import Dirty_Rat
from ....game_elements.game_objects.equipment import Weak

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier2:
    @staticmethod
    def bat(agent: 'MessageAgent'):
        units = agent.enemy.random_units(agent.team[agent.event_raiser[1]])
        for unit in units:
            unit.held = Weak()

    @staticmethod
    def crab(agent: 'MessageAgent'):
        battle_hp = agent.acting_team.friend_ahead().battle_hp
        agent.event_raising_animal.battle_hp = battle_hp

    @staticmethod
    def dodo(agent: 'MessageAgent'):
        battle_atk = agent.event_raising_animal.battle_atk
        if agent.event_raising_animal.level == 1:
            agent.acting_team.friend_ahead().battle_atk += battle_atk
        elif agent.event_raising_animal.level == 2:
            agent.acting_team.friend_ahead().battle_atk += 2 * battle_atk
        else:
            agent.acting_team.friend_ahead().battle_atk += 3 * battle_atk

    @staticmethod
    def dirty_rat(agent: 'MessageAgent'):
        # TODO
        return NotImplemented

    @staticmethod
    def dromedary(agent: 'MessageAgent'):
        if agent.event_raising_animal.level == 1:
            agent.shop.buff(1, 1)
        elif agent.event_raising_animal.level == 2:
            agent.shop.buff(2, 2)
        else:
            agent.shop.buff(3, 3)

    @staticmethod
    def elephant(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def flamingo(agent: 'MessageAgent'):
        friends = agent.acting_team.friends_behind(2)
        if agent.event_raising_animal.level == 1:
            agent.buff(friends, 1, 1)
        elif agent.event_raising_animal.level == 2:
            agent.buff(friends, 2, 2)
        else:
            agent.buff(friends, 3, 3)

    # hedgehog has to trigger the hurt trigger!!
    @staticmethod
    def hedgehog(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def peacock(agent: 'MessageAgent'):
        if agent.event_raising_animal.level == 1:
            agent.event_raising_animal.temp_buff(2, 0)
        elif agent.event_raising_animal.level == 2:
            agent.event_raising_animal.temp_buff(4, 0)
        else:
            agent.event_raising_animal.temp_buff(6, 0)

    # summons, ugh
    @staticmethod
    def rat(agent: 'MessageAgent'):
        unit = Dirty_Rat()
        # TODO check the summon hp
        unit.battle_atk = agent.event_raising_animal.level
        unit.battle_hp = agent.event_raising_animal.level
        agent.enemy.summon(unit, 0)

    @staticmethod
    def shrimp(agent: 'MessageAgent'):
        if agent.event_raising_animal.level == 1:
            agent.team.random_friend().temp_buff(0, 1)
        elif agent.event_raising_animal.level == 2:
            agent.team.random_friend().temp_buff(0, 2)
        else:
            agent.team.random_friend().temp_buff(0, 3)

    # more summons!!
    @staticmethod
    def spider(agent: 'MessageAgent'):
        unit: Animal = agent.shop[0].spawner.spawn_tier(3)

        # stats fixed at 2, 2
        unit.battle_atk = 2
        unit.battle_hp = 2

        if agent.event_raising_animal.level == 1:
            unit.xp = 0
        if agent.event_raising_animal.level == 2:
            unit.xp = 2
        if agent.event_raising_animal.level == 3:
            unit.xp = 5

        agent.summon(unit)

    @staticmethod
    def swan(agent: 'MessageAgent'):
        if agent.event_raising_animal.level == 1:
            agent.gold += 1
        elif agent.event_raising_animal.level == 2:
            agent.gold += 2
        else:
            agent.gold += 3

    @staticmethod
    def tabby_cat(agent: 'MessageAgent'):
        if agent.event_raising_animal.level == 1:
            [friend.temp_buff(1, 0) for friend in agent.team.friends()]
        elif agent.event_raising_animal.level == 2:
            [friend.temp_buff(2, 0) for friend in agent.team.friends()]
        else:
            [friend.temp_buff(3, 0) for friend in agent.team.friends()]
