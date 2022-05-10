from .AbstractElements import Empty, Unarmed, Spawner, Team
from ..Overseer import MessageAgent


class GameSystem:
    def __init__(self, agent: MessageAgent):
        self.__agent = agent
