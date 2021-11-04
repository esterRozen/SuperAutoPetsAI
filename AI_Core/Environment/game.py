from abc import ABC

import gym
from gym import spaces


class SAP_Game(gym.Env):
    def __init__(self):
        self.action_space = spaces.Tuple(
            spaces.Discrete(7),
            spaces.MultiDiscrete([5, 5, 7])
        )
        self.observation_space = spaces.Dict(
            {
                'TeamUnit1': spaces.MultiDiscrete([80, 50, 50, 8]),
                'TeamUnit2': spaces.MultiDiscrete([80, 50, 50, 8]),
                'TeamUnit3': spaces.MultiDiscrete([80, 50, 50, 8]),
                'TeamUnit4': spaces.MultiDiscrete([80, 50, 50, 8]),
                'TeamUnit5': spaces.MultiDiscrete([80, 50, 50, 8]),
                'ShopSlot1': spaces.MultiDiscrete([80, 50, 50]),
                'ShopSlot2': spaces.MultiDiscrete([80, 50, 50]),
                'ShopSlot3': spaces.MultiDiscrete([80, 50, 50]),
                'ShopSlot4': spaces.MultiDiscrete([80, 50, 50]),
                'ShopSlot5': spaces.MultiDiscrete([80, 50, 50]),
                'ShopSlot6': spaces.MultiDiscrete([80, 50, 50]),
                'ShopSlot7': spaces.Discrete(15),
                'ShopSlot8': spaces.Discrete(15)
            }
        )

    def reset(self):
        pass

    def step(self, action):
        # return state, reward, done, info
        pass

    def load(self, state):
        pass

    def render(self, mode="human"):
        pass
