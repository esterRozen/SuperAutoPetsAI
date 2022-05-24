from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier2:
    # have to implement equipments
    @staticmethod
    def bat(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def crab(agent: 'MessageAgent'):
        battle_hp = agent.team.friend_ahead().battle_hp
        agent.team.animals[agent.team.acting].battle_hp = battle_hp

    @staticmethod
    def dodo(agent: 'MessageAgent'):
        battle_atk = agent.team.animals[agent.team.acting].battle_atk
        if agent.lvl == 1:
            agent.team.friend_ahead().battle_atk += battle_atk
        elif agent.lvl == 2:
            agent.team.friend_ahead().battle_atk += 2 * battle_atk
        else:
            agent.team.friend_ahead().battle_atk += 3 * battle_atk

    @staticmethod
    def dirty_rat(agent: 'MessageAgent'):
        return NotImplemented

    @staticmethod
    def dromedary(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.shop.buff(1, 1)
        elif agent.lvl == 2:
            agent.shop.buff(2, 2)
        else:
            agent.shop.buff(3, 3)

    @staticmethod
    def elephant(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def flamingo(agent: 'MessageAgent'):
        friends = agent.team.friends_behind(2)
        if agent.lvl == 1:
            agent.buff(friends, 1, 1)
        elif agent.lvl == 2:
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
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].temp_buff(2, 0)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].temp_buff(4, 0)
        else:
            agent.team.animals[agent.team.acting].temp_buff(6, 0)

    # summons, ugh
    @staticmethod
    def rat(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def shrimp(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.random_friend().temp_buff(0, 1)
        elif agent.lvl == 2:
            agent.team.random_friend().temp_buff(0, 2)
        else:
            agent.team.random_friend().temp_buff(0, 3)

    # more summons!!
    @staticmethod
    def spider(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def swan(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.gold += 1
        elif agent.lvl == 2:
            agent.gold += 2
        else:
            agent.gold += 3

    @staticmethod
    def tabby_cat(agent: 'MessageAgent'):
        if agent.lvl == 1:
            [friend.temp_buff(1, 0) for friend in agent.team.friends()]
        elif agent.lvl == 2:
            [friend.temp_buff(2, 0) for friend in agent.team.friends()]
        else:
            [friend.temp_buff(3, 0) for friend in agent.team.friends()]
