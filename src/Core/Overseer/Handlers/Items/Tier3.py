from Core.Overseer.Handlers.Triggers import Triggers


class Tier3(Triggers):
    def __init__(self, mode):
        super(Tier3, self).__init__(mode)

    # triggers hurt ugh
    def _badger(self):
        # TODO
        pass

    # triggers hurt
    def _blowfish(self):
        # TODO
        pass

    def _camel(self):
        if self.lvl == 1:
            self.buff(self.team.friend_behind(), 1, 2)
        elif self.lvl == 2:
            self.buff(self.team.friend_behind(), 2, 4)
        else:
            self.buff(self.team.friend_behind(), 3, 6)

    def _caterpillar(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].xp += 1
        elif self.lvl == 2:
            self.team.animals[self.team.acting].xp += 1
        else:
            # TODO caterpillar level 3
            pass

    def _giraffe(self):
        if self.lvl == 1:
            self.buff(self.team.friends_ahead(1), 1, 1)
        elif self.lvl == 2:
            self.buff(self.team.friends_ahead(2), 1, 1)
        else:
            self.buff(self.team.friends_ahead(3), 1, 1)

    def _hatching_chick(self):
        if self.lvl == 1:
            self.team.friend_ahead().temp_buff(5, 5)
        elif self.lvl == 2:
            self.team.friend_ahead().permanent_buff(2, 2)
        else:
            self.team.friend_ahead().increase_xp(1)

    def _kangaroo(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].temp_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].temp_buff(4, 4)
        else:
            self.team.animals[self.team.acting].temp_buff(6, 6)

    def _owl(self):
        if self.lvl == 1:
            self.team.random_friend().permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.random_friend().permanent_buff(4, 4)
        else:
            self.team.random_friend().permanent_buff(6, 6)

    def _ox(self):
        # TODO
        pass

    def _puppy(self):
        if self.gold < 2:
            return
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(4, 4)
        else:
            self.team.animals[self.team.acting].permanent_buff(6, 6)

    def _rabbit(self):
        if self.lvl == 1:
            self.team.animals[self.event_raiser].permanent_buff(0, 1)
        elif self.lvl == 2:
            self.team.animals[self.event_raiser].permanent_buff(0, 2)
        else:
            self.team.animals[self.event_raiser].permanent_buff(0, 3)

    def _sheep(self):
        # TODO
        pass

    def _snail(self):
        if not self.battle_lost:
            return
        if self.lvl == 1:
            self.buff(self.team.friends(), 2, 1)
        elif self.lvl == 2:
            self.buff(self.team.friends(), 4, 2)
        else:
            self.buff(self.team.friends(), 6, 3)

    def _tropical_fish(self):
        if self.lvl == 1:
            self.team.friend_ahead().permanent_buff(0, 1)
            self.team.friend_behind().permanent_buff(0, 1)
        elif self.lvl == 2:
            self.team.friend_ahead().permanent_buff(0, 2)
            self.team.friend_behind().permanent_buff(0, 2)
        else:
            self.team.friend_ahead().permanent_buff(0, 3)
            self.team.friend_behind().permanent_buff(0, 3)

    def _turtle(self):
        # TODO
        pass

    def _whale(self):
        # TODO
        pass