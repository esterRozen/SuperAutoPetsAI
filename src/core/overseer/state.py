import numpy as np
from numpy.typing import NDArray
from dataclasses import dataclass

from ..game_elements import Shop
from ..game_elements.abstract_elements import Team
from ..game_elements.game_objects.game_objects import pack_names


@dataclass
class State:
    _mode: str
    _turn: int
    _life: int
    _wins: int
    _gold: int
    _battle_lost: bool
    _team: Team
    _shop: Shop = None

    def __init__(self, mode: str, turn: int, life: int, wins: int, gold: int,
                 battle_lost: bool, team: Team, shop: Shop = None):
        self._mode = mode
        self._turn = turn
        self._life = life
        self._wins = wins
        self._gold = gold
        self._battle_lost = battle_lost
        self._team = team
        self._shop = shop

    def __eq__(self, other: 'State') -> bool:
        if type(other) != type(self):
            return False
        for key in other.__dict__:
            if key in self.__dict__:
                if self.__dict__[key] != other.__dict__[key]:
                    return False
            else:
                return False
        return True

    @property
    def mode(self) -> str:
        return self._mode

    @property
    def turn(self) -> int:
        return self._turn

    @property
    def life(self) -> int:
        return self._life

    @property
    def wins(self) -> int:
        return self._wins

    @property
    def gold(self) -> int:
        return self._gold

    @property
    def battle_lost(self) -> bool:
        return self._battle_lost

    @property
    def team(self) -> Team:
        return self._team

    @property
    def shop(self) -> Shop:
        if self._shop is None:
            return Shop(self.mode, self.turn)
        else:
            return self._shop

    def as_array(self) -> NDArray:
        state_list = []
        # 5 x 7
        for unit in self._team:
            state_list += [unit.id,
                           unit.atk, unit.battle_atk,
                           unit.hp, unit.battle_hp,
                           unit.xp, unit.held.id]

        # 7 x 5
        for slot in self._shop:
            item = slot.item
            state_list += [item.id,
                           item.hp, item.atk,
                           int(slot.is_frozen), item.cost]

        state_list.append(self._gold)
        state_list.append(self._life)
        state_list.append(self._wins)
        state_list.append(self._turn)
        state_list.append(int(self._battle_lost))
        pack_id = pack_names.index(self.mode)
        state_list.append(pack_id)
        return np.array(state_list)
