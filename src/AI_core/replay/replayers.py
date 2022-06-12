import collections as coll
import random as rand
from typing import List

Transition = coll.namedtuple('Transition', ('state', 'action', 'next_state', 'reward'))


class ReplayMemory:
    def __init__(self, capacity=5000):
        self.memory = coll.deque([], maxlen=capacity)

    def push(self, *args):
        """
        save a transition
        Args:
            *args: the components of the Transition type
        Returns:
        """
        self.memory.append(Transition(*args))

    def sample(self, batch_size) -> List[Transition]:
        return rand.sample(self.memory, batch_size)

    def __len__(self) -> int:
        return len(self.memory)

    def __getitem__(self, item) -> Transition:
        return self.memory[item]


class MultiChannelReplay:
    def __init__(self, channels: int, capacity=5000):
        self._replayer = [ReplayMemory(capacity) for _ in range(channels)]
        self.__channels = channels

    def push(self, channel, *args):
        self._replayer[channel].push(*args)

    def sample(self, batch_size) -> List[Transition]:
        out = []
        for _ in batch_size:
            i = rand.randrange(0, self.__channels)
            out.append(self._replayer[i].sample(1)[0])

        return out
