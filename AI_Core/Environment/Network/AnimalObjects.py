import torch
import torch.nn as nn
from Core.GameElements.SimpleClasses import Animal, Equipment


class Animal(nn.Module):
    def __init__(self):
        super(Animal, self).__init__()
        self.modules = [
            nn.Embedding(80, 5),
            nn.Embedding(20, 3),
            nn.Linear(2, 2)
        ]
        # embedding 1: animal type
        # embedding 2: hold item
        # linear: hp, atk

    def forward(self, animal: Animal, item: Equipment):
        animal_embed = self.modules[0](animal.id)
        item_embed = self.modules[1](item.id)
        return [animal_embed, item_embed, self.modules[2]([animal.hp, animal.atk])]
