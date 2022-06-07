from unittest import TestCase

from src.core.game_elements.game_objects.animals import tier_1, tier_2, tier_5
from src.core.game_systems import BattleSystem, ShopSystem
from src.core.overseer import MessageAgent


class TestTier5(TestCase):
    def setUp(self) -> None:
        self.agent = MessageAgent("base pack")
        BattleSystem(self.agent)
        ShopSystem(self.agent)

    def test__chicken(self):
        # TODO
        self.fail()

    def test__cow(self):
        # TODO
        self.fail()

    def test__crocodile(self):
        # TODO
        self.fail()

    def test__eagle(self):
        # TODO
        self.fail()

    def test__goat(self):
        # TODO
        self.fail()

    def test__microbe(self):
        # TODO
        self.fail()

    def test__parrot(self):
        # TODO
        self.fail()

    def test__poodle(self):
        self.agent.summon(tier_1.Fish(), ("team", 4))
        self.agent.summon(tier_2.Shrimp(), ("team", 3))
        self.agent.summon(tier_1.Fish(), ("team", 2))
        self.agent.summon(tier_5.Poodle(), ("team", 1))
        self.agent.summon(tier_5.Cow(), ("team", 0))
        self.fail()

    def test__rhino(self):
        # TODO
        self.fail()

    def test__scorpion(self):
        # TODO
        self.fail()

    def test__seal(self):
        # TODO
        self.fail()

    def test__shark(self):
        # TODO
        self.fail()

    def test__turkey(self):
        # TODO
        self.fail()
