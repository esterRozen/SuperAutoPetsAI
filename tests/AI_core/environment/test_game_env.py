from unittest import TestCase

from src.AI_core.environment import SAPGame


class TestSAPGame(TestCase):
    def setUp(self) -> None:
        self.env = SAPGame("base pack")

    def test_step(self):
        self.fail()

    def test_reset(self):
        self.fail()

    def test_render(self):
        self.fail()

    def test_sample(self):
        action_sample = self.env.action_space.sample()
        observation_sample = self.env.observation_space.sample()
        self.fail()
