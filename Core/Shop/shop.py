from Core.GameElements.spawner import Spawner


class Shop:
    tier = 1

    size_animals = 3
    size_food = 1

    anim = []
    food = []

    def __init__(self, mode):
        self.spawner = Spawner(mode)
        # populate with 3 tier 1 animals and 1 tier 1 food
        # mark all unfrozen
        pass

    def purchase(self, position):
        # remove from shop and return animal
        # if frozen, unfreeze slot
        pass

    def spawn(self):
        pass

    def item(self, position):
        if position >= self.size_animals + self.size_food or position < 0:
            return 0
        if position >= self.size_animals:
            position -= self.size_animals
            return self.food[position]
        return self.anim[position]

    def rank_up(self):
        # increase rank, adjust max size accordingly
        pass

    def reroll(self):
        # populate shop based on current rank and animals frozen
        pass

    @staticmethod
    def freeze(item):
        item.freeze = not item.freeze
        pass


class ShopItem:
    frozen = False

    def __init__(self, item, cost):
        self.item = item
        self.cost = cost
