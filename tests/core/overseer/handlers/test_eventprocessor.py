from unittest import TestCase

from src.core.game_elements.abstract_elements import Animal, Empty
from src.core.game_elements.game_objects.equipment import Milk
from src.core.game_systems import ShopSystem, BattleSystem
from src.core.overseer.handlers import EventProcessor
from src.core.overseer.handlers.eventprocessor import \
    for_sorted_trigger, for_sorted_both_trigger, for_sorted_without_actor_trigger_, \
    for_sorted_behind_, trigger_actor_ability, get_roster

from src.core.overseer import MessageAgent
from src.core.game_elements.game_objects.animals import tier_1, tier_2, tier_3, tier_4, tier_5, tier_6


class TestEventProcessor(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        BattleSystem(self.agent)
        ShopSystem(self.agent)
        self.ep = EventProcessor()

    def check_shop_buffs(self, atk, hp):
        for slot in self.agent.shop.roster:
            if isinstance(slot.item, Animal) and not isinstance(slot.item, Empty):
                # noinspection PyArgumentList
                original = slot.item.__class__()
                self.assertTrue(slot.item.atk == original.atk + atk)
                self.assertTrue(slot.item.battle_atk == original.battle_atk + atk)
                self.assertTrue(slot.item.hp == original.hp + hp)
                self.assertTrue(slot.item.battle_hp == original.battle_hp + hp)

    def test_buy(self):
        self.agent.summon(tier_1.Otter(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("team", 1))
        self.ep.buy(self.agent, ("team", 0))

        self.assertTrue(self.agent.team[1].atk == 2)
        self.assertTrue(self.agent.team[1].battle_atk == 2)
        self.assertTrue(self.agent.team[1].hp == 2)
        self.assertTrue(self.agent.team[1].battle_hp == 2)

        self.agent.battle_lost = True
        self.agent.summon(tier_3.Snail(), ("team", 2))
        self.ep.buy(self.agent, ("team", 2))

        self.assertTrue(self.agent.team[0].atk == 2)
        self.assertTrue(self.agent.team[0].battle_atk == 2)
        self.assertTrue(self.agent.team[0].hp == 3)
        self.assertTrue(self.agent.team[0].battle_hp == 3)

        self.assertTrue(self.agent.team[1].atk == 3)
        self.assertTrue(self.agent.team[1].battle_atk == 3)
        self.assertTrue(self.agent.team[1].hp == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 3)

        self.agent.summon(tier_5.Cow(), ("team", 3))
        self.ep.buy(self.agent, ("team", 3))

        self.assertTrue(isinstance(self.agent.shop[5].item, Milk))
        self.assertTrue(isinstance(self.agent.shop[6].item, Milk))

    def test_buy_food(self):
        self.agent.summon(tier_6.Sauropod(), ("team", 0))
        self.ep.buy_food(self.agent)

        self.assertTrue(self.agent.gold == 11)

        self.agent.summon(tier_1.Ladybug(), ("team", 1))
        self.ep.buy_food(self.agent)

        self.assertTrue(self.agent.team[1].atk == 1)
        self.assertTrue(self.agent.team[1].battle_atk == 2)
        self.assertTrue(self.agent.team[1].hp == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 4)
        self.assertTrue(self.agent.gold == 12)

        self.ep.buy_food(self.agent)

        self.assertTrue(self.agent.team[1].atk == 1)
        self.assertTrue(self.agent.team[1].battle_atk == 3)
        self.assertTrue(self.agent.team[1].hp == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 5)
        self.assertTrue(self.agent.gold == 13)

        self.ep.buy_food(self.agent)

        self.assertTrue(self.agent.team[1].atk == 1)
        self.assertTrue(self.agent.team[1].battle_atk == 4)
        self.assertTrue(self.agent.team[1].hp == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 6)
        self.assertTrue(self.agent.gold == 13)

    def test_buy_t1_pet(self):
        self.agent.summon(tier_6.Dragon(), ("team", 0))
        self.agent.summon(tier_5.Chicken(), ("team", 1))
        self.agent.summon(tier_1.Bee(), ("team", 2))
        self.agent.summon(tier_1.Bee(), ("team", 4))

        self.ep.buy_t1_pet(self.agent)

        self.check_shop_buffs(1, 1)
        self.assertTrue(self.agent.team[1].atk == 2)
        self.assertTrue(self.agent.team[1].battle_atk == 2)
        self.assertTrue(self.agent.team[1].hp == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 3)

        self.assertTrue(self.agent.team[2].atk == 2)
        self.assertTrue(self.agent.team[2].battle_atk == 2)
        self.assertTrue(self.agent.team[2].hp == 2)
        self.assertTrue(self.agent.team[2].battle_hp == 2)

        self.assertTrue(self.agent.team[4].atk == 2)
        self.assertTrue(self.agent.team[4].battle_atk == 2)
        self.assertTrue(self.agent.team[4].hp == 2)
        self.assertTrue(self.agent.team[4].battle_hp == 2)

    def test_eat_food(self):
        # TODO
        self.fail()

    def test_end_turn(self):
        # TODO
        self.fail()

    def test_friend_bought(self):
        # TODO
        self.fail()

    def test_friend_eats_food(self):
        # TODO
        self.fail()

    def test_friend_sold(self):
        # TODO
        self.fail()

    def test_friend_summoned_shop(self):
        # TODO
        self.fail()

    def test_sell(self):
        # TODO
        self.fail()

    def test_start_turn(self):
        # TODO
        self.fail()

    def test_friend_ahead_faints(self):
        # TODO
        self.fail()

    def test_friend_faints(self):
        # TODO
        self.fail()

    def test_hurt(self):
        # TODO
        self.fail()

    def test_is_summoned(self):
        # TODO
        self.fail()

    def test_on_faint(self):
        # TODO
        self.fail()

    def test_on_level(self):
        # TODO
        self.fail()

    def test_damage_team(self):
        # TODO
        self.fail()

    def test_before_attack(self):
        # TODO
        self.fail()

    def test_enemy_attacks(self):
        # TODO
        self.fail()

    def test_friend_ahead_attacks(self):
        # TODO
        self.fail()

    def test_friend_summoned_battle(self):
        # TODO
        self.fail()

    def test_knock_out(self):
        # TODO
        self.fail()

    def test_start_battle(self):
        # TODO
        self.fail()

    def test_deal_enemy(self):
        # TODO
        self.fail()
