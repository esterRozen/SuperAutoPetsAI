from Core.GameElements.AbstractElements import Empty, Unarmed, Spawner, Team
from Core.Overseer import MessageAgent


class ShopSystem:
    def __init__(self, agent: MessageAgent):
        self.__agent = agent

    def start_turn(self):
        # load backup team into normal team
        # reset temp stats

        # clear shop

        # events
        # start turn
        pass

    def buy_item(self, item_pos: int, target_pos: int):
        # differentiate between food/equipment and animals!
        # presume it is a valid purchase

        pass
