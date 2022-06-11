from src.core import Engine

__all__ = ['EngineAPI']


class EngineAPI:
    def __init__(self, mode, limit: int = 50):
        self.__engine = Engine(mode)

        self.__limit = 50
        self.__actions_this_turn = 0

    def process_commands(self, command):
        """
        Processes action state commands into engine readable commands
        Args:
            command:

        Returns:

        """
