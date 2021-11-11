# must have a way to save and load states
from Core.Overseer import MessageHandler


class Engine:
    def __init__(self, mode):
        self.system = MessageHandler(mode)

    def move_action(self, roster_init, roster_final):
        pass

    def combine_action(self, roster_init, roster_final):
        pass

    def sell_action(self, unit):
        pass

    def buy_action(self, shop_init, roster_final):
        pass

    def freeze_action(self, shop_pos):
        pass

    def reroll_action(self):
        pass

    def end_turn_action(self):
        pass
