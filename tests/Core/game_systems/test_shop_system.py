from unittest import TestCase

from src.core.game_systems import BattleSystem, ShopSystem
from src.core.overseer import MessageAgent


class TestShopSystem(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        BattleSystem(self.agent)
        ShopSystem(self.agent)

    def test_instantiation(self):
        # TODO
        self.fail()

    def test_start_turn(self):
        # TODO
        self.fail()

    def test_toggle_freeze(self):
        # TODO
        self.fail()

    def test_reroll(self):
        # TODO
        self.fail()

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
