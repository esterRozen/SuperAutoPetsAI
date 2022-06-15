from threading import Lock
import random as rand
from ..game_elements.abstract_elements import Team
from ..game_elements.game_objects.game_objects import MetaSingleton


class FightBuffer(metaclass=MetaSingleton):
    def __init__(self, limit=500):
        self._stored = []
        self._size = 0
        self._limit = limit
        self._lock = Lock()

    def push(self, team):
        with self._lock:
            if self._size < self._limit:
                self._stored.append(team)
                self._size += 1
            else:
                self._stored[rand.randrange(0, self._limit)] = team

    def pop(self):
        with self._lock:
            if self._size == 0:
                return Team()

            if self._size == 5000:
                self._size -= 1
                return self._stored.pop(rand.randrange(0, self._size))

            return self._stored[rand.randrange(0, self._size)]
