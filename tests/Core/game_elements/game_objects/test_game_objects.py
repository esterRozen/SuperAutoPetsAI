from unittest import TestCase
from src.core.game_elements.game_objects.game_objects import \
    (GameObjects, base, base_items, paid_1, paid_1_items)


class TestBase(TestCase):
    def test_base_pack(self):
        base_pack = GameObjects().packs["base pack"]
        self.assertTrue(len(base_pack) == 7, "Should be 6 tiers in list + 1 tier for unrollables")
        animals = [[animal.__class__.__name__ for animal in tier] for tier in base_pack]
        for i, tier in enumerate(animals):
            for j, animal in enumerate(tier):
                self.assertTrue(animal == base[i][j],
                                f"T{i + 1}: {animal} should be {base[i][j]}")

    def test_base_items(self):
        base_pack_items = GameObjects().packs["base pack items"]
        self.assertTrue(len(base_pack_items) == 7, "Should be 6 tiers in list + 1 tier for unrollables")
        objs = [[obj.__class__.__name__ for obj in tier] for tier in base_pack_items]
        for i, tier in enumerate(objs):
            for j, obj in enumerate(tier):
                self.assertTrue(obj == base_items[i][j],
                                f"T{i + 1}: {obj} should be {base_items[i][j]}")

    def test_paid_pack_1(self):
        paid_pack_1 = GameObjects().packs["paid pack 1"]
        self.assertTrue(len(paid_pack_1) == 7, "Should be 6 tiers in list + 1 tier for unrollables")
        animals = [[animal.__class__.__name__ for animal in tier] for tier in paid_pack_1]
        for i, tier in enumerate(animals):
            for j, animal in enumerate(tier):
                self.assertTrue(animal == paid_1[i][j],
                                f"T{i + 1}: {animal} should be {paid_1[i][j]}")

    def test_paid_pack_1_items(self):
        paid_pack_1_items = GameObjects().packs["paid pack 1 items"]
        self.assertTrue(len(paid_pack_1_items) == 7, "Should be 6 tiers in list + 1 tier for unrollables")
        objs = [[obj.__class__.__name__ for obj in tier] for tier in paid_pack_1_items]
        for i, tier in enumerate(objs):
            for j, obj in enumerate(tier):
                self.assertTrue(obj == paid_1_items[i][j],
                                f"T{i + 1}: {obj} should be {paid_1_items[i][j]}")
