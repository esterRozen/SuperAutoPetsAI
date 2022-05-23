from ..eventnames import *


class ShopSystem:
    def __init__(self, agent):
        """
        Args:
            agent (MessageAgent):

        """
        self.__agent = agent

    def start_turn(self):
        # load backup team into normal team
        # reset temp stats
        self.__agent.load_backup()
        self.__agent.reset_temp_stats()

        # reload shop
        shop = self.__agent.shop
        shop.clear_unfrozen()
        shop.fill_shop()

        # events
        # start turn
        self.__agent.handle_event(START_TURN)

    def freeze(self, pos: int):
        pass

    def reroll(self):
        pass

    def buy(self, item_pos: int, target_pos: int):
        # differentiate between food/equipment and animals!
        # presume it is a valid purchase

        pass

    def sell(self, pos: int):
        pass

    def move(self, roster_init, roster_final):
        pass

    def combine(self, roster_init, roster_final):
        pass

    def end_turn(self):
        # complete end turn effects
        self.__agent.handle_event(END_TURN)
