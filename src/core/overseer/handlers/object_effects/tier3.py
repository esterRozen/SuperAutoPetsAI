from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier3:
    # triggers hurt ugh
    @staticmethod
    def badger(agent: 'MessageAgent'):
        # TODO
        pass

    # triggers hurt
    @staticmethod
    def blowfish(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def camel(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.buff(agent.team.friend_behind(), 1, 2)
        elif agent.lvl == 2:
            agent.buff(agent.team.friend_behind(), 2, 4)
        else:
            agent.buff(agent.team.friend_behind(), 3, 6)

    @staticmethod
    def caterpillar(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].xp += 1
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].xp += 1
        else:
            # TODO caterpillar level 3
            pass

    @staticmethod
    def dog(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].permanent_buff(1, 1)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].permanent_buff(2, 2)
        else:
            agent.team.animals[agent.team.acting].permanent_buff(3, 3)

    @staticmethod
    def giraffe(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.buff(agent.team.friends_ahead(1), 1, 1)
        elif agent.lvl == 2:
            agent.buff(agent.team.friends_ahead(2), 1, 1)
        else:
            agent.buff(agent.team.friends_ahead(3), 1, 1)

    @staticmethod
    def hatching_chick(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.friend_ahead().temp_buff(5, 5)
        elif agent.lvl == 2:
            agent.team.friend_ahead().permanent_buff(2, 2)
        else:
            agent.team.friend_ahead().increase_xp(1)

    @staticmethod
    def kangaroo(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].temp_buff(2, 2)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].temp_buff(4, 4)
        else:
            agent.team.animals[agent.team.acting].temp_buff(6, 6)

    @staticmethod
    def owl(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.random_friend().permanent_buff(2, 2)
        elif agent.lvl == 2:
            agent.team.random_friend().permanent_buff(4, 4)
        else:
            agent.team.random_friend().permanent_buff(6, 6)

    @staticmethod
    def ox(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def puppy(agent: 'MessageAgent'):
        if agent.gold < 2:
            return
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].permanent_buff(2, 2)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].permanent_buff(4, 4)
        else:
            agent.team.animals[agent.team.acting].permanent_buff(6, 6)

    @staticmethod
    def rabbit(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.event_raiser].permanent_buff(0, 1)
        elif agent.lvl == 2:
            agent.team.animals[agent.event_raiser].permanent_buff(0, 2)
        else:
            agent.team.animals[agent.event_raiser].permanent_buff(0, 3)

    @staticmethod
    def sheep(agent: 'MessageAgent'):
        # TODO
        pass

    @staticmethod
    def snail(agent: 'MessageAgent'):
        if not agent.battle_lost:
            return
        if agent.lvl == 1:
            agent.buff(agent.team.friends(), 2, 1)
        elif agent.lvl == 2:
            agent.buff(agent.team.friends(), 4, 2)
        else:
            agent.buff(agent.team.friends(), 6, 3)

    @staticmethod
    def tropical_fish(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.friend_ahead().permanent_buff(0, 1)
            agent.team.friend_behind().permanent_buff(0, 1)
        elif agent.lvl == 2:
            agent.team.friend_ahead().permanent_buff(0, 2)
            agent.team.friend_behind().permanent_buff(0, 2)
        else:
            agent.team.friend_ahead().permanent_buff(0, 3)
            agent.team.friend_behind().permanent_buff(0, 3)

    @staticmethod
    def turtle(agent: 'MessageAgent'):
        # TODO
        pass
