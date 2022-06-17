from unittest import TestCase

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

    def test_buy(self):
        # TODO
        self.fail()

    def test_sell(self):
        # TODO
        self.fail()

    def test_move(self):
        # TODO
        self.fail()

    def test_combine(self):
        # TODO
        self.fail()

    def test_end_turn(self):
        # TODO
        self.fail()
