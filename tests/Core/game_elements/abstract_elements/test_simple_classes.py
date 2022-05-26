from unittest import TestCase

from core.eventnames import BUY
from src.core.game_elements.abstract_elements import Animal, Empty, Equipment, Unarmed


# testing generics and nulls
class TestAnimal(TestCase):
    def test_level(self):
        animal = Animal(6, 3)

        self.assertTrue(animal.level == 1, "level starts at 1")

        animal.increase_xp(1)
        self.assertTrue(animal.level == 1, "level should not increment at 1 xp")

        animal.increase_xp(2)
        self.assertTrue(animal.level == 2, "level should have incremented")

        animal.increase_xp(1)
        animal.reset_temp_stats()
        self.assertTrue(animal.level == 2, "level should remain same")

        animal.increase_xp(8)
        self.assertTrue(animal.level == 3, "level limited to 3")

    def test_trigger(self):
        animal = Animal(3, 4)
        self.assertTrue(animal.trigger(BUY) == 0, "default trigger should be 0")

    def test_equipment_modifier(self):
        # TODO
        self.fail()

    def test_permanent_buff(self):
        animal = Animal(5, 2)

        animal.permanent_buff(3, 3)
        self.assertTrue(animal.hp == 5, "HP incorrectly added")
        self.assertTrue(animal.atk == 8, "ATK incorrectly added")

        # turn end
        animal.reset_temp_stats()
        self.assertTrue(animal.id == 0, "id changed")
        self.assertTrue(animal.cost == 3, "cost changed")
        self.assertTrue(animal.xp == 0, "xp changed")
        self.assertTrue(animal.tier == 0, "tier changed")

        animal = Animal(2, 2)

        animal.permanent_buff(-2, 4)
        self.assertTrue(animal.hp == 6, "HP incorrectly added")
        self.assertTrue(animal.atk == 1, "ATK incorrectly removed")
        self.assertTrue(animal.battle_hp == 6, "Battle HP not considered")
        self.assertTrue(animal.battle_atk == 1, "Battle ATK not considered")

        animal = Animal(2, 2)

        animal.temp_buff(3, 3)
        animal.permanent_buff(-2, 4)
        self.assertTrue(animal.hp == 6, "perm HP incorrectly added")
        self.assertTrue(animal.atk == 1, "perm ATK incorrectly added")
        self.assertTrue(animal.battle_hp == 9, "battle HP incorrect")
        self.assertTrue(animal.battle_atk == 3, "battle ATK incorrect")

        animal.reset_temp_stats()
        self.assertTrue(animal.hp == 6, "perm HP wrong")
        self.assertTrue(animal.atk == 1, "perm ATK wrong")
        self.assertTrue(animal.battle_hp == 6, "battle HP wrong")
        self.assertTrue(animal.battle_atk == 1, "battle ATK wrong")

        self.assertTrue(animal.id == 0, "id changed")
        self.assertTrue(animal.cost == 3, "cost changed")
        self.assertTrue(animal.xp == 0, "xp changed")
        self.assertTrue(animal.tier == 0, "tier changed")

    def test_temp_buff(self):
        animal = Animal(2, 2)
        animal.temp_buff(-2, 4)
        self.assertTrue(animal.hp == 2, "perm HP should be untouched")
        self.assertTrue(animal.atk == 2, "perm ATK should be untouched")
        self.assertTrue(animal.battle_hp == 6, "battle HP incorrect")
        self.assertTrue(animal.battle_atk == 1, "battle ATK incorrect")
        animal.temp_buff(3, 3)
        self.assertTrue(animal.hp == 2, "perm HP should be untouched")
        self.assertTrue(animal.atk == 2, "perm ATK should be untouched")
        self.assertTrue(animal.battle_hp == 9, "battle HP incorrect")
        self.assertTrue(animal.battle_atk == 4, "battle ATK incorrect")

    def test_reset_stats(self):
        animal = Animal(5, 4)

        animal.increase_xp(4)
        animal.permanent_buff(3, 3)
        animal.reset_temp_stats()

        self.assertTrue(animal.level == 2, "incorrect level")
        self.assertTrue(animal.hp == 11, "incorrect hp")
        self.assertTrue(animal.atk == 12, "incorrect atk")
        self.assertTrue(animal.battle_hp == 11, "incorrect battle hp")
        self.assertTrue(animal.battle_atk == 12, "incorrect battle atk")

    def test_increase_xp(self):
        animal = Animal(4, 2)
        animal.increase_xp(1)
        self.assertTrue(animal.xp == 1, "xp incorrect")
        self.assertTrue(animal.hp == 3, "hp incorrect")
        self.assertTrue(animal.battle_hp == 3, "battle hp incorrect")
        self.assertTrue(animal.atk == 5, "atk incorrect")
        self.assertTrue(animal.battle_atk == 5, "battle atk incorrect")

        animal.increase_xp(2)
        self.assertTrue(animal.xp == 3, "xp incorrect")
        self.assertTrue(animal.hp == 5, "hp incorrect")
        self.assertTrue(animal.battle_hp == 5, "battle hp incorrect")
        self.assertTrue(animal.atk == 7, "atk incorrect")
        self.assertTrue(animal.battle_atk == 7, "battle atk incorrect")

        animal.increase_xp(1)
        animal.reset_temp_stats()
        self.assertTrue(animal.xp == 4, "xp changed in reset")
        self.assertTrue(animal.hp == 6, "hp changed in reset")
        self.assertTrue(animal.battle_hp == 6, "battle hp changed in reset")
        self.assertTrue(animal.atk == 8, "atk changed in reset")
        self.assertTrue(animal.battle_atk == 8, "battle atk changed in reset")

        animal.increase_xp(5)
        self.assertTrue(animal.xp == 5, "xp should be capped at 5")
        self.assertTrue(animal.level == 3, "level should only be 3")
        self.assertTrue(animal.hp == 7, "hp should be limited by xp cap")
        self.assertTrue(animal.atk == 9, "atk limited by xp cap")
        self.assertTrue(animal.battle_hp == 7, "battle hp limited by xp cap")
        self.assertTrue(animal.battle_atk == 9, "battle atk limited by xp cap")


class TestEmpty(TestCase):
    def test_level(self):
        empty = Empty()
        self.assertTrue(empty.level == 0)
        empty.increase_xp(40)
        self.assertTrue(empty.level == 0)

    def test_trigger(self):
        empty = Empty()
        self.assertTrue(empty.trigger(BUY) == 0)

    def test_equipment_modifier(self):
        # TODO
        self.fail()

    def test_permanent_buff(self):
        empty = Empty()
        empty.permanent_buff(3, 3)
        self.assertTrue(empty.hp == 0)
        self.assertTrue(empty.atk == 0)
        self.assertTrue(empty.battle_hp == 0)
        self.assertTrue(empty.battle_atk == 0)

    def test_temp_buff(self):
        empty = Empty()
        empty.temp_buff(3, 3)
        self.assertTrue(empty.hp == 0)
        self.assertTrue(empty.atk == 0)
        self.assertTrue(empty.battle_hp == 0)
        self.assertTrue(empty.battle_atk == 0)

    def test_reset_stats(self):
        empty = Empty()
        empty.temp_buff(3, 3)
        empty.reset_temp_stats()
        self.assertTrue(empty.hp == 0)
        self.assertTrue(empty.atk == 0)
        self.assertTrue(empty.battle_hp == 0)
        self.assertTrue(empty.battle_atk == 0)

    def test_increase_xp(self):
        empty = Empty()
        empty.increase_xp(2)
        self.assertTrue(empty.xp == 0)


class TestEquipment(TestCase):
    def test_instantiation(self):
        equip = Equipment()
        self.assertTrue(equip.cost == 3, "cost should be 3")
        self.assertTrue(equip.id == 0, "id should be 0")

    def test_trigger(self):
        equip = Equipment()
        self.assertTrue(equip.trigger(30) == 0, "trigger should be no-op")

    def test_query(self):
        # TODO
        self.fail()


class TestUnarmed(TestCase):
    def test_instantiation(self):
        nothing = Unarmed()
        self.assertTrue(nothing.cost == 0, "cost should be 0")
        self.assertTrue(nothing.id == 0, "id should be 0")
        self.assertTrue(nothing.trigger(30) == 0, "trigger should be no-op")

    def test_query(self):
        # TODO
        self.fail()
