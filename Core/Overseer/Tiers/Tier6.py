from Core.Overseer.BaseHandler import BaseHandler


class Tier6(BaseHandler):
    # not 100% sure how to implement cat.
    def _cat(self):
        # TODO
        pass

    def _dragon(self):
        if self.lvl == 1:
            self.buff(self.team.friends(), 1, 1)
        elif self.lvl == 2:
            self.buff(self.team.friends(), 2, 2)
        else:
            self.buff(self.team.friends(), 2, 2)

    def _fly(self):
        # TODO
        pass

    def _gorilla(self):
        # TODO
        pass

    def _leopard(self):
        # TODO
        pass

    def _mammoth(self):
        if self.lvl == 1:
            self.buff(self.team.friends(), 2, 2)
        elif self.lvl == 2:
            self.buff(self.team.friends(), 4, 4)
        else:
            self.buff(self.team.friends(), 6, 6)

    def _octopus(self):
        # TODO
        pass

    def _sauropod(self):
        self.gold += 1

    def _snake(self):
        # TODO
        pass

    # how to do this??
    def _tiger(self):
        # TODO
        pass

    def _tyrannosaurus(self):
        if self.gold < 3:
            return
        if self.lvl == 1:
            self.buff(self.team.friends(), 2, 2)
        elif self.lvl == 2:
            self.buff(self.team.friends(), 4, 4)
        else:
            self.buff(self.team.friends(), 6, 6)