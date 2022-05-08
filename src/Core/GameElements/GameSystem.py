from .AbstractElements import Empty, Unarmed, Spawner, Team


class GameSystem:
    def __init__(self, mode):
        self._spawner = Spawner(mode)
        self.team = Team()

