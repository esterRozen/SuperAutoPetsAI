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
        self._locks: List[Lock] = [Lock() for _ in range(20)]

    def push(self, team: Team, turn: int):
        with self._locks[turn - 1]:
            if self._size[turn] < self._limit:
                self._stored[turn].append(team)
                self._size[turn] += 1
            else:
                self._stored[turn][rand.randrange(0, self._limit)] = team

    def pop(self, turn: int):
        with self._locks[turn - 1]:
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
        locked = self._acquire_all_locks()

        with open(_stored_name, 'wb') as f:
            pkl.dump(self._stored, f, pkl.HIGHEST_PROTOCOL)

        with open(_size_name, 'wb') as f:
            pkl.dump(self._size, f, pkl.HIGHEST_PROTOCOL)

        self._release_all_locks_to_self(locked)

    def load_cache(self):
        locked = self._acquire_all_locks()

        with open(_stored_name, 'rb') as f:
            self._stored = pkl.load(f)

        with open(_size_name, 'rb') as f:
            self._size = pkl.load(f)

        self._release_all_locks_to_self(locked)

    def _acquire_all_locks(self) -> List[Lock]:
        locked = []
        while not self._locks:
            for lock_idx in range(self._locks.__len__() - 1, -1, -1):
                acquired = self._locks[lock_idx].acquire(blocking=False)
                if acquired:
                    locked.append(self._locks.pop(lock_idx))

        return locked

    def _release_all_locks_to_self(self, locks: List[Lock]):
        self._locks = locks
        for lock in self._locks:
            lock.release()
