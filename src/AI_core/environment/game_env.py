from abc import ABC
from typing import Optional, Union, Tuple, TypeAlias

import gym
from gym.spaces import MultiDiscrete, Discrete
from gym.core import ObsType

from .API import EngineAPI


_num_elements = 150
_num_equip = 30
_max_gold = 25
_max_turn = 20


Observe: TypeAlias = gym.spaces.Dict[MultiDiscrete, Discrete]
Action: TypeAlias = gym.spaces.Tuple[Discrete, MultiDiscrete]


class SAPGame(gym.Env):
    def __init__(self, mode):
        self.__engine = EngineAPI(mode)
        self.action_space = gym.spaces.Tuple(
            Discrete(7),                # represents action
            MultiDiscrete([5, 5, 7])    # represents targets TODO double check this
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

    def step(self, action: Action)\
            -> Tuple[Observe, float, bool, dict]:
        """
        Run one timestep of the environment's dynamics. When end of
        episode is reached, you are responsible for calling `reset()`
        to reset this environment's state.

        Accepts an action and returns a tuple (observation, reward, done, info).

        Args:
            action (object): an action provided by the agent

        Returns:
            observation (object): agent's observation of the current environment
            reward (float) : amount of reward returned after previous action
            done (bool): whether the episode has ended, in which case further step() calls will return
            undefined results
            info (dict): contains auxiliary diagnostic information (helpful for debugging, logging,
            and sometimes learning)
        """
        pass

    def reset(self, *, seed: Optional[int] = None, return_info: bool = False, options: Optional[dict] = None)\
            -> Union[Observe, Tuple[Observe, dict]]:
        """
        Resets the environment to an initial state and returns an initial
        observation.

        This method should also reset the environment's random number
        generator(s) if `seed` is an integer or if the environment has not
        yet initialized a random number generator. If the environment already
        has a random number generator and `reset` is called with `seed=None`,
        the RNG should not be reset.
        Moreover, `reset` should (in the typical use case) be called with an
        integer seed right after initialization and then never again.

        Returns:
            observation (object): the initial observation.
            info (optional dictionary): a dictionary containing extra information, this is only returned if
            return_info is set to true
        """
        # Initialize the RNG if the seed is manually passed
        pass

    def render(self, mode="human"):
        """
        Renders the environment.

        The set of supported modes varies per environment. (And some
        third-party environments may not support rendering at all.)
        By convention, if mode is:

        - human: render to the current display or terminal and
          return nothing. Usually for human consumption.
        - rgb_array: Return a numpy.ndarray with shape (x, y, 3),
          representing RGB values for an x-by-y pixel image, suitable
          for turning into a video.
        - ansi: Return a string (str) or StringIO.StringIO containing a
          terminal-style text representation. The text can include newlines
          and ANSI escape sequences (e.g. for colors).

        Note:
            Make sure that your class's metadata 'render_modes' key includes
              the list of supported modes. It's recommended to call super()
              in implementations to use the functionality of this method.

        Args:
            mode (str): the mode to render with
    """
        pass
