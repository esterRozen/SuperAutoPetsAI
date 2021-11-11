from Core.Overseer.Handlers.Triggers import Triggers


class Tier5(Triggers):
    def __init__(self, mode):
        super(Tier5, self).__init__(mode)

    def _chicken(self):
        if self.lvl == 1:
            self.shop.perm_buff(1, 1)
        elif self.lvl == 2:
            self.shop.perm_buff(2, 2)
        else:
            self.shop.perm_buff(3, 3)

    # add cow's milk to shop
    def _cow(self):
        # TODO
        pass

    # deal 7/14/21 damage to last enemy
    def _crocodile(self):
        # TODO
        pass

    def _eagle(self):
        # TODO
        pass

    # limited activation count stored in Goat object
    def _goat(self):
        self.gold += 1

    def _microbe(self):
        # TODO
        pass

    # copy ability should be stored in the parrot object
    def _parrot(self):
        # TODO
        pass

    def _rhino(self):
        # TODO
        pass

    def _scorpion(self):
        pass

    def _seal(self):
        friends = self.team.random_friends(2)
        if self.lvl == 1:
            self.buff(friends, 1, 1)
        elif self.lvl == 2:
            self.buff(friends, 2, 2)
        else:
            self.buff(friends, 3, 3)

    def _shark(self):
        if self.lvl == 1:
            self.buff(self.team.animals[self.team.acting], 2, 1)
        elif self.lvl == 2:
            self.buff(self.team.animals[self.team.acting], 4, 2)
        else:
            self.buff(self.team.animals[self.team.acting], 6, 3)

    def _turkey(self):
        if self.lvl == 1:
            self.buff(self.team.animals[self.event_raiser], 3, 3)
        elif self.lvl == 2:
            self.buff(self.team.animals[self.event_raiser], 6, 6)
        else:
            self.buff(self.team.animals[self.event_raiser], 9, 9)
