from unittest import TestCase

from src.core.game_elements.abstract_elements import Animal, Empty
from src.core.game_elements.game_objects.equipment import Milk, Melon, Coconut, Peanut, Weak
from src.core.game_systems import ShopSystem, BattleSystem
from src.core.overseer.handlers import EventProcessor

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

        self.ep.sell(self.agent, ("team", 3))

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
        self.ep.friend_ahead_faints(self.agent, ("team", 0))

        self.assertTrue(isinstance(self.agent.team[1].held, Melon))
        self.assertTrue(self.agent.team[1].atk == 2)

    def test_friend_faints(self):
        # shark, fly
        self.agent.summon(tier_5.Shark(), ("team", 3))
        self.agent.summon(tier_6.Fly(), ("team", 4))

        self.ep.friend_faints(self.agent, ("team", 1), fainted=tier_1.Bee())

    def test_hurt(self):
        # blowfish, peacock, gorilla
        self.agent.in_shop = False
        self.agent.summon(tier_1.Bee(), ("enemy", 0))

        self.agent.summon(tier_3.Blowfish(), ("team", 0))
        self.agent.summon(tier_2.Peacock(), ("team", 1))
        self.agent.summon(tier_6.Gorilla(), ("team", 2))

        self.ep.hurt(self.agent, ("team", 0))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.ep.hurt(self.agent, ("team", 1))
        self.unit_stats(1, 2, 6, 5, 5)

        self.ep.hurt(self.agent, ("team", 2))
        self.assertTrue(isinstance(self.agent.team[2].held, Coconut))

    def test_is_summoned(self):
        # scorpion
        self.agent.summon(tier_5.Scorpion(), ("team", 0))
        self.ep.is_summoned(self.agent, ("team", 0))

        self.assertTrue(isinstance(self.agent.team[0].held, Peanut))

    def test_on_faint(self):
        # ant, cricket, flamingo, hedgehog, rat
        self.agent.summon(tier_1.Ant(), ("team", 0))
        self.agent.summon(tier_1.Cricket(), ("team", 1))

        self.ep.on_faint(self.agent, ("team", 0), fainted=self.agent.team[0])
        self.unit_stats(1, 3, 3, 3, 3)

        cricket = self.agent.team[1]
        self.agent.team[1] = Empty()
        self.ep.on_faint(self.agent, ("team", 1), fainted=cricket)
        self.assertTrue(isinstance(self.agent.team[1], tier_1.Zombie_Cricket))

        self.agent.summon(tier_2.Flamingo(), ("team", 2))
        self.agent.summon(tier_2.Hedgehog(), ("team", 3))
        self.agent.summon(tier_2.Rat(), ("team", 4))

        self.ep.on_faint(self.agent, ("team", 2), fainted=self.agent.team[2])
        self.unit_stats(3, 4, 4, 3, 3)
        self.unit_stats(4, 5, 5, 6, 6)

        hedgehog = self.agent.team[3]
        self.agent.team[3] = Empty()
        self.ep.on_faint(self.agent, ("team", 3), fainted=hedgehog)

        self.assertTrue(isinstance(self.agent.team[1], Empty))
        self.assertTrue(isinstance(self.agent.team[2], Empty))
        self.unit_stats(4, 5, 5, 4, 4)

        self.agent.in_shop = False
        self.ep.on_faint(self.agent, ("team", 4), fainted=self.agent.team[4])

        self.assertTrue(isinstance(self.agent.enemy[0], tier_2.Dirty_Rat))

        self.agent.enemy = self.agent.enemy.__class__()
        self.agent.team = self.agent.team.__class__()
        # spider, badger, sheep, turtle, deer
        spider = tier_2.Spider()
        self.ep.on_faint(self.agent, ("team", 0), fainted=spider)
        self.assertTrue(self.agent.team[0].tier == 3)
        self.unit_stats(0, 2, 2, 2, 2)

        # badger
        self.agent.team[0] = Empty()
        badger = tier_3.Badger()
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.agent.summon(tier_1.Bee(), ("team", 1))
        self.ep.on_faint(self.agent, ("team", 0), fainted=badger)
        self.assertTrue(isinstance(self.agent.team[1], Empty))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.summon(tier_1.Bee(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("team", 2))
        self.ep.on_faint(self.agent, ("team", 1), fainted=badger)
        self.assertTrue(isinstance(self.agent.team[2], Empty))
        self.assertTrue(isinstance(self.agent.team[0], Empty))

        # sheep
        sheep = tier_3.Sheep()
        self.ep.on_faint(self.agent, ("team", 0), fainted=sheep)
        self.assertTrue(isinstance(self.agent.team[0], tier_3.Ram))
        self.assertTrue(isinstance(self.agent.team[1], tier_3.Ram))

        turtle = tier_3.Turtle()
        self.ep.on_faint(self.agent, ("team", 0), fainted=turtle)
        self.assertTrue(isinstance(self.agent.team[1].held, Melon))

        deer = tier_4.Deer()
        self.ep.on_faint(self.agent, ("team", 2), fainted=deer)
        self.assertTrue(isinstance(self.agent.team[2], tier_4.Bus))

        self.agent.team = self.agent.team.__class__()
        # microbe, rooster, whale, eagle, mammoth
        microbe = tier_4.Microbe()
        self.agent.summon(tier_1.Bee(), ("team", 1))
        self.agent.summon(tier_1.Bee(), ("team", 3))
        self.agent.summon(tier_1.Bee(), ("team", 4))
        self.agent.summon(tier_1.Bee(), ("enemy", 2))
        self.agent.summon(tier_1.Bee(), ("enemy", 4))

        self.ep.on_faint(self.agent, ("team", 0), fainted=microbe)
        self.assertTrue(isinstance(self.agent.team[1].held, Weak))
        self.assertTrue(isinstance(self.agent.team[3].held, Weak))
        self.assertTrue(isinstance(self.agent.team[4].held, Weak))
        self.assertTrue(isinstance(self.agent.enemy[2].held, Weak))
        self.assertTrue(isinstance(self.agent.enemy[4].held, Weak))

        self.agent.team = self.agent.team.__class__()
        self.agent.enemy = self.agent.enemy.__class__()

        # rooster
        rooster = tier_4.Rooster()
        self.ep.on_faint(self.agent, ("team", 0), fainted=rooster)
        self.assertTrue(isinstance(self.agent.team[0], tier_4.Chick))

        # eagle
        eagle = tier_5.Eagle()
        self.ep.on_faint(self.agent, ("team", 1), fainted=eagle)
        self.assertTrue(self.agent.team[1].tier == 6)

        self.agent.team = self.agent.team.__class__()
        # mammoth
        self.agent.summon(tier_1.Bee(), ("team", 1))
        self.agent.summon(tier_1.Bee(), ("team", 3))
        self.agent.in_shop = True
        mammoth = tier_6.Mammoth()
        self.ep.on_faint(self.agent, ("team", 0), fainted=mammoth)
        self.unit_stats(1, 3, 3, 3, 3)
        self.unit_stats(3, 3, 3, 3, 3)

    def test_on_level(self):
        # fish
        self.agent.summon(tier_1.Fish(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("team", 1))
        self.agent.summon(tier_1.Bee(), ("team", 2))
        self.agent.summon(tier_1.Bee(), ("team", 4))

        self.agent.team[0].xp = 2
        self.ep.on_level(self.agent, ("team", 0))

        self.unit_stats(1, 2, 2, 2, 2)
        self.unit_stats(2, 2, 2, 2, 2)
        self.unit_stats(4, 2, 2, 2, 2)

        self.agent.team[0].xp = 5
        self.ep.on_level(self.agent, ("team", 0))

        self.unit_stats(1, 4, 4, 4, 4)
        self.unit_stats(2, 4, 4, 4, 4)
        self.unit_stats(4, 4, 4, 4, 4)

    def test_before_attack(self):
        # elephant, boar, octopus

        self.agent.summon(tier_2.Elephant(), ("team", 0))
        self.agent.summon(tier_6.Boar(), ("team", 1))
        self.agent.summon(tier_6.Octopus(), ("team", 2))

        self.ep.before_attack(self.agent, ("team", 0))
        self.unit_stats(1, 10, 10, 5, 5)

        self.ep.before_attack(self.agent, ("team", 1))
        self.unit_stats(1, 10, 14, 5, 7)

        self.agent.in_shop = False
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.agent.summon(tier_1.Bee(), ("enemy", 1))

        self.ep.before_attack(self.agent, ("team", 2))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))
        self.assertTrue(isinstance(self.agent.enemy[1], Empty))

    def test_friend_ahead_attacks(self):
        # kangaroo, snake
        self.agent.summon(tier_3.Kangaroo(), ("team", 1))
        self.agent.summon(tier_6.Snake(), ("team", 2))

        self.ep.friend_ahead_attacks(self.agent, ("team", 0))
        self.unit_stats(1, 1, 3, 2, 4)

        self.agent.in_shop = False
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.ep.friend_ahead_attacks(self.agent, ("team", 1))
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

    def test_friend_summoned_battle(self):
        # horse, dog, turkey
        self.agent.summon(tier_1.Bee(), ("team", 0))
        self.agent.summon(tier_1.Horse(), ("team", 1))
        self.agent.summon(tier_3.Dog(), ("team", 2))
        self.agent.summon(tier_5.Turkey(), ("team", 3))

        self.ep.friend_summoned_battle(self.agent, ("team", 0))
        self.unit_stats(0, 3, 4, 4, 4)
        self.assertTrue(self.agent.team[2].atk == 4 or self.agent.team[2].hp == 4)

    def test_knock_out(self):
        # hippo, rhino
        self.agent.summon(tier_4.Hippo(), ("team", 0))
        self.agent.summon(tier_5.Rhino(), ("team", 1))

        self.ep.knock_out(self.agent, ("team", 0))
        self.unit_stats(0, 4, 7, 7, 10)

        self.agent.in_shop = False
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.ep.knock_out(self.agent, ("team", 1))

        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

    def test_start_battle(self):
        # mosquito, bat, crab, dodo, caterpillar
        self.agent.in_shop = False
        self.agent.summon(tier_1.Mosquito(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.ep.start_battle(self.agent)

        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.team = self.agent.team.__class__()
        # bat
        self.agent.summon(tier_2.Bat(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.ep.start_battle(self.agent)

        self.assertTrue(isinstance(self.agent.enemy[0].held, Weak))

        # crab
        self.agent.summon(tier_2.Crab(), ("team", 1))
        self.agent.summon(tier_2.Elephant(), ("team", 2))
        self.ep.start_battle(self.agent)

        self.unit_stats(1, 3, 3, 1, 2)
        self.agent.summon(tier_2.Dodo(), ("team", 3))
        self.ep.start_battle(self.agent)

        self.unit_stats(2, 3, 4, 5, 5)

        self.agent.summon(tier_4.Caterpillar(), ("team", 4))
        self.agent.team[4].xp = 5
        self.ep.start_battle(self.agent)

        self.assertTrue(isinstance(self.agent.team[4], tier_4.Butterfly))

        self.agent.team = self.agent.team.__class__()
        # dolphin, skunk, whale, crocodile, leopard
        self.agent.summon(tier_4.Dolphin(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.ep.start_battle(self.agent)
        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.team = self.agent.team.__class__()
        self.agent.summon(tier_4.Skunk(), ("team", 0))
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.agent.enemy[0].battle_hp = 50
        self.ep.start_battle(self.agent)

        self.agent.team[0] = self.agent.enemy[0]
        self.unit_stats(0, 1, 1, 1, 34)

        self.agent.team = self.agent.team.__class__()
        self.agent.enemy = self.agent.enemy.__class__()
        self.agent.summon(tier_5.Crocodile(), ("team", 3))
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.ep.start_battle(self.agent)

        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.team = self.agent.team.__class__()
        self.agent.summon(tier_6.Leopard(), ("team", 4))
        self.agent.summon(tier_1.Bee(), ("enemy", 0))
        self.ep.start_battle(self.agent)

        self.assertTrue(isinstance(self.agent.enemy[0], Empty))

        self.agent.team = self.agent.team.__class__()
        self.agent.enemy = self.agent.enemy.__class__()
        # whale
        self.agent.summon(tier_4.Whale(), ("team", 2))
        self.agent.summon(tier_1.Bee(), ("team", 1))
        self.ep.start_battle(self.agent)
        self.assertTrue(isinstance(self.agent.team[2].stored, tier_1.Bee))

        self.ep.on_faint(self.agent, ("team", 2), fainted=self.agent.team[2])
        self.assertTrue(isinstance(self.agent.team[2], tier_1.Bee))
