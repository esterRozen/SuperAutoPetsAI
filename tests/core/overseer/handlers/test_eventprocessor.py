from unittest import TestCase

from src.core.game_elements.abstract_elements import Animal, Empty
from src.core.game_elements.game_objects.equipment import Milk, Melon
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

    def check_shop_slot(self, num, atk, hp):
        slot = self.agent.shop[num]
        original = slot.item.__class__()
        self.assertTrue(slot.item.atk == original.atk + atk)
        self.assertTrue(slot.item.battle_atk == original.battle_atk + atk)
        self.assertTrue(slot.item.hp == original.hp + hp)
        self.assertTrue(slot.item.battle_hp == original.battle_hp + hp)

    def unit_stats(self, pos, atk, battle_atk, hp, battle_hp):
        self.assertTrue(self.agent.team[pos].atk == atk)
        self.assertTrue(self.agent.team[pos].battle_atk == battle_atk)
        self.assertTrue(self.agent.team[pos].hp == hp)
        self.assertTrue(self.agent.team[pos].battle_hp == battle_hp)

    def test_buy(self):
        # otter, snail, cow
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
        # ladybug, sauropod
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
        # chicken, dragon
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
        # beetle, tabby cat. rabbit, worm, seal
        self.agent.summon(tier_5.Seal(), ("team", 0))
        self.agent.summon(tier_3.Rabbit(), ("team", 1))
        self.agent.summon(tier_2.Tabby_Cat(), ("team", 2))

        self.ep.eat_food(self.agent, ("team", 0))
        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].battle_atk == 3)
        self.assertTrue(self.agent.team[0].hp == 8)
        self.assertTrue(self.agent.team[0].battle_hp == 8)

        self.assertTrue(self.agent.team[1].atk == 2)
        self.assertTrue(self.agent.team[1].battle_atk == 2)
        self.assertTrue(self.agent.team[1].hp == 3)
        self.assertTrue(self.agent.team[1].battle_hp == 3)

        self.assertTrue(self.agent.team[2].atk == 6)
        self.assertTrue(self.agent.team[2].battle_atk == 6)
        self.assertTrue(self.agent.team[2].hp == 4)
        self.assertTrue(self.agent.team[2].battle_hp == 4)

        self.agent.summon(tier_1.Beetle(), ("team", 3))
        self.agent.summon(tier_4.Worm(), ("team", 4))

        self.ep.eat_food(self.agent, ("team", 1))
        self.assertTrue(self.agent.team[1].atk == 2)
        self.assertTrue(self.agent.team[1].battle_atk == 2)
        self.assertTrue(self.agent.team[1].hp == 4)
        self.assertTrue(self.agent.team[1].battle_hp == 4)

        self.ep.eat_food(self.agent, ("team", 2))
        self.assertTrue(self.agent.team[0].atk == 3)
        self.assertTrue(self.agent.team[0].battle_atk == 4)
        self.assertTrue(self.agent.team[0].hp == 8)
        self.assertTrue(self.agent.team[0].battle_hp == 8)

        self.assertTrue(self.agent.team[1].atk == 2)
        self.assertTrue(self.agent.team[1].battle_atk == 3)
        self.assertTrue(self.agent.team[1].hp == 4)
        self.assertTrue(self.agent.team[1].battle_hp == 4)

        self.assertTrue(self.agent.team[2].atk == 6)
        self.assertTrue(self.agent.team[2].battle_atk == 6)
        self.assertTrue(self.agent.team[2].hp == 4)
        self.assertTrue(self.agent.team[2].battle_hp == 4)

        self.assertTrue(self.agent.team[3].atk == 2)
        self.assertTrue(self.agent.team[3].battle_atk == 3)
        self.assertTrue(self.agent.team[3].hp == 3)
        self.assertTrue(self.agent.team[3].battle_hp == 3)

        self.assertTrue(self.agent.team[4].atk == 3)
        self.assertTrue(self.agent.team[4].battle_atk == 4)
        self.assertTrue(self.agent.team[4].hp == 3)
        self.assertTrue(self.agent.team[4].battle_hp == 3)

        self.ep.eat_food(self.agent, ("team", 3))
        animal = self.agent.shop[0].item
        original = animal.__class__()
        self.assertTrue(animal.hp == original.hp + 1)
        self.assertTrue(animal.battle_hp == original.battle_hp + 1)
        self.assertTrue(animal.atk == original.atk)
        self.assertTrue(animal.battle_atk == original.battle_atk)

        self.ep.eat_food(self.agent, ("team", 4))
        self.assertTrue(self.agent.team[4].atk == 4)
        self.assertTrue(self.agent.team[4].battle_atk == 5)
        self.assertTrue(self.agent.team[4].hp == 4)
        self.assertTrue(self.agent.team[4].battle_hp == 4)

    def test_end_turn(self):
        # bison, parrot, penguin, monkey, bluebird,
        self.agent.summon(tier_4.Bison(), ("team", 0))
        self.agent.summon(tier_4.Parrot(), ("team", 1))
        self.agent.summon(tier_4.Penguin(), ("team", 2))
        self.agent.summon(tier_5.Monkey(), ("team", 3))
        self.agent.summon(tier_1.Bluebird(), ("team", 4))
        self.agent.team[1].xp = 5

        self.ep.end_turn(self.agent)

        # ability order: parrot, bison, bluebird, monkey, penguin
        self.assertTrue(self.agent.team[1].stored == self.agent.team[0].trigger)
        self.unit_stats(0, 8, 8, 9, 9)  # bison
        self.unit_stats(1, 5, 5, 3, 3)  # parrot
        self.unit_stats(2, 1, 1, 2, 2)  # penguin
        self.unit_stats(3, 1, 1, 2, 2)  # monkey
        self.unit_stats(4, 3, 3, 1, 1)  # bluebird

        # puppy, hatching chick, tropical fish, llama, poodle,
        self.agent.team = self.agent.team.__class__()
        self.agent.summon(tier_3.Puppy(), ("team", 0))
        self.agent.summon(tier_3.Hatching_Chick(), ("team", 1))
        self.agent.summon(tier_3.Tropical_Fish(), ("team", 2))
        self.agent.summon(tier_4.Llama(), ("team", 3))
        self.agent.summon(tier_5.Poodle(), ("team", 4))

        self.ep.end_turn(self.agent)
        self.unit_stats(0, 3, 8, 3, 8)
        self.unit_stats(1, 1, 1, 2, 2)
        self.unit_stats(2, 3, 3, 5, 5)
        self.unit_stats(3, 4, 4, 8, 8)
        self.unit_stats(4, 3, 3, 3, 3)

        # tyrannosaurus
        self.agent.team = self.agent.team.__class__()
        self.agent.summon(tier_6.Tyrannosaurus(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("team", 1))
        self.agent.summon(tier_1.Bee(), ("team", 3))

        self.ep.end_turn(self.agent)
        self.unit_stats(0, 9, 9, 4, 4)
        self.unit_stats(1, 3, 3, 2, 2)
        self.unit_stats(3, 3, 3, 2, 2)

    def test_friend_bought(self):
        # goat, buffalo,
        self.agent.summon(tier_4.Buffalo(), ("team", 0))
        self.agent.summon(tier_5.Goat(), ("team", 1))
        self.agent.summon(tier_1.Bee(), ("team", 2))

        self.ep.friend_bought(self.agent, ("team", 2))

        self.unit_stats(0, 5, 5, 5, 5)
        self.assertTrue(self.agent.gold == 11)

    def test_friend_eats_food(self):
        # rabbit
        self.agent.summon(tier_3.Rabbit(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("team", 2))

        self.ep.friend_eats_food(self.agent, ("team", 2))

        self.unit_stats(2, 1, 1, 2, 2)

    def test_friend_sold(self):
        # shrimp
        self.agent.summon(tier_2.Shrimp(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("team", 1))

        self.ep.friend_sold(self.agent, ("team", 3))
        self.unit_stats(1, 1, 1, 2, 2)

    def test_friend_summoned_shop(self):
        # dog, lobster, horse, turkey
        self.agent.summon(tier_1.Horse(), ("team", 0))
        self.agent.summon(tier_3.Dog(), ("team", 1))
        self.agent.summon(tier_4.Lobster(), ("team", 2))
        self.agent.summon(tier_5.Turkey(), ("team", 3))
        self.agent.summon(tier_1.Bee(), ("team", 4))

        self.ep.friend_summoned_shop(self.agent, ("team", 4))
        self.unit_stats(0, 2, 2, 1, 1)
        self.assertTrue(self.agent.team[1].atk == 4 or self.agent.team[1].hp == 4)
        self.unit_stats(2, 4, 4, 5, 5)
        self.unit_stats(3, 3, 3, 4, 4)
        self.unit_stats(4, 5, 6, 7, 7)

    def test_sell(self):
        # beaver, duck, pig, oql
        self.agent.summon(tier_3.Owl(), ("team", 0))
        self.agent.summon(tier_1.Duck(), ("team", 1))

        self.ep.sell(self.agent, ("team", 0))
        self.unit_stats(1, 4, 4, 5, 5)

        self.ep.sell(self.agent, ("team", 1))
        self.check_shop_buffs(0, 1)

        self.agent.summon(tier_1.Beaver(), ("team", 2))
        self.ep.sell(self.agent, ("team", 2))
        self.unit_stats(0, 5, 5, 4, 4)
        self.unit_stats(1, 4, 4, 6, 6)

        self.agent.summon(tier_1.Pig(), ("team", 2))
        self.ep.sell(self.agent, ("team", 2))
        self.assertTrue(self.agent.gold == 11)

    def test_start_turn(self):
        # dromedary, swan, caterpillar, squirrel,
        self.agent.summon(tier_2.Dromedary(), ("team", 0))
        self.agent.summon(tier_2.Swan(), ("team", 1))
        self.agent.summon(tier_4.Caterpillar(), ("team", 2))
        self.agent.summon(tier_4.Squirrel(), ("team", 3))

        self.ep.start_turn(self.agent)
        self.check_shop_slot(0, 1, 1)
        self.check_shop_slot(1, 1, 1)
        self.check_shop_slot(2, 0, 0)

        self.assertTrue(self.agent.gold == 11)
        self.assertTrue(self.agent.team[2].xp == 1)
        self.assertTrue(self.agent.shop[5].item.cost == 2)

    def test_friend_ahead_faints(self):
        # ox
        self.agent.summon(tier_3.Ox(), ("team", 1))
        self.ep.friend_ahead_faints(self.agent, ("team", 0), tier_1.Bee())

        self.assertTrue(isinstance(self.agent.team[1].held, Melon))
        self.assertTrue(self.agent.team[1].atk == 2)

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
