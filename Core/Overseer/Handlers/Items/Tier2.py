from Core.Overseer.Handlers.Triggers import Triggers


class Tier2(Triggers):
    def __init__(self, mode):
        super(Tier2, self).__init__(mode)

    # have to implement equipments
    def _bat(self):
        # TODO
        pass

    def _crab(self):
        battle_hp = self.team.friend_ahead().battle_hp
        self.team.animals[self.team.acting].battle_hp = battle_hp

    def _dodo(self):
        battle_atk = self.team.animals[self.team.acting].battle_atk
        if self.lvl == 1:
            self.team.friend_ahead().battle_atk += battle_atk
        elif self.lvl == 2:
            self.team.friend_ahead().battle_atk += 2 * battle_atk
        else:
            self.team.friend_ahead().battle_atk += 3 * battle_atk

    def _dog(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(1, 1)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        else:
            self.team.animals[self.team.acting].permanent_buff(3, 3)

    def _dromedary(self):
        if self.lvl == 1:
            self.shop.buff(1, 1)
        elif self.lvl == 2:
            self.shop.buff(2, 2)
        else:
            self.shop.buff(3, 3)

    def _elephant(self):
        # TODO
        pass

    def _flamingo(self):
        friends = self.team.friends_behind(2)
        if self.lvl == 1:
            self.buff(friends, 1, 1)
        elif self.lvl == 2:
            self.buff(friends, 2, 2)
        else:
            self.buff(friends, 3, 3)

    # hedgehog has to trigger the hurt trigger!!
    def _hedgehog(self):
        # TODO
        pass

    def _peacock(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].temp_buff(2, 0)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].temp_buff(4, 0)
        else:
            self.team.animals[self.team.acting].temp_buff(6, 0)

    # summons, ugh
    def _rat(self):
        # TODO
        pass

    def _shrimp(self):
        if self.lvl == 1:
            self.team.random_friend().temp_buff(0, 1)
        elif self.lvl == 2:
            self.team.random_friend().temp_buff(0, 2)
        else:
            self.team.random_friend().temp_buff(0, 3)

    # more summons!!
    def _spider(self):
        # TODO
        pass

    def _swan(self):
        if self.lvl == 1:
            self.gold += 1
        elif self.lvl == 2:
            self.gold += 2
        else:
            self.gold += 3

    def _tabby_cat(self):
        if self.lvl == 1:
            [friend.temp_buff(1, 0) for friend in self.team.friends()]
        elif self.lvl == 2:
            [friend.temp_buff(2, 0) for friend in self.team.friends()]
        else:
            [friend.temp_buff(3, 0) for friend in self.team.friends()]
