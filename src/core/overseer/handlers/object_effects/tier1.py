from typing import TYPE_CHECKING

from ....game_elements.game_objects.units import ZombieCricket
if TYPE_CHECKING:
    from ... import MessageAgent


class Tier1:
    @staticmethod
    def nop(agent: 'MessageAgent'):
        return

    @staticmethod
    def ant(agent: 'MessageAgent'):
        #  buff random animal on team.
        friend = agent.team.random_friend()
        if not friend:
            return
        if agent.lvl == 1:
            agent.buff(friend, 2, 1)
        elif agent.lvl == 2:
            agent.buff(friend, 4, 2)
        else:
            agent.buff(friend, 6, 3)

    # on sell give 2 +1/2/3 hp
    @staticmethod
    def beaver(agent: 'MessageAgent'):
        friends = agent.team.random_friends(2)
        if not friends:
            return
        if agent.lvl == 1:
            [friend.permanent_buff(1, 0) for friend in friends]
        elif agent.lvl == 2:
            [friend.permanent_buff(2, 0) for friend in friends]
        else:
            [friend.permanent_buff(3, 0) for friend in friends]

    @staticmethod
    def beetle(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.shop.buff(0, 1)
        elif agent.lvl == 2:
            agent.shop.buff(0, 2)
        else:
            agent.shop.buff(0, 3)

    # give leftmost friend 1, 2, 3 atk
    @staticmethod
    def bluebird(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.leftmost_unit().permanent_buff(1, 0)
        elif agent.lvl == 2:
            agent.team.leftmost_unit().permanent_buff(2, 0)
        else:
            agent.team.leftmost_unit().permanent_buff(3, 0)

    # how to handle summons???
    @staticmethod
    def cricket(agent: 'MessageAgent'):
        unit = ZombieCricket()
        unit.battle_atk = agent.lvl
        unit.battle_hp = agent.lvl
        agent.team.summon(unit, agent.team.acting)

    @staticmethod
    def duck(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.shop.buff(1, 1)
        elif agent.lvl == 2:
            agent.shop.buff(2, 2)
        else:
            agent.shop.buff(3, 3)

    # on level give all friends +1/1, +2/2, X
    @staticmethod
    def fish(agent: 'MessageAgent'):
        if agent.lvl == 1:
            print("this shouldn't happen! fish lvl 1 trigger")
            return
        if agent.lvl == 2:
            agent.buff(agent.team.friends(), 1, 1)
        elif agent.lvl == 3:
            agent.buff(agent.team.friends(), 2, 2)

    # friend summoned, give +1/2/3 atk until end of battle
    @staticmethod
    def horse(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.event_raiser].temp_buff(1, 0)
        elif agent.lvl == 2:
            agent.team.animals[agent.event_raiser].temp_buff(2, 0)
        else:
            agent.team.animals[agent.event_raiser].temp_buff(3, 0)

    # buy food, gain x/x until end of battle
    @staticmethod
    def ladybug(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.animals[agent.team.acting].temp_buff(1, 1)
        elif agent.lvl == 2:
            agent.team.animals[agent.team.acting].temp_buff(2, 2)
        else:
            agent.team.animals[agent.team.acting].temp_buff(3, 3)

    # start of battle deal 1/2/3 damage to random enemy
    @staticmethod
    def mosquito(agent: 'MessageAgent'):
        # TODO
        pass

    # buy, give a random friend +1/1, 2/2, 3/3
    @staticmethod
    def otter(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.team.random_friend().permanent_buff(1, 1)
        elif agent.lvl == 2:
            agent.team.random_friend().permanent_buff(2, 2)
        else:
            agent.team.random_friend().permanent_buff(3, 3)

    # gain extra +1/2/3 gold on sell
    @staticmethod
    def pig(agent: 'MessageAgent'):
        if agent.lvl == 1:
            agent.gold += 1
        elif agent.lvl == 2:
            agent.gold += 2
        else:
            agent.gold += 3
        pass

    # sloth automatically no ops
    @staticmethod
    def sloth(agent: 'MessageAgent'):
        pass
