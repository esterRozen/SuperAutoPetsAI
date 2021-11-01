class Shop:
    tier = 1

    size_animals = 3
    size_food = 1

    anim = []
    food = []

    anim_frozen = []
    food_frozen = []

    def __init__(self):
        # populate with 3 tier 1 animals and 1 tier 1 food
        # mark all unfrozen
        pass

    def purchase(self, position):
        # remove from shop and return animal
        # if frozen, unfreeze slot
        pass

    def spawn(self):
        pass

    def rank_up(self):
        # increase rank, adjust max size accordingly
        pass

    def reroll(self):
        # populate shop based on current rank and animals frozen
        pass

    def freeze(self):
        # toggle whether an animal can be rerolled
        pass
