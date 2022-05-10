from typing import Tuple, Optional, Union
from src.Core import Engine


__all__ = ['Engine_API']


class Engine_API:
    def __init__(self, mode):
        self.__engine = Engine(mode)

    def process_commands(self, command):
        pass

