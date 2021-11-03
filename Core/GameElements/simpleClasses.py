# noinspection PyUnusedLocal,PyMethodMayBeStatic
class Animal:
    xp = 0
    battle_hp = 0
    battle_atk = 0
    cost = 3

    def __init__(self, atk, hp):
        self.hp = hp
        self.atk = atk

        self.battle_hp = hp
        self.battle_atk = atk

    @property
    def level(self):
        return min(self.xp // 3 + 1, 3)

    def reset_stats(self):
        self.battle_hp = self.hp
        self.battle_atk = self.atk

    def trigger(self, name):
        return 0


# noinspection PyUnusedLocal,PyMethodMayBeStatic
class Equipment:
    cost = 3

    def trigger(self, name):
        return 0


class Roster:
    def __init__(self, size):
        self.contents = [None] * size
        self.max_size = size

    def remove(self, position):
        item = self.contents[position]
        self.contents[position] = None
        return item

    def clear(self):
        self.contents = [None] * self.max_size

    def grow(self):
        self.max_size += 1

    def add(self, item):
        """

        :param item: item to insert
        :return: position inserted to, 0 on failure
        """
        i = 0
        while i < self.max_size:
            if self.contents[i] is None:
                self.contents[i] = item
                return i
        return -1

    def add_at_pos(self, item, position):
        """
        inserts to the position, default move right unless there's no space
        :param item:
        :param position:
        :return: -1 on failure
        """
        if self.contents.count(None) == 0:
            return -1

        if self.contents[position] is None:
            pass
        # if you need to, shift stuff to the right.
        elif self.contents[position:].count(None) != 0:
            value = self.contents[position]
            self._shift_right_recurse(position, value)
        elif self.contents[:position].count(None) != 0:
            value = self.contents[position]
            self._shift_left_recurse(position, value)

        self.contents[position] = item
        return 1

    def _shift_left_recurse(self, position, value):
        if self.contents[position - 1] is not None:
            nextValue = self.contents[position - 1]
            self._shift_left_recurse(position - 1, nextValue)
        self.contents[position - 1] = value

    def _shift_right_recurse(self, position, value):
        """
        assumes that at some point there is an empty space in
        self.contents
        :param position:
        :param value:
        :return:
        """
        if self.contents[position + 1] is not None:
            nextValue = self.contents[position + 1]
            self._shift_right_recurse(position + 1, nextValue)
        self.contents[position + 1] = value
