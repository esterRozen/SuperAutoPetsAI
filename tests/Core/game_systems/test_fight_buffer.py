from unittest import TestCase

from src.core.game_elements.abstract_elements import Team, Empty
from src.core.game_elements.game_objects.animals import tier_1
from src.core.game_systems.fightbuffer import FightBuffer


# noinspection PyMissingTypeHints
class TestFightBuffer(TestCase):
    def setUp(self) -> None:
        self.fightbuffer = FightBuffer()
        return

    def test_is_singleton(self):
        fightbuffer_2 = FightBuffer(limit=1000)
        self.assertTrue(fightbuffer_2 == self.fightbuffer)
        self.assertTrue(fightbuffer_2._limit == 500)

        self.fightbuffer.__class__.clear()
        del fightbuffer_2
        del self.fightbuffer

        self.fightbuffer = FightBuffer(limit=1000)
        self.assertTrue(self.fightbuffer._limit == 1000)

    def test_pop_empty(self):
        for i in range(1, 21):
            team = self.fightbuffer.pop(i)
            self.assertTrue(isinstance(team[0], tier_1.Ant))
            self.assertTrue(isinstance(team[1], tier_1.Ant))
            self.assertTrue(isinstance(team[2], tier_1.Ant))

        team = Team()
        team[0] = tier_1.Bee()
        self.fightbuffer.push(team, 1)

        team = self.fightbuffer.pop(1)
        self.assertTrue(isinstance(team[0], tier_1.Bee))
        self.assertTrue(isinstance(team[1], Empty))
        self.assertTrue(isinstance(team[2], Empty))

        team = self.fightbuffer.pop(1)
        self.assertTrue(isinstance(team[0], tier_1.Bee))
        self.assertTrue(isinstance(team[1], Empty))
        self.assertTrue(isinstance(team[2], Empty))

        for i in range(2, 21):
            team = self.fightbuffer.pop(i)
            self.assertTrue(isinstance(team[0], tier_1.Ant))
            self.assertTrue(isinstance(team[1], tier_1.Ant))
            self.assertTrue(isinstance(team[2], tier_1.Ant))

    def test_push(self):
        team = Team()
        team[0] = tier_1.Bee()
        self.fightbuffer.push(team, 1)

        team = Team()
        team[0] = tier_1.Ant()
        self.fightbuffer.push(team, 2)

        team = self.fightbuffer.pop(1)
        self.assertTrue(isinstance(team[0], tier_1.Bee))

        team = self.fightbuffer.pop(2)
        self.assertTrue(isinstance(team[0], tier_1.Ant))

    def test_cache(self):
        team = Team()
        team[0] = tier_1.Bee()
        self.fightbuffer.push(team, 1)

        self.fightbuffer.dump_to_cache()
        self.fightbuffer.load_cache()

        team = self.fightbuffer.pop(1)
        self.assertTrue(isinstance(team[0], tier_1.Bee))
        self.assertTrue(isinstance(team[1], Empty))
        self.assertTrue(isinstance(team[2], Empty))
        self.assertTrue(isinstance(team[3], Empty))
        self.assertTrue(isinstance(team[4], Empty))
