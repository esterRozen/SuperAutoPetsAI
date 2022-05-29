from typing import Union, Tuple, List

from .abstract_elements import *


class Shop:
    def __init__(self, mode: str, turn: int):
        """
        supports flags:
            "base pack"
            "paid pack 1"
        Args:
            mode: flag
            turn: turn number to initialize at
        """

        self._turn = turn
        self._mode = mode

        # permanent buff for all future animals spawned
        self._perm_buff = [0, 0]

        self._animal_slots, self._item_slots, self.tier = Shop.shop_params(turn)

        self.roster: List[ShopSlot] = [AnimalShopSlot(mode) for _ in range(self._animal_slots)]
        for _ in range(5 - self._animal_slots):
            slot = AnimalShopSlot(mode)
            slot.is_enabled = False
            self.roster.append(slot)

        self.roster += [ShopSlot(mode + " items") for _ in range(self._item_slots)]
        for _ in range(2 - self._item_slots):
            slot = ShopSlot(mode + " items")
            slot.is_enabled = False
            self.roster.append(slot)

        self.fill_shop()

    def __delitem__(self, key):
        self.roster[key].clear()

    def __getitem__(self, item: int):
        return self.roster[item]

    def __iter__(self):
        for slot in self.roster:
            yield slot

    def __repr__(self):
        rep = f"Shop[perm:({self._perm_buff[0]}, {self._perm_buff[1]}), roster: ("
        slots: List[str] = [slot.__repr__() for slot in self]
        rep += ", ".join(slots)

        rep += ")]"
        return rep

    def __setitem__(self, key: int, value: Union[Animal, Equipment]):
        self.roster[key].item = value

    @property
    def size(self):
        j = 0
        for slot in self.roster:
            if not isinstance(slot.item, Empty) and not isinstance(slot.item, Unarmed):
                j += 1
        return j

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

    def summon_level_unit(self) -> bool:
        tier_summoned = min(6, self.tier + 1)

        # if size < 7, push food over *if necessary*
        if self.size < 7:
            i = 0
            idx_found = False
            while i < 7 and not idx_found:
                if isinstance(self.roster[i].item, Empty):
                    idx_found = True
                elif not isinstance(self.roster[i], AnimalShopSlot):
                    if isinstance(self.roster[i].item, Unarmed):
                        idx_found = True
                    else:
                        i += 1
                else:
                    i += 1

            if i == 7:
                return False
            if i <= 5:
                self.roster[i].item = self.roster[0].spawner.spawn_tier(tier_summoned)
                return True
            if i == 6:
                self.roster[i].item = self.roster[5].item
                self.roster[5].item = self.roster[0].spawner.spawn_tier(tier_summoned)
                return True
        else:
            return False

    def clear_unfrozen(self):
        """
        clears all unfrozen items in shop
        shifts and food left
        Returns:

        """
        for slot in self.roster:
            if not slot.is_frozen:
                slot.clear()

        animals = []
        items = []
        for shop_slot in self.roster:
            if isinstance(shop_slot.item, Animal) and not isinstance(shop_slot.item, Empty):
                animals.append(shop_slot.item)
                shop_slot.clear()
                shop_slot.toggle_freeze()
            if isinstance(shop_slot.item, Equipment) and not isinstance(shop_slot.item, Unarmed):
                items.append(shop_slot.item)
                shop_slot.clear()
                shop_slot.toggle_freeze()

        j = 0
        while animals:
            self.roster[j].item = animals.pop(0)
            self.roster[j].toggle_freeze()
            j += 1

        j = 5
        while items:
            self.roster[j].item = items.pop(0)
            self.roster[j].toggle_freeze()
            j += 1

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

    def upgrade_shop(self, turn):
        """
        handles upgrading animal slots, food slots, and current tier
        uses state transition as basis for updates
        Args:
            turn: int - turn number

        Returns:

        """
        curr = Shop.shop_params(turn)

        # add animal slot
        animal_slot_idx = curr[0]-1
        self.roster[animal_slot_idx].is_enabled = True

        # add item slot
        item_slot_idx = 4 + curr[1]
        self.roster[item_slot_idx].is_enabled = True

        # raise tier
        self.tier = curr[2]

    def reroll(self):
        # populate shop based on current rank and animals frozen
        self.clear_unfrozen()
        self.fill_shop()

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
    is_enabled = True

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
        if not self.is_enabled:
            return
        self.is_frozen = not self.is_frozen

    def buy(self) -> Union[Animal, Equipment]:
        item = self.item
        self.item = Empty()
        self.is_frozen = False
        return item

    def spawn(self, max_tier):
        if not self.is_enabled:
            return
        self.item = self.spawner.spawn(max_tier)

    def spawn_tier(self, tier):
        if not self.is_enabled:
            return
        self.item = self.spawner.spawn_tier(tier)


class AnimalShopSlot(ShopSlot):
    perm_buff = [0, 0]

    def __init__(self, mode: str):
        super(AnimalShopSlot, self).__init__(mode)

    def clear(self):
        self.item = Empty()
        return

    def spawn(self, max_tier):
        if not self.is_enabled:
            return
        self.item = self.spawner.spawn(max_tier)
        self.item.permanent_buff(self.perm_buff[0], self.perm_buff[1])

    def spawn_tier(self, tier):
        if not self.is_enabled:
            return
        self.item = self.spawner.spawn_tier(tier)
        self.item.permanent_buff(self.perm_buff[0], self.perm_buff[1])
