from threading import Lock
import random as rand
from typing import Dict, List
import pickle as pkl

from ..game_elements.abstract_elements import Team
from ..game_elements.game_objects.animals import Ant
from ..game_elements.game_objects.game_objects import MetaSingleton

_stored_name = "./pickle/stored_cache"
_size_name = "./pickle/size_cache"


class FightBuffer(metaclass=MetaSingleton):
    def __init__(self, limit=500):
        self._stored: Dict[int, List[Team]] = {turn: [] for turn in range(1, 21)}
        self._size: Dict[int, int] = {turn: 0 for turn in range(1, 21)}
        self._limit = limit
        self._lock = Lock()

    def push(self, team: Team, turn: int):
        with self._lock:
            if self._size[turn] < self._limit:
                self._stored[turn].append(team)
                self._size[turn] += 1
            else:
                self._stored[turn][rand.randrange(0, self._limit)] = team

    def pop(self, turn: int):
        with self._lock:
            if self._size[turn] == 0:
                team = Team()
                team[0] = Ant()
                team[1] = Ant()
                team[2] = Ant()
                return team

            if self._size[turn] == 5000:
                self._size -= 1
                return self._stored[turn].pop(rand.randrange(0, self._size[turn]))

            return self._stored[turn][rand.randrange(0, self._size[turn])]

    def dump_to_cache(self):
        # have to store and load these separately as pickling singletons can be weird.
        with self._lock:
            with open(_stored_name, 'wb') as f:
                pkl.dump(self._stored, f, pkl.HIGHEST_PROTOCOL)

            with open(_size_name, 'wb') as f:
                pkl.dump(self._size, f, pkl.HIGHEST_PROTOCOL)

    def load_cache(self):
        with self._lock:
            with open(_stored_name, 'rb') as f:
                self._stored = pkl.load(f)

            with open(_size_name, 'rb') as f:
                self._size = pkl.load(f)
