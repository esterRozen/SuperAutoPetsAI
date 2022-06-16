from threading import Lock
import random as rand
from typing import Dict, List

from ..game_elements.abstract_elements import Team
from ..game_elements.game_objects.game_objects import MetaSingleton


class FightBuffer(metaclass=MetaSingleton):
    def __init__(self, limit=500):
        self._stored: Dict[int, List] = {turn: [] for turn in range(1, 21)}
        self._size: Dict[int, int] = {turn: 0 for turn in range(1, 21)}
        self._limit = limit
        self._lock = Lock()

    def push(self, team, turn: int):
        with self._lock:
            if self._size[turn] < self._limit:
                self._stored[turn].append(team)
                self._size[turn] += 1
            else:
                self._stored[turn][rand.randrange(0, self._limit)] = team

    def pop(self, turn: int):
        with self._lock:
            if self._size[turn] == 0:
                return Team()

            if self._size[turn] == 5000:
                self._size -= 1
                return self._stored[turn].pop(rand.randrange(0, self._size[turn]))

            return self._stored[turn][rand.randrange(0, self._size[turn])]
