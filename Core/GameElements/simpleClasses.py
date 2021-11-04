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

    def permanent_buff(self, hp, atk):
        self.hp += hp
        self.atk += atk

        self.battle_hp += hp
        self.battle_atk += atk
        return

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
        self._contents = [None] * size
        self.max_size = size

    def item(self, position):
        return self._contents[position]

    def remove(self, position):
        item = self._contents[position]
        self._contents[position] = None
        return item

    def clear(self):
        self._contents = [None] * self.max_size

    def grow(self):
        self.max_size += 1

    def add(self, item):
        """

        :param item: item to insert
        :return: position inserted to, 0 on failure
        """
        i = 0
        while i < self.max_size:
            if self._contents[i] is None:
                self._contents[i] = item
                return i
        return -1

    def add_at_pos(self, item, position):
        """
        inserts to the position, default move right unless there's no space
        :param item:
        :param position:
        :return: -1 on failure
        """
        if self._contents.count(None) == 0:
            return -1

        if self._contents[position] is None:
            pass
        # if you need to, shift stuff to the right.
        elif self._contents[position:].count(None) != 0:
            value = self._contents[position]
            self._shift_right_recurse(position, value)
        elif self._contents[:position].count(None) != 0:
            value = self._contents[position]
            self._shift_left_recurse(position, value)

        self._contents[position] = item
        return 1

    def _shift_left_recurse(self, position, value):
        if self._contents[position - 1] is not None:
            nextValue = self._contents[position - 1]
            self._shift_left_recurse(position - 1, nextValue)
        self._contents[position - 1] = value

    def _shift_right_recurse(self, position, value):
        """
        assumes that at some point there is an empty space in
        self.contents
        :param position:
        :param value:
        :return:
        """
        if self._contents[position + 1] is not None:
            nextValue = self._contents[position + 1]
            self._shift_right_recurse(position + 1, nextValue)
        self._contents[position + 1] = value
