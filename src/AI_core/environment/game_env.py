from typing import Optional, Union, Tuple, TypeAlias

import gym
from gym.spaces import MultiDiscrete, Discrete, Dict

from .API import EngineAPI

_num_packs = 2
_num_units = 120
_num_equip = 30
_max_gold = 25
_max_turn = 20

Observe: TypeAlias = gym.spaces.Dict[MultiDiscrete, Discrete]
Action: TypeAlias = gym.spaces.Tuple[Discrete, MultiDiscrete]


class SAPGame(gym.Env):
    def __init__(self, mode):
        self.__engine = EngineAPI(mode)
        self.action_space = Dict({
            "move": MultiDiscrete([5, 5]),
            "combine": MultiDiscrete([5, 5]),
            "sell": Discrete(5),
            "buy": Discrete(7),
            "freeze": Discrete(7),
            "reroll": Discrete(1),
            "end turn": Discrete(1)
        })

        self.observation_space = Dict({
            "team": Dict({
                "slot 1": Dict({
                    "unit": Discrete(_num_units),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "held": Discrete(_num_equip)
                }),
                "slot 2": Dict({
                    "unit": Discrete(_num_units),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "held": Discrete(_num_equip)
                }),
                "slot 3": Dict({
                    "unit": Discrete(_num_units),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "held": Discrete(_num_equip)
                }),
                "slot 4": Dict({
                    "unit": Discrete(_num_units),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "held": Discrete(_num_equip)
                }),
                "slot 5": Dict({
                    "unit": Discrete(_num_units),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "held": Discrete(_num_equip)
                }),
            }),
            "shop": Dict({
                "slot 1": Dict({
                    "item": Discrete(_num_units + _num_equip),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "frozen": Discrete(2),
                    "cost": Discrete(4)
                }),
                "slot 2": Dict({
                    "item": Discrete(_num_units + _num_equip),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "frozen": Discrete(2),
                    "cost": Discrete(4)
                }),
                "slot 3": Dict({
                    "item": Discrete(_num_units + _num_equip),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "frozen": Discrete(2),
                    "cost": Discrete(4)
                }),
                "slot 4": Dict({
                    "item": Discrete(_num_units + _num_equip),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "frozen": Discrete(2),
                    "cost": Discrete(4)
                }),
                "slot 5": Dict({
                    "item": Discrete(_num_units + _num_equip),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "frozen": Discrete(2),
                    "cost": Discrete(4)
                }),
                "slot 6": Dict({
                    "item": Discrete(_num_units + _num_equip),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "frozen": Discrete(2),
                    "cost": Discrete(4)
                }),
                "slot 7": Dict({
                    "item": Discrete(_num_units + _num_equip),
                    "atk": Discrete(50, start=1),
                    "hp": Discrete(50, start=1),
                    "frozen": Discrete(2),
                    "cost": Discrete(4)
                })
            }),
            "gold": Discrete(_max_gold),
            "turn": Discrete(_max_turn, start=1),
            "battle lost": Discrete(2),
            "pack": Discrete(_num_packs)
        })

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
