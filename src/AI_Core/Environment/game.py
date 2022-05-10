from abc import ABC
from typing import Optional, Union, Tuple

import gym
from gym.spaces import MultiDiscrete, Discrete
from gym.core import ObsType, ActType


_num_elements = 150
_num_equip = 30
_max_gold = 25
_max_turn = 20


class SAP_Game(gym.Env):
    def __init__(self):
        self.action_space = gym.spaces.Tuple(
            Discrete(7),
            MultiDiscrete([5, 5, 7])
        )
        self.observation_space = gym.spaces.Dict(
            {
                'TeamUnit1': MultiDiscrete([_num_elements, 50, 50, _num_equip]),
                'TeamUnit2': MultiDiscrete([_num_elements, 50, 50, _num_equip]),
                'TeamUnit3': MultiDiscrete([_num_elements, 50, 50, _num_equip]),
                'TeamUnit4': MultiDiscrete([_num_elements, 50, 50, _num_equip]),
                'TeamUnit5': MultiDiscrete([_num_elements, 50, 50, _num_equip]),
                'ShopSlot1': MultiDiscrete([_num_elements, 50, 50]),
                'ShopSlot2': MultiDiscrete([_num_elements, 50, 50]),
                'ShopSlot3': MultiDiscrete([_num_elements, 50, 50]),
                'ShopSlot4': MultiDiscrete([_num_elements, 50, 50]),
                'ShopSlot5': MultiDiscrete([_num_elements, 50, 50]),
                'ShopSlot6': MultiDiscrete([_num_elements, 50, 50]),
                'ShopSlot7': Discrete(_num_equip),
                'ShopSlot8': Discrete(_num_equip),
                'Gold': Discrete(_max_gold),
                'Turn': Discrete(_max_turn)
            }
        )

    def load(self, state):
        pass

    def step(self, action: ActType)\
            -> Tuple[ObsType, float, bool, dict]:
        pass

    def reset(self, *, seed: Optional[int] = None, return_info: bool = False, options: Optional[dict] = None)\
            -> Union[ObsType, Tuple[ObsType, dict]]:
        pass

    def render(self, mode="human"):
        pass
