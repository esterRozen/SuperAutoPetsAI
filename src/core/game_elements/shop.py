from typing import Union, Tuple, List

from .abstract_elements import *


class Shop:
    def __init__(self, mode: str, turn: int):
        self._turn = turn
        self._mode = mode

        # permanent buff for all future animals spawned
        self._perm_buff = [0, 0]

        self._animal_slots, self._item_slots, self.tier = Shop.shop_params(turn)

        self.roster: List[ShopSlot] = [AnimalShopSlot(mode) for _ in range(self._animal_slots)]
        self.roster += [ShopSlot("food") for _ in range(self._item_slots)]

        self.fill_shop()

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.roster[item]
        else:
            raise ValueError("Must be int as index of shop roster")

    def __iter__(self):
        for slot in self.roster:
            yield slot

    def __repr__(self):
        rep = f"Shop[perm:({self._perm_buff[0]}, {self._perm_buff[1]}), roster: ("
        slots: List[str] = [slot.__repr__() for slot in self]
        rep += ", ".join(slots)

        rep += ")]"
        return rep

    def buff(self, atk, hp):
        # only for animals in current shop
        for shop_slot in self.roster:
            if isinstance(shop_slot.item, Animal):
                shop_slot.item.permanent_buff(atk, hp)

    def start_turn(self):
        # grow shop size
        self._turn += 1
        self.upgrade_shop(self._turn)

        # clear un-frozen animals, shift left
        self.clear_unfrozen()

        # spawn new animals
        self.fill_shop()
        return

    def perm_buff(self, atk, hp):
        self.buff(atk, hp)
        self._perm_buff = [self._perm_buff[0] + atk, self._perm_buff[1] + hp]
        for shop_slot in self.roster:
            if isinstance(shop_slot, AnimalShopSlot):
                shop_slot.perm_buff = self._perm_buff

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
        """
        clears all unfrozen items in shop
        shifts animals left, foods right
        Returns:

        """
        for slot in self.roster:
            if not slot.is_frozen:
                slot.clear()

        animals = []
        items = []
        for shop_slot in self.roster:
            if isinstance(shop_slot.item, Animal) and not isinstance(shop_slot.item, Empty):
                animals += [shop_slot.item]
                shop_slot.clear()
            if isinstance(shop_slot.item, Equipment) and not isinstance(shop_slot.item, Unarmed):
                items += [shop_slot.item]
                shop_slot.clear()

        j = 0
        while animals:
            self.roster[j].item = animals.pop()
            j += 1

        j = len(self.roster) - 1
        while items:
            self.roster[j].item = items.pop(-1)
            j -= 1

    def clear(self):
        for slot in self.roster:
            slot.clear()
        return

    def fill_shop(self):
        """
        does not replace present items
        :return:
        """
        for slot in self.roster:
            if isinstance(slot.item, Empty) or isinstance(slot.item, Unarmed):
                slot.spawn(self.tier)

    def item(self, position):
        if position >= len(self.roster) or position < 0:
            return Empty()

        return self.roster[position]

    def upgrade_shop(self, turn):
        """
        handles upgrading animal slots, food slots, and current tier
        uses state transition as basis for updates
        Args:
            turn: int - turn number

        Returns:

        """
        curr = Shop.shop_params(turn)
        prev = Shop.shop_params(turn - 1)

        # add animal slot
        if curr[0] - prev[0]:
            new_animal_slot = AnimalShopSlot(self._mode)
            new_animal_slot.perm_buff = self._perm_buff
            self.roster.insert(prev[0], new_animal_slot)

        # add item slot
        if curr[1] - prev[1]:
            new_item_slot = ShopSlot(self._mode)
            self.roster.insert(len(self.roster)-prev[1])
            pass

        # raise tier
        if curr[2] - prev[2]:
            self.tier = curr[2]

    def reroll(self):
        # populate shop based on current rank and animals frozen
        self.clear_unfrozen()
        self.fill_shop()
        pass

    @staticmethod
    def shop_params(turn: int) -> Tuple[int, int, int]:
        """

        Args:
            turn:

        Returns: Tuple of ints -> animal slots, food slots, tier

        """
        animal_slots = min((turn - 1)//4 + 3, 5)
        item_slots = min((turn - 1)//2 + 1, 2)
        tier = min((turn - 1)//2 + 1, 6)

        return animal_slots, item_slots, tier

    def toggle_freeze(self, pos: int):
        self.roster[pos].toggle_freeze()
        return


class ShopSlot:
    is_frozen = False

    def __init__(self, mode):
        self.mode = mode
        self.spawner = Spawner(mode)
        self.item: Union[Animal, Equipment] = Empty()

    def __repr__(self):
        return f"[{self.is_frozen}, {self.item.__repr__()}]"

    def clear(self):
        self.item = Unarmed()
        return

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

    def __init__(self, mode: str):
        super(AnimalShopSlot, self).__init__(mode)

    def clear(self):
        self.item = Empty()
        return

    def spawn(self, max_tier):
        self.item = self.spawner.spawn(max_tier)
        self.item.permanent_buff(self.perm_buff[0], self.perm_buff[1])

    def spawn_tier(self, tier):
        self.item = self.spawner.spawn_tier(tier)
        self.item.permanent_buff(self.perm_buff[0], self.perm_buff[1])
