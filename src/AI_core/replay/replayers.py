import collections as coll
import random as rand
from typing import List, Optional
import numpy as np

Transition = coll.namedtuple('Transition', ('state', 'action', 'reward', 'next_state', 'done'))


def compress_transition(experiences: List[Transition]) -> Transition:
    state = np.concatenate([experience.state for experience in experiences])
    action = np.array([experience.action for experience in experiences])
    reward = np.array([experience.reward for experience in experiences])
    next_state = np.concatenate([experience.next_state for experience in experiences])
    done = np.array([experience.done for experience in experiences])

    return Transition(state, action, reward, next_state, done)


class ReplayMemory:
    def __init__(self, capacity=5000):
        self.memory = coll.deque([], maxlen=capacity)

    def push(self, item):
        """
        save a transition
        Args:
            item: one transition
        Returns:
        """
        self.memory.append(item)

    def sample(self, batch_size) -> List[Transition]:
        return rand.sample(self.memory, batch_size)

    def sample_processed(self, batch_size) -> Transition:
        experiences = self.sample(batch_size)

        return compress_transition(experiences)

    def __len__(self) -> int:
        return len(self.memory)

    def __getitem__(self, item) -> Transition:
        return self.memory[item]


class MultiChannelReplay:
    def __init__(self, channels: int, capacity=5000):
        self._replayers = [ReplayMemory(capacity) for _ in range(channels)]
        self.__channels = channels

    def push(self, channel, *args):
        self._replayers[channel].push(*args)

    def sample(self, batch_size, channel: Optional[int] = None) -> List[Transition]:
        if channel is not None:
            return self._replayers[channel].sample(batch_size)

        out = []
        lens = [replayer.__len__() for replayer in self._replayers]
        samples = sum(lens)
        for _ in range(batch_size):
            idx = rand.randrange(0, samples)
            channel = 0

            while idx > 0:
                idx -= lens[channel]
                channel += 1

            channel -= 1
            idx += lens[channel]
            out.append(self._replayers[channel][idx])

        return out

    def sample_processed(self, batch_size, channel: Optional[int] = None) -> Transition:
        experiences = self.sample(batch_size, channel)

        return compress_transition(experiences)

    def __len__(self):
        return sum([replayer.__len__() for replayer in self._replayers])
