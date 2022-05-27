from unittest import TestCase

from src.core.game_elements.abstract_elements import Animal
from src.core.game_elements.abstract_elements import Empty, Unarmed
from src.core.game_elements import Shop


class TestShop(TestCase):
    def test_buff(self):
        shop = Shop("base", 1)
        atk1 = shop[0].item.atk
        atk2 = shop[2].item.atk

        hp1 = shop[0].item.hp
        hp2 = shop[2].item.hp

        shop.buff(2, 1)

        self.assertTrue(atk1 + 2 == shop[0].item.atk)
        self.assertTrue(atk2 + 2 == shop[2].item.atk)
        self.assertTrue(hp1 + 1 == shop[0].item.hp)
        self.assertTrue(hp2 + 1 == shop[2].item.hp)

    def test_start_turn(self):
        shop = Shop("base", 6)

        self.assertTrue(len(shop.roster) == 7)
        shop.toggle_freeze(0)
        shop.toggle_freeze(2)
        shop.toggle_freeze(5)

        anim1 = shop[0].item
        anim2 = shop[2].item
        item = shop[5].item
        shop.start_turn()

        self.assertTrue(shop[0].item == anim1)
        self.assertTrue(shop[1].item == anim2)

        self.assertTrue(shop[5].item == item)

    def test_perm_buff(self):
        shop = Shop("base", 1)

        atk1 = shop[0].item.atk
        atk2 = shop[2].item.atk

        hp1 = shop[0].item.hp
        hp2 = shop[2].item.hp

        shop.perm_buff(2, 1)

        self.assertTrue(shop[0].item.atk == atk1 + 2)
        self.assertTrue(shop[2].item.atk == atk2 + 2)

        self.assertTrue(shop[0].item.hp == hp1 + 1)
        self.assertTrue(shop[2].item.hp == hp2 + 1)

        shop.reroll()

        atk1 = shop[0].item.atk
        atk2 = shop[2].item.atk

        hp1 = shop[0].item.hp
        hp2 = shop[2].item.hp

        shop.perm_buff(2, 1)

        self.assertTrue(shop[0].item.atk == atk1 + 2)
        self.assertTrue(shop[2].item.atk == atk2 + 2)

        self.assertTrue(shop[0].item.hp == hp1 + 1)
        self.assertTrue(shop[2].item.hp == hp2 + 1)

    def test_summon_level_unit(self):
        shop = Shop("base", 1)
        shop.summon_level_unit()

        self.assertTrue(shop[3].item.tier == 2)

        shop.start_turn()
        self.assertTrue(shop.size == 4)

        shop.clear()
        self.assertTrue(shop.size == 0)

        shop = Shop("base", 15)
        result = shop.summon_level_unit()

        self.assertFalse(result)

    def test_clear_unfrozen(self):
        shop = Shop("base", 1)

        anim1 = shop[0].item
        anim2 = shop[2].item
        item = shop[5].item

        shop[0].toggle_freeze()
        shop[2].toggle_freeze()
        shop[5].toggle_freeze()

        shop.clear_unfrozen()

        self.assertTrue(anim1 == shop[0].item)
        self.assertTrue(anim2 == shop[1].item)
        self.assertTrue(item == shop[5].item)

        self.assertIsInstance(shop[2].item, Empty)
        self.assertIsInstance(shop[6].item, Unarmed)

    def test_clear(self):
        shop = Shop("base", 15)

        shop.clear()
        for i in range(0, 5):
            self.assertIsInstance(shop[i].item, Empty)

        for i in range(5, 7):
            self.assertIsInstance(shop[i].item, Unarmed)

    def test_fill_shop(self):
        shop = Shop("base", 1)
        shop.clear()

        shop.fill_shop()
        for i in range(0, 3):
            self.assertFalse(isinstance(shop[i].item, Empty))
        for i in range(3, 5):
            self.assertIsInstance(shop[i].item, Empty)

        self.assertFalse(isinstance(shop[5].item, Unarmed))
        self.assertIsInstance(shop[6].item, Unarmed)

    def test_grow_shop(self):
        turns = [
            [3, 1, 1],
            [3, 2, 2],
            [4, 2, 3],
            [4, 2, 4],
            [5, 2, 5],
            [5, 2, 6],
            [5, 2, 6],
            [5, 2, 6]
        ]
        shop = Shop("base", 0)
        for turn_info in turns:
            shop.start_turn()
            for i in range(0, turn_info[0]):
                self.assertTrue(shop.roster[i].is_enabled)
            for i in range(turn_info[0], 5):
                self.assertFalse(shop.roster[i].is_enabled)
            for i in range(5, turn_info[1] + 5):
                self.assertTrue(shop.roster[i].is_enabled)
            for i in range(turn_info[1] + 5, 7):
                self.assertFalse(shop.roster[i].is_enabled)
            self.assertTrue(shop.tier == turn_info[2])

            shop.start_turn()
            for i in range(0, turn_info[0]):
                self.assertTrue(shop.roster[i].is_enabled)
            for i in range(turn_info[0], 5):
                self.assertFalse(shop.roster[i].is_enabled)
            for i in range(5, 5 + turn_info[1]):
                self.assertTrue(shop.roster[i].is_enabled)
            for i in range(5 + turn_info[1], 7):
                self.assertFalse(shop.roster[i].is_enabled)
            self.assertTrue(shop.tier == turn_info[2])

    def test_reroll(self):
        shop = Shop("base", 5)

        reroll_valid = False

        # multiple tests avoid bad luck
        for _ in range(10):
            animals = []
            shop.reroll()

            # get all animals
            for slot in shop.roster:
                if isinstance(slot.item, Animal) and not isinstance(slot.item, Empty):
                    animals.append(slot.item)

            shop.reroll()
            rolled_animals = []

            # get all animals
            for slot in shop.roster:
                if isinstance(slot.item, Animal) and not isinstance(slot.item, Empty):
                    rolled_animals.append(slot.item)

            # there should definitely be one different!
            for i, _ in enumerate(animals):
                if animals[i] != rolled_animals[i]:
                    reroll_valid = True

            # next check freezing prevents rerolls
            for slot in shop.roster:
                slot.toggle_freeze()

            shop.reroll()

            # assert they are still the same units
            for i, _ in enumerate(rolled_animals):
                self.assertTrue(rolled_animals[i] == shop[i].item)

            # unfreeze
            for slot in shop.roster:
                slot.toggle_freeze()

        # this should almost certainly be true!!
        self.assertTrue(reroll_valid)

    def test_toggle_freeze(self):
        shop = Shop("base", 1)

        shop.toggle_freeze(0)
        self.assertTrue(shop[0].is_frozen)

        shop.toggle_freeze(0)
        self.assertFalse(shop[0].is_frozen)
        self.assertFalse(shop[1].is_frozen)

        shop.toggle_freeze(0)
        shop.toggle_freeze(1)
        self.assertTrue(shop[0].is_frozen)
        self.assertTrue(shop[1].is_frozen)
        self.assertFalse(shop[2].is_frozen)

        shop.toggle_freeze(0)
        self.assertFalse(shop[0].is_frozen)
        self.assertTrue(shop[1].is_frozen)

        shop.toggle_freeze(1)
        self.assertFalse(shop[0].is_frozen)
        self.assertFalse(shop[1].is_frozen)
        self.assertFalse(shop[2].is_frozen)

        shop.toggle_freeze(4)
        self.assertFalse(shop[4].is_frozen)
