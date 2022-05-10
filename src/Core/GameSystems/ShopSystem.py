from Core.GameElements.AbstractElements import Empty, Unarmed, Spawner, Team
from Core.Overseer import MessageAgent


class ShopSystem:
    def __init__(self, agent: MessageAgent):
        self.__agent = agent
