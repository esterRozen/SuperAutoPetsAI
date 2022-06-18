from unittest import TestCase

from src.core.game_elements.abstract_elements import Team
from src.core.game_elements.game_objects.animals import tier_1
from src.core.game_elements.game_objects.equipment import Honey
from src.core.game_systems import BattleSystem, ShopSystem
from src.core.overseer import MessageAgent


class TestBattleSystem(TestCase):

    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        self.battle_sys = BattleSystem(self.agent)
        ShopSystem(self.agent)
        self.agent.debug_mode_no_handle_queue = False
        self.agent.in_shop = False

    def test_start_battle(self):
        self.agent.team[0] = tier_1.Fish()
        self.agent.team[0].held = Honey()
        enemy = Team()
        enemy[0] = tier_1.Cricket()

        self.battle_sys.start_battle(enemy)
        self.assertTrue(self.agent.wins == 1)
        self.assertTrue(isinstance(self.agent.team[0], tier_1.Bee))

    def test_summon(self):
        # TODO
        self.fail()
