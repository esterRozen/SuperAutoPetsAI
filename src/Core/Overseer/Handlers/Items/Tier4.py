from Core.Overseer.Handlers.triggers import Triggers


class Tier4(Triggers):
    def __init__(self, mode):
        super(Tier4, self).__init__(mode)

    def _bison(self):
        if not self.team.has_lvl3():
            return
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(4, 4)
        else:
            self.team.animals[self.team.acting].permanent_buff(6, 6)

    def _buffalo(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(1, 1)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        else:
            self.team.animals[self.team.acting].permanent_buff(3, 3)

    def _deer(self):
        # TODO
        pass

    def _dolphin(self):
        # TODO
        animal = self.enemy.lowest_health()
        if self.lvl == 1:
            pass
        elif self.lvl == 2:
            pass
        else:
            pass

    def _hippo(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].temp_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].temp_buff(4, 4)
        else:
            self.team.animals[self.team.acting].temp_buff(6, 6)

    def _llama(self):
        if self.team.size() > 4:
            return
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(4, 4)
        else:
            self.team.animals[self.team.acting].permanent_buff(6, 6)

    def _lobster(self):
        if self.lvl == 1:
            self.team.animals[self.event_raiser].permanent_buff(2, 2)
        elif self.lvl == 2:
            self.team.animals[self.event_raiser].permanent_buff(4, 4)
        else:
            self.team.animals[self.event_raiser].permanent_buff(6, 6)
        pass

    def _monkey(self):
        animal_to_buff = self.team.rightmost_unit()
        if self.lvl == 1:
            self.buff(animal_to_buff, 2, 2)
        elif self.lvl == 2:
            self.buff(animal_to_buff, 4, 4)
        else:
            self.buff(animal_to_buff, 6, 6)

    def _penguin(self):
        animals_to_buff = self.team.other_lvl2_or_3()
        if self.lvl == 1:
            self.buff(animals_to_buff, 1, 1)
        elif self.lvl == 2:
            self.buff(animals_to_buff, 2, 2)
        else:
            self.buff(animals_to_buff, 3, 3)

    def _poodle(self):
        animals_to_buff = self.team.ret_diff_tiers()
        if self.lvl == 1:
            for animal in animals_to_buff:
                animal.permanent_buff(1, 1)
        elif self.lvl == 2:
            for animal in animals_to_buff:
                animal.permanent_buff(2, 2)
        else:
            for animal in animals_to_buff:
                animal.permanent_buff(3, 3)

    def _rooster(self):
        # TODO
        pass

    def _skunk(self):
        # TODO
        pass

    def _squirrel(self):
        food_slot = self.shop.roster[-1]
        for slot in self.shop.roster:
            slot.item = food_slot.spawn(self.shop.tier)

    def _worm(self):
        if self.lvl == 1:
            self.team.animals[self.team.acting].permanent_buff(1, 1)
        elif self.lvl == 2:
            self.team.animals[self.team.acting].permanent_buff(2, 2)
        else:
            self.team.animals[self.team.acting].permanent_buff(3, 3)
