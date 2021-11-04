from Core.GameElements.spawner import Spawner
from Core.GameElements.simpleClasses import Animal


class Shop:
    def __init__(self, mode, num, tier):
        self._spawner = Spawner(mode)
        self._shop_size = num
        self._tier = tier
        # populate with 3 tier 1 animals and 1 tier 1 food
        # mark all unfrozen
        if mode == "paid_1" or mode == "base":
            slot = AnimalShopSlot
        elif mode == "food":
            slot = ShopSlot
        else:
            raise ValueError
        self.roster = [slot(item) for item in self._spawner.spawn_n(num, tier)]

    def summon_level_unit(self):
        unit = self._spawner.spawn_tier(self._tier+1)

    def clear_unfrozen(self):
        for slot in self.roster:
            if not slot.is_frozen:
                slot.item = None
        return

    def fill_shop(self):
        """
        does not replace present items
        :return:
        """
        for slot in self.roster:
            if slot.item is None:
                slot.item = self._spawner
        pass

    def item(self, position):
        if position >= self._shop_size or position < 0:
            return 0

        return self.roster[position]

    def grow_shop(self):
        self._shop_size += 1

    def reroll(self):
        # populate shop based on current rank and animals frozen
        self.clear_unfrozen()
        self.fill_shop()
        pass

    @staticmethod
    def freeze(item):
        item.freeze = not item.freeze
        pass


class ShopSlot:
    is_frozen = False

    def __init__(self, item):
        self.item = item

    def toggle_freeze(self):
        self.is_frozen = not self.is_frozen

    def buy(self):
        item = self.item
        self.item = None
        self.is_frozen = False
        return item


class AnimalShopSlot(ShopSlot):
    def __init__(self, item: Animal):
        super(AnimalShopSlot, self).__init__(item)


if __name__ == "__main__":
    a = Shop("base", 3, 1)
    a.roster