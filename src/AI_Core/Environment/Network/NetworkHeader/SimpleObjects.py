import torch
import torch.nn as nn
from Core.GameElements.AbstractElements.SimpleClasses import Animal, Equipment


class Unit(nn.Module):
    # 10 dimensions per unit
    # accepts non-tensor input
    def __init__(self):
        super(Unit, self).__init__()
        self.modules = [
            AnimalEmbed().modules,
            ItemEmbed().modules,
            nn.Linear(2, 2)
        ]
        # embedding 1: animal type
        # embedding 2: hold item
        # linear: hp, atk

    def forward(self, animal: Animal, item: Equipment):
        hp_atk_tensor = torch.tensor([animal.hp, animal.atk])
        return [self.modules[0](animal),
                self.modules[1](item),
                self.modules[2](hp_atk_tensor)]


class AnimalEmbed(nn.Module):
    def __init__(self):
        super(AnimalEmbed, self).__init__()
        self.modules = nn.Embedding(80, 5)

    def forward(self, animal: Animal):
        return self.modules(torch.tensor(animal.id))


class ItemEmbed(nn.Module):
    def __init__(self):
        super(ItemEmbed, self).__init__()
        self.modules = nn.Embedding(20, 3)

    def forward(self, item: Equipment):
        return self.modules(torch.tensor(item.id))
