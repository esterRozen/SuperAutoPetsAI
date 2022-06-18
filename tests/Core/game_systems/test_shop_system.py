from unittest import TestCase

from src.core.game_elements.abstract_elements import Empty
from src.core.game_elements.game_objects.animals import Swan
from src.core.game_systems import BattleSystem, ShopSystem
from src.core.overseer import MessageAgent


class TestShopSystem(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        self.agent.debug_mode_no_handle_queue = False
        self.battle_sys = BattleSystem(self.agent)
        self.shop_sys = ShopSystem(self.agent)

    def test_start_turn(self):
        self.agent.gold = 4
        self.agent.team[0] = Swan()
        self.agent.team[0].temp_buff(1, 1)
        self.agent.store_backup()
        self.shop_sys.start_turn()

        self.assertTrue(self.agent.gold == 11)
        self.assertTrue(self.agent.team[0].battle_atk == 1)
        self.assertTrue(self.agent.team[0].atk == 1)
        self.assertTrue(self.agent.team[0].battle_hp == 3)
        self.assertTrue(self.agent.team[0].hp == 3)

    def test_toggle_freeze(self):
        result = self.shop_sys.toggle_freeze(0)
        self.assertTrue(result == 0)
        result = self.shop_sys.toggle_freeze(3)
        self.assertTrue(result == -1)
        result = self.shop_sys.toggle_freeze(5)
        self.assertTrue(result == 0)
        result = self.shop_sys.toggle_freeze(6)
        self.assertTrue(result == -1)

        shop = self.agent.shop
        self.assertTrue(shop[0].is_frozen)
        self.assertTrue(not shop[3].is_frozen)
        self.assertTrue(shop[5].is_frozen)
        self.assertTrue(not shop[6].is_frozen)

    def test_reroll(self):
        item1 = self.agent.shop[0].item
        item2 = self.agent.shop[1].item
        self.shop_sys.reroll()
        # equality checks if it's the same object instance.
        self.assertTrue(self.agent.shop[0].item != item1)
        self.assertTrue(self.agent.shop[1].item != item2)

        self.assertTrue(self.agent.gold == 9)

    def test_reroll_poor(self):
        item1 = self.agent.shop[0].item
        item2 = self.agent.shop[1].item
        self.agent.gold = 0
        self.shop_sys.reroll()

        self.assertTrue(self.agent.shop[0].item == item1)
        self.assertTrue(self.agent.shop[1].item == item2)

    def test_buy_empty_slot(self):
        # TODO
        self.fail()

    def test_buy_poor(self):
        # TODO
        self.fail()

    def test_buy_to_empty(self):
        item = self.agent.shop[0].item
        result = self.shop_sys.buy(0, 0)
        self.assertTrue(result == 0)
        self.assertTrue(self.agent.team[0] == item)
        self.assertTrue(self.agent.gold == 7)
        self.assertTrue(isinstance(self.agent.shop[0].item, Empty))

    def test_buy_to_empty_poor(self):
        item = self.agent.shop[0].item
        self.agent.gold = 2
        result = self.shop_sys.buy(0, 0)
        self.assertTrue(result == -1)
        self.assertTrue(isinstance(self.agent.team[0], Empty))
        self.assertTrue(self.agent.gold == 2)
        self.assertTrue(self.agent.shop[0].item == item)

    def test__buy_to_same(self):
        item = self.agent.shop[0].item
        copy = item.__class__()
        self.agent.team[0] = copy
        self.shop_sys.buy(0, 0)
        self.assertTrue(isinstance(self.agent.team[0], item.__class__))
        self.assertTrue(self.agent.gold == 7)

        unit = self.agent.team[0]
        self.assertTrue(unit.xp == 1)
        self.assertTrue(unit.hp == unit.__class__().hp + 1)
        self.assertTrue(unit.atk == unit.__class__().atk + 1)
        self.assertTrue(unit.level == 1)

    def test__buy_to_same_level_up(self):
        # TODO
        self.fail()

    def test__buy_food(self):
        # TODO
        self.fail()

    def test__buy_food_empty(self):
        # TODO
        self.fail()

    def test__buy_food_poor(self):
        # TODO
        self.fail()

    def test__buy_targeted_food(self):
        # TODO
        self.fail()

    def test__buy_non_targeted_food(self):
        # TODO
        self.fail()

    def test__buy_different_animal(self):
        # TODO
        self.fail()

    def test__buy_different_animal_full_team(self):
        # TODO
        self.fail()

    def test_sell(self):
        # TODO
        self.fail()

    def test_sell_bad_position(self):
        # TODO
        self.fail()

    def test_move(self):
        # TODO
        self.fail()

    def test_move_left(self):
        # TODO
        self.fail()

    def test_move_right(self):
        # TODO
        self.fail()

    def test_move_invalid(self):
        # TODO
        self.fail()

    def test_combine(self):
        # TODO
        self.fail()

    def test_combine_empty(self):
        # TODO
        self.fail()

    def test_combine_different_animals(self):
        # TODO
        self.fail()

    def test_combine_same_position(self):
        # TODO
        self.fail()

    def test_end_turn(self):
        # TODO
        self.fail()
