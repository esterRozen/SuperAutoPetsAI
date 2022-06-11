from gym.spaces import Dict

from src.core import Engine

__all__ = ['EngineAPI']

_limit = 50


class EngineAPI:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.__actions_this_turn = 0

    def action(self, command):
        """
        Processes action state commands into engine readable commands
        Args:
            command:

        Returns:

        """
        pass

    def shop_action(self, *args):
        pass

    def battle(self):
        pass

    def current_state(self) -> Dict:
        pass

    def reset(self):
        pass
