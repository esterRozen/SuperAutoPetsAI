import collections as coll
import random as rand
from typing import List, Optional

Transition = coll.namedtuple('Transition', ('state', 'action', 'reward', 'next_state', 'done'))


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

        state = [experience.state for experience in experiences]
        action = [experience.action for experience in experiences]
        reward = [experience.reward for experience in experiences]
        next_state = [experience.next_state for experience in experiences]
        done = [experience.done for experience in experiences]

        return Transition(state, action, next_state, reward, done)

    def __len__(self):
        return sum([replayer.__len__() for replayer in self._replayers])