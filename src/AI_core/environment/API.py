from typing import Tuple, Optional, Union
from src.core import Engine


__all__ = ['EngineAPI']


class EngineAPI:
    def __init__(self, mode):
        self.__engine = Engine(mode)

    def process_commands(self, command):
        pass

