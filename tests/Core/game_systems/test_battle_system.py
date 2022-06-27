from unittest import TestCase

from src.core.game_elements.abstract_elements import Team, Empty
from src.core.game_elements.game_objects.animals import tier_1, tier_2, tier_3, tier_4, tier_5
from src.core.game_elements.game_objects.equipment import Honey, Garlic
from src.core.game_systems import BattleSystem, ShopSystem
from src.core.overseer import MessageAgent


class TestBattleSystem(TestCase):

    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        self.battle_sys = BattleSystem(self.agent)
        ShopSystem(self.agent)
        self.agent.debug_mode_no_handle_queue = False
        self.agent.in_shop = False

    def test_basic_battle(self):
        self.agent.team[0] = tier_1.Fish()
        self.agent.team[0].held = Honey()
        enemy = Team()
        enemy[0] = tier_1.Cricket()

        self.battle_sys.start_battle(enemy)
        self.assertTrue(self.agent.wins == 1)
        self.assertTrue(isinstance(self.agent.team[0], tier_1.Bee))

    def test_battle_summons(self):
        self.agent.team[0] = tier_2.Spider()
        self.agent.team[1] = tier_1.Bee()
        self.agent.team[2] = tier_2.Spider()

        enemy = Team()
        enemy[0] = tier_2.Spider()
        enemy[1] = tier_1.Bee()
        enemy[2] = tier_2.Spider()

        result = self.battle_sys.start_battle(enemy)

        if result == 1:
            self.assertTrue(self.agent.life == 10)
            self.assertTrue(self.agent.wins == 1)
            self.assertTrue(not self.agent.battle_lost)
        elif result == 0:
            self.assertTrue(self.agent.life == 10)
            self.assertTrue(self.agent.wins == 0)
            self.assertTrue(not self.agent.battle_lost)
        elif result == -1:
            self.assertTrue(self.agent.life == 9)
            self.assertTrue(self.agent.wins == 0)
            self.assertTrue(not self.agent.battle_lost)
        self.assertTrue(self.agent.turn == 1)

        self.assertTrue(isinstance(self.agent.enemy[0], Empty) or isinstance(self.agent.team[0], Empty))

    def test_complex_battle(self):
        self.agent.team[0] = tier_2.Hedgehog()
        self.agent.team[1] = tier_3.Camel()
        self.agent.team[1].held = Garlic()
        self.agent.team[2] = tier_4.Skunk()
        self.agent.team[2].held = Garlic()
        self.agent.team[3] = tier_3.Sheep()
        self.agent.team[4] = tier_3.Badger()
        self.agent.team[4].held = Honey()

        enemy = Team()
        enemy[0] = tier_5.Eagle()
        enemy[1] = tier_3.Kangaroo()
        enemy[2] = tier_2.Spider()
        enemy[3] = tier_1.Otter()
        enemy[4] = tier_4.Deer()
        self.battle_sys.start_battle(enemy)

        # TODO assertions
        self.fail()

    def test_lose_health(self):
        # TODO
        self.fail()

    def test_summon(self):
        # TODO
        self.fail()
