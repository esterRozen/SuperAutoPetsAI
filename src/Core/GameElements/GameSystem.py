from Core.GameElements.AbstractElements.SimpleClasses import Empty, Unarmed
from Core.GameElements.AbstractElements.Spawner import Spawner
from Core.GameElements.AbstractElements import Team


class GameSystem():
    def __init__(self, mode):
        self._spawner = Spawner(mode)
        self.team = Team([Empty() for _ in range(5)], [Unarmed() for _ in range(5)])
    pass
