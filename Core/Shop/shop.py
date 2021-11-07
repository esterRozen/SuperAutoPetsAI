from Core.GameElements.spawner import Spawner
from Core.GameElements.simpleClasses import Animal


class Shop:
    def __init__(self, mode, num, tier):
        self._mode = mode
        self._shop_size = num
        self._food_shop_size = 1
        self._tier = tier
        # populate with 3 tier 1 animals and 1 tier 1 food
        # mark all unfrozen

        self.roster = [ShopSlot(mode) for _ in range(num)]
        self.roster += [ShopSlot("food")]

    def summon_level_unit(self):
        # if size < 7, push food over
        if len(self.roster) < 7:
            i = 0
            idx_found = False
            while i < 7 and not idx_found:
                if self.roster[i].mode == "food":
                    idx_found = True
                else:
                    i += 1
            self.roster.insert(i, ShopSlot(self._mode))
            self.roster[i].spawn_tier(self._tier+1)
        else:
            pass

    def clear_unfrozen(self):
        for slot in self.roster:
            if not slot.is_frozen:
                slot.item = None

        j = 0
        for i in range(self._shop_size):
            if self.roster[i].item is not None:
                self.roster[j].item = self.roster[i].item
                j += 1
        # if the first item of the food shop is an animal send it back!!
        if type(self.roster[self._shop_size].item) == Animal:
            self.roster[j].item = self.roster[self._shop_size].item

        j = self._shop_size
        for i in range(self._shop_size, self._shop_size+self._food_shop_size):
            if self.roster[i].item is not None:
                self.roster[j].item = self.roster[i].item

    def clear(self):
        for slot in self.roster:
            slot.item = None

    def fill_shop(self):
        """
        does not replace present items
        :return:
        """
        for slot in self.roster:
            if slot.item is None:
                slot.spawn(self._tier)

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

    def __init__(self, mode):
        self.mode = mode
        self.spawner = Spawner(mode)
        self.item = None

    def toggle_freeze(self):
        self.is_frozen = not self.is_frozen

    def buy(self):
        item = self.item
        self.item = None
        self.is_frozen = False
        return item

    def spawn(self, max_tier):
        self.item = self.spawner.spawn(max_tier)

    def spawn_tier(self, tier):
        self.item = self.spawner.spawn_tier(tier)


class AnimalShopSlot(ShopSlot):
    def __init__(self, item: Animal):
        super(AnimalShopSlot, self).__init__(item)


if __name__ == "__main__":
    a = Shop("base", 3, 1)
    a.roster