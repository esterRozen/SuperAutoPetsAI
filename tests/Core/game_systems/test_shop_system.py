from unittest import TestCase

from src.core.game_elements.abstract_elements import Empty, Unarmed
from src.core.game_elements.game_objects.animals import tier_1, tier_2, tier_4
from src.core.game_systems import BattleSystem, ShopSystem
from src.core.overseer import MessageAgent


class TestShopSystem(TestCase):
    def unit_stats(self, pos, atk, battle_atk, hp, battle_hp):
        self.assertTrue(self.agent.team[pos].atk == atk)
        self.assertTrue(self.agent.team[pos].battle_atk == battle_atk)
        self.assertTrue(self.agent.team[pos].hp == hp)
        self.assertTrue(self.agent.team[pos].battle_hp == battle_hp)

    def write_shop_from_team(self, team_pos, shop_pos):
        self.agent.shop[shop_pos].item = self.agent.team[team_pos].__class__()

    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        self.agent.debug_mode_no_handle_queue = False
        self.battle_sys = BattleSystem(self.agent)
        self.shop_sys = ShopSystem(self.agent)

    def test_start_turn(self):
        self.agent.gold = 4
        self.agent.team[0] = tier_2.Swan()
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
        result = self.shop_sys.reroll()
        self.assertTrue(result == 0)

        # equality checks if it's the same object instance.
        self.assertTrue(self.agent.shop[0].item != item1)
        self.assertTrue(self.agent.shop[1].item != item2)

        self.assertTrue(self.agent.gold == 9)

    def test_reroll_poor(self):
        item1 = self.agent.shop[0].item
        item2 = self.agent.shop[1].item
        self.agent.gold = 0
        result = self.shop_sys.reroll()
        self.assertTrue(result == -1)

        self.assertTrue(self.agent.shop[0].item == item1)
        self.assertTrue(self.agent.shop[1].item == item2)

    def test_buy_empty_slot(self):
        self.agent.shop[0].item = Empty()
        result = self.shop_sys.buy(0, 0)
        self.assertTrue(result == -1)
        self.assertTrue(isinstance(self.agent.shop[0].item, Empty))
        self.assertTrue(isinstance(self.agent.team[0], Empty))

    def test_buy_unarmed_slot(self):
        self.agent.team[0] = tier_1.Ant()
        self.agent.shop[5].item = Unarmed()
        result = self.shop_sys.buy(5, 0)
        self.assertTrue(result == -1)
        self.assertTrue(isinstance(self.agent.shop[5].item, Unarmed))
        self.assertTrue(isinstance(self.agent.team[0].held, Unarmed))

    def test_buy_poor(self):
        self.agent.gold = 2
        self.shop_sys.buy(0, 0)
        self.assertTrue(isinstance(self.agent.team[0], Empty))
        self.assertTrue(not isinstance(self.agent.shop[0].item, Empty))

    def test_buy_triggers_friend_summoned(self):
        # only for buy to empty and buy to different
        self.agent.team[0] = tier_1.Horse()
        self.shop_sys.buy(0, 1)
        battle_atk = self.agent.team[1].__class__().battle_atk
        self.assertTrue(self.agent.team[1].battle_atk == battle_atk + 1)

        self.setUp()
        self.agent.team[0] = tier_1.Horse()
        self.agent.team[1] = tier_1.Ant()
        self.agent.shop[0].item = tier_1.Ant()
        self.shop_sys.buy(0, 1)
        self.assertTrue(self.agent.team[1].atk == 3)
        self.assertTrue(self.agent.team[1].battle_atk == 3)

    def test_buy_triggers_friend_bought(self):
        # for all buy animal responses
        self.agent.team[0] = tier_4.Buffalo()
        self.shop_sys.buy(0, 1)
        self.unit_stats(0, 5, 5, 5, 5)
        self.write_shop_from_team(1, 0)
        self.shop_sys.buy(0, 1)
        self.unit_stats(0, 6, 6, 6, 6)
        self.shop_sys.buy(1, 1)
        self.unit_stats(0, 7, 7, 7, 7)

    def test_buy_triggers_buy(self):
        # for all buy responses that are successful
        self.agent.team[0] = tier_1.Fish()
        self.agent.shop[0].item = tier_1.Otter()
        self.agent.shop[1].item = tier_1.Otter()
        self.shop_sys.buy(0, 1)
        self.unit_stats(0, 3, 3, 3, 3)
        self.shop_sys.buy(1, 1)
        self.unit_stats(0, 4, 4, 4, 4)

        self.agent.shop[0].item = tier_1.Otter()
        self.agent.team[1] = tier_1.Ant()
        self.shop_sys.buy(0, 1)
        self.unit_stats(0, 5, 5, 5, 5)

    def test_buy_triggers_buy_t1_pet(self):
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
        item = self.agent.shop[0].item
        copy = item.__class__()
        copy.xp = 1
        self.agent.team[0] = copy
        self.shop_sys.buy(0, 0)
        self.assertTrue(isinstance(self.agent.team[0], item.__class__))
        self.assertTrue(self.agent.gold == 7)

        unit = self.agent.team[0]
        self.assertTrue(unit.xp == 2)
        self.assertTrue(unit.level == 2)
        self.assertTrue(unit.hp == unit.__class__().hp + 1)
        self.assertTrue(unit.atk == unit.__class__().atk + 1)

    def test__buy_food(self):
        self.agent.team[0] = tier_1.Ant()
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
