from Core.Overseer.Handlers.triggers import Triggers
from Core.GameElements.Objects.Equipment import *


class Equipment(Triggers):
    def __init__(self, mode):
        super(Equipment, self).__init__(mode)

    def apple(self):
        # raise eat food
        self.team.animals[self.team.acting].permanent_buff(1, 1)

    def honey(self):
        # raise eat food
        pass

    def cupcake(self):
        # raise eat food
        self.team.animals[self.team.acting].temp_buff(3, 3)

    def meat_bone(self):
        # raise eat food
        pass

    def sleeping_pill(self):
        # raise eat food
        # raise faint, have variables set properly
        self.event_raiser = self.team.acting
        self.send_engine_message("faint")

    def garlic(self):
        # raise eat food
        pass

    def salad_bowl(self):
        units = self.team.random_units_idx(2)
        for unit in units:
            # raise eat food
            pass



    pass