import random
from typing import List, Union

from ..game_objects import GameObjects, pack_names, spawn_groups
from . import Animal, Equipment


# outputs a random animal given a range of tiers
class Spawner:
    def __init__(self, mode: str):
        """
        supports flags based on spawn_groups in game_objects.py
        Args:
            mode: flag
        """
        self._mode = mode
        self._population = []
        if mode in pack_names:
            animals = GameObjects().packs[mode]
            self._population = []
            for tier in animals:
                self._population.append([])
                for animal in tier:
                    if animal.rollable:
                        self._population[-1].append(animal)
        elif mode in spawn_groups:
            items = GameObjects().packs[mode]
            self._population = []
            for tier in items:
                self._population.append([])
                for item in tier:
                    if item.rollable:
                        self._population[-1].append(item)

    def __eq__(self, other: 'Spawner') -> bool:
        return self._mode == other._mode

    def spawn(self, max_tier) -> type(Union[Animal, Equipment]):
        return type(self.spawn_n(1, max_tier)[0])()

    def spawn_n(self, n, max_tier) -> List[type(Union[Animal, Equipment])]:
        max_idx = min(max_tier, 6)
        max_idx = max(max_idx, 1)

        subpopulation = sum(self._population[:max_idx], [])
        sample = random.choices(subpopulation, k=n)
        return [type(instance)() for instance in sample]

    def spawn_tier(self, tier) -> type(Union[Animal, Equipment]):
        idx = tier - 1
        idx = max(idx, 0)
        idx = min(idx, 5)

        subpopulation = self._population[idx]
        return type(random.choice(subpopulation))()
