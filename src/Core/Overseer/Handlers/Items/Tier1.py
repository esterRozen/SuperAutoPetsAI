from Core.Overseer.Handlers.Triggers import Triggers
from Core.GameElements.Objects.Base_Pack import ZombieCricket


class Tier1(Triggers):
    def __init__(self, mode):
        super(Tier1, self).__init__(mode)

    def _ant(self):
        # permanently buff random animal on team.
        friend = self.team.random_friend()
        if friend == []:
            return
        if self.lvl == 1:
            self.buff(friend, 2, 1)
        elif self.lvl == 2:
            self.buff(friend, 4, 2)
        else:
            self.buff(friend, 6, 3)

    # on sell give 2 +1/2/3 hp
    def _beaver(self):
        friends = self.team.random_friends(2)
        if friends == []:
            return
        if self.lvl == 1:
            [friend.permanent_buff(1, 0) for friend in friends]
        elif self.lvl == 2:
            [friend.permanent_buff(2, 0) for friend in friends]
        else:
            [friend.permanent_buff(3, 0) for friend in friends]

    def _beetle(self):
        if self.lvl == 1:
            self.shop.buff(0, 1)
        elif self.lvl == 2:
            self.shop.buff(0, 2)
        else:
            self.shop.buff(0, 3)

    # give leftmost friend 1, 2, 3 atk
    def _bluebird(self):
        if self.lvl == 1:
            self.team.leftmost_unit().permanent_buff(1, 0)
        elif self.lvl == 2:
            self.team.leftmost_unit().permanent_buff(2, 0)
        else:
            self.team.leftmost_unit().permanent_buff(3, 0)

    # how to handle summons???
    def _cricket(self):
        unit = ZombieCricket()
        unit.battle_atk = self.lvl
        unit.battle_hp = self.lvl
        self.team.summon(unit, self.team.acting)

    def _duck(self):
        if self.lvl == 1:
            self.shop.buff(1, 1)
        elif self.lvl == 2:
            self.shop.buff(2, 2)
        else:
            self.shop.buff(3, 3)

    # on level give all friends +1/1, +2/2, X
    def _fish(self):
        if self.lvl == 1:
            print("this shouldn't happen! fish lvl 1 trigger")
            return
        if self.lvl == 2:
            self.buff(self.team.friends(), 1, 1)
        elif self.lvl == 3:
            self.buff(self.team.friends(), 2, 2)

    # friend summoned, give +1/2/3 atk until end of battle
    def _horse(self):
        if self.lvl == 1:
            self.team.animals[self.event_raiser].temp_buff(1, 0)
        elif self.lvl == 2:
            self.team.animals[self.event_raiser].temp_buff(2, 0)
        else:
            self.team.animals[self.event_raiser].temp_buff(3, 0)

    # buy food, gain x/x until end of battle
    def _ladybug(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].temp_buff(1, 1)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].temp_buff(2, 2)
        else:
            self.team.animals[self.team.acting].temp_buff(3, 3)

    # start of battle deal 1/2/3 damage to random enemy
    def _mosquito(self):
        # TODO
        pass

    # buy, give a random friend +1/1, 2/2, 3/3
    def _otter(self):
        if self.lvl == 1:
            self.team.random_friend().permanent_buff(1, 1)
        elif self.lvl == 2:
            self.team.random_friend().permanent_buff(2, 2)
        else:
            self.team.random_friend().permanent_buff(3, 3)

    # gain extra +1/2/3 gold on sell
    def _pig(self):
        if self.lvl == 1:
            self.gold += 1
        elif self.lvl == 2:
            self.gold += 2
        else:
            self.gold += 3
        pass

    # sloth automatically no ops
    def _sloth(self):
        pass
