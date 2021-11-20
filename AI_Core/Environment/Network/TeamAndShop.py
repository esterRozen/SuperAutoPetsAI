import torch
import torch.nn as nn
from AI_Core.Environment.Network.SimpleObjects import Unit


class Team(nn.Module):
    def __init__(self):
        super(Team, self).__init__()
        self.modules = [
            Unit(),
            Unit(),
            Unit(),
            Unit(),
            Unit()
        ]

    def forward(self, roster):
        return [self.modules[i](roster[i]) for i in range(len(roster))]


class Shop(nn.Module):
    def __init__(self):
        super(Shop, self).__init__()
        # food items will be treated as non existent units
        # that are holding an item
        # allows other shop slots to be filled with food items
        # as well.
        self.modules = [
            Unit(),
            Unit(),
            Unit(),
            Unit(),
            Unit(),
            Unit(),
            Unit()
        ]

    def forward(self, roster):
        return [self.modules[i](roster[i][0], roster[i][1]) for i in range(len(roster))]
