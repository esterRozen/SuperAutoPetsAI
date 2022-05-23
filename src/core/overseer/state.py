from dataclasses import dataclass

from ..game_elements import Shop
from ..game_elements.abstract_elements import Team


@dataclass
class State:
    mode: str
    turn: int
    life: int
    battle_lost: bool
    team: Team
    shop: Shop = None
    gold: int = 10
