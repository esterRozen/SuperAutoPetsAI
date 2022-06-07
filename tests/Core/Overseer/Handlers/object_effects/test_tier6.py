from unittest import TestCase

from src.core.game_elements.game_objects.animals import tier_6
from src.core.overseer.handlers.object_effects.tier6 import Tier6
from src.core.game_systems import ShopSystem, BattleSystem
from src.core.overseer import MessageAgent


class TestTier6(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        BattleSystem(self.agent)
        ShopSystem(self.agent)

    def test__cat(self):
        # TODO
        self.fail()

    def test__dragon(self):
        # TODO
        self.fail()

    def test__fly(self):
        # TODO
        self.fail()

    def test__gorilla(self):
        # TODO
        self.fail()

    def test__leopard(self):
        # TODO
        self.fail()

    def test__mammoth(self):
        # TODO
        self.fail()

    def test__octopus(self):
        # TODO
        self.fail()

    def test__sauropod(self):
        # TODO
        self.fail()

    def test__snake(self):
        # TODO
        self.fail()

    def test__tiger(self):
        # TODO
        self.fail()

    def test__tyrannosaurus(self):
        # TODO
        self.fail()
