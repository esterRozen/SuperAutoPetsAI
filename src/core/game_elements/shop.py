from typing import Union

from .abstract_elements import *


class Shop:
    def __init__(self, mode, num, tier):
        self._mode = mode
        self._shop_size = num
        self._food_shop_size = 1
        self.tier = tier
        self._perm_buff = [0, 0] # atk, hp buff
        # populate with 3 tier 1 animals and 1 tier 1 food
        # mark all unfrozen

        self.roster = [AnimalShopSlot(mode) for _ in range(num)]
        self.roster += [ShopSlot("food")]

    def buff(self, atk, hp):
        # only for animals in current shop
        for i in range(0, self._shop_size):
            self.roster[i].item.permanent_buff(atk, hp)

    def start_turn(self, turn):
        # TODO start_turn flow
        # clear un-frozen animals, shift left

        # check the number of animal shop slots
        # removes excess animal slots if needed

        # spawn new animals

        pass

    def perm_buff(self, atk, hp):
        for i in range(0, self._shop_size):
            new_buff = self.roster[i].perm_buff
            new_buff = [new_buff[0]+atk, new_buff[1]+hp]
            self.roster[i].perm_buff = new_buff
        self.buff(atk, hp)

    def summon_level_unit(self):
        # if size < 7, push food over
        if len(self.roster) < 7:
            i = 0
            idx_found = False
            while i < 7 and not idx_found:
                if not isinstance(self.roster[i], AnimalShopSlot):
                    idx_found = True
                else:
                    i += 1
            self.roster.insert(i, AnimalShopSlot(self._mode))
            self.roster[i].spawn_tier(self.tier + 1)
        else:
            return -1

    def clear_unfrozen(self):
        for slot in self.roster:
            if not slot.is_frozen:
                slot.item = Empty()

        j = 0
        for i in range(self._shop_size):
            if isinstance(self.roster[i].item, Empty):
                self.roster[j].item = self.roster[i].item
                j += 1
        # if the first item of the food shop is an animal send it back!!
        if isinstance(self.roster[self._shop_size].item, Animal):
            self.roster[j].item = self.roster[self._shop_size].item

        j = self._shop_size
        for i in range(self._shop_size, self._shop_size+self._food_shop_size):
            if isinstance(self.roster[i].item, Empty):
                self.roster[j].item = self.roster[i].item

    def clear(self):
        for slot in self.roster:
            slot.item = Empty()

    def fill_shop(self):
        """
        does not replace present items
        :return:
        """
        for slot in self.roster:
            if isinstance(slot.item, Empty):
                slot.spawn(self.tier)

    def item(self, position):
        if position >= self._shop_size or position < 0:
            return 0

        return self.roster[position]

    def grow_shop(self, turn):
        # grow shop depending on turn number
        pass

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
        self.item: Union[Animal, Equipment] = Empty()

    def toggle_freeze(self):
        self.is_frozen = not self.is_frozen

    def buy(self) -> Union[Animal, Equipment]:
        item = self.item
        self.item = Empty()
        self.is_frozen = False
        return item

    def spawn(self, max_tier):
        self.item = self.spawner.spawn(max_tier)

    def spawn_tier(self, tier):
        self.item = self.spawner.spawn_tier(tier)


class AnimalShopSlot(ShopSlot):
    perm_buff = [0, 0]

    def __init__(self, item: Animal):
        super(AnimalShopSlot, self).__init__(item)

    def spawn(self, max_tier):
        self.item = self.spawner.spawn(max_tier)
        self.item.permanent_buff(self.perm_buff[0], self.perm_buff[1])

    def spawn_tier(self, tier):
        self.item = self.spawner.spawn_tier(tier)
        self.item.permanent_buff(self.perm_buff[0], self.perm_buff[1])


if __name__ == "__main__":
    a = Shop("base", 3, 1)
    a.roster
