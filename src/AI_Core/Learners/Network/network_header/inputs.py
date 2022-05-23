from typing import List, TypeAlias

from src.core.game_elements.abstract_elements import Animal, Equipment


AnimalEmbed: TypeAlias = List[float]
ItemEmbed: TypeAlias = List[float]
TeamEmbed: TypeAlias = List[float]


def animal_embed(animal: Animal) -> AnimalEmbed:
    return [float(animal.id), float(animal.battle_hp), float(animal.battle_atk)]


def item_embed(equip: Equipment) -> ItemEmbed:
    return [float(equip.id)]


def team_embed(animals: List[AnimalEmbed], items: List[ItemEmbed]):
    out = []
    for animal in animals:
        out += animal
    for item in items:
        out += item
    return out


def shop_embed(costs: List[int], animals: List[AnimalEmbed], items: List[ItemEmbed]) -> List[float]:
    out = []
    shop = animals + items
    for i, cost in enumerate(costs):
        out += cost
        out += shop[i]
    return out


def state_embed():
    pass
