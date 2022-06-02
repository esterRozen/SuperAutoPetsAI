from typing import TYPE_CHECKING, Tuple

from .. import eventnames
from ..game_elements.abstract_elements import Empty, Unarmed, Equipment, Animal

if TYPE_CHECKING:
    from ..overseer import MessageAgent


class ShopSystem:
    def __init__(self, agent: 'MessageAgent'):
        """
        Args:
            agent (MessageAgent):
        """
        self.__agent = agent
        self.__agent.set_shopper(self)

    def start_turn(self):
        # load backup team into normal team
        # reset temp stats
        self.__agent.load_backup()
        self.__agent.reset_temp_stats()

        # shop flows
        self.__agent.shop.start_turn()

        # events
        # start turn
        self.__agent.enqueue_event(eventnames.START_TURN)

    def toggle_freeze(self, pos: int):
        self.__agent.shop.toggle_freeze(pos)
        return

    def reroll(self):
        self.__agent.shop.reroll()
        return

    def buy(self, item_pos: int, target_pos: int):
        # differentiate between food/equipment and animals!
        # presume it is a valid purchase
        shop_slot = self.__agent.shop.roster[item_pos]

        if isinstance(shop_slot.item, Empty) or isinstance(shop_slot, Unarmed):
            return

        # guard clause, no gold, no purchase.
        if self.__agent.gold < shop_slot.item.cost:
            return

        if isinstance(self.__agent.team.animals[target_pos], Empty):
            self.__buy_to_empty_response(shop_slot, target_pos)
            return

        if isinstance(shop_slot.item, self.__agent.team.animals[target_pos].__class__):
            self.__buy_to_same_response(shop_slot, target_pos)
            return

        if isinstance(shop_slot.item, Equipment):
            self.__buy_equipment_response(shop_slot, target_pos)

        self.__buy_different_animal_response(shop_slot, target_pos)
        return

    def __buy_to_empty_response(self, shop_slot, target_pos: int):
        if isinstance(shop_slot.item, Equipment):
            return

        target = ("team", target_pos)
        item: Animal = shop_slot.item

        self.__agent.gold -= item.cost
        shop_slot.buy()

        self.__agent.team.animals[target_pos] = item

        self.__agent.enqueue_event(eventnames.FRIEND_SUMMONED_SHOP,
                                   actor=target)

        self.__agent.enqueue_event(eventnames.FRIEND_BOUGHT,
                                   actor=target)

        self.__agent.enqueue_event(eventnames.BUY,
                                   actor=target)
        if item.tier == 1:
            self.__agent.enqueue_event(eventnames.BUY_T1_PET)
        return

    def __buy_to_same_response(self, shop_slot, target_pos: int):
        target_unit = self.__agent.team.animals[target_pos]
        target = ("team", target_pos)

        item: Animal = shop_slot.buy()
        self.__agent.gold -= item.cost

        target_unit.increase_xp(1)

        self.__agent.enqueue_event(eventnames.FRIEND_BOUGHT,
                                   actor=target)

        self.__agent.enqueue_event(eventnames.BUY,
                                   actor=target)

        if item.tier == 1:
            self.__agent.enqueue_event(eventnames.BUY_T1_PET,
                                       actor=("team", target_pos))
        return

    def __buy_equipment_response(self, shop_slot, target_pos: int):
        item: Equipment = shop_slot.item

        actor = ("team", target_pos)
        self.__agent.gold -= item.cost
        shop_slot.buy()

        if item.is_targeted:
            # handle consumable targeted food e.g. pear
            # enqueue buy food ability for all units, if ability exists
            self.__agent.enqueue_event(eventnames.BUY_FOOD)

            # perform food effects
            self.__agent.func[item.id](self.__agent, ("team", target_pos), ("team", target_pos))

            # enqueue "eat food" ability of animal that ate, if ability exists
            self.__agent.enqueue_event(eventnames.EAT_FOOD,
                                       actor=actor)

            # enqueue "friend eats food" ability of friends, if ability exists
            self.__agent.enqueue_event(eventnames.FRIEND_EATS_FOOD,
                                       actor=actor)
            return
        else:
            # handle non targeted food e.g. sushi
            self.__agent.enqueue_event(eventnames.BUY_FOOD)

            # perform food effects
            # food function will enqueue proper EAT FOOD and FRIEND EATS FOOD events.
            self.__agent.func[item.id](self.__agent, ("team", target_pos), ("team", target_pos))
            return

    def __buy_different_animal_response(self, shop_slot, target_pos: int):
        if not self.__agent.team.has_summon_space:
            return

        actor = ("team", target_pos)
        animal: Animal = shop_slot.item
        self.__agent.gold -= animal.cost
        self.__agent.team.summon(animal, target_pos)

        self.__agent.enqueue_event(eventnames.FRIEND_SUMMONED_SHOP,
                                   actor=actor)

        self.__agent.enqueue_event(eventnames.FRIEND_BOUGHT,
                                   actor=actor)

        self.__agent.enqueue_event(eventnames.BUY,
                                   actor=actor)
        if animal.tier == 1:
            self.__agent.enqueue_event(eventnames.BUY_T1_PET,
                                       actor=actor)
        return

    def summon(self, unit: Animal, target: Tuple[str, int]):
        if target[0] == "enemy":
            return

        self.__agent.team_of_(target).summon(unit, target[1])

    def sell(self, pos: int):
        actor = ("team", pos)
        if isinstance(self.__agent.actor(actor), Empty):
            return

        animal = self.__agent.actor(actor)

        # enqueue sell event and friend sold event
        self.__agent.enqueue_event(eventnames.SELL,
                                   actor=actor)

        self.__agent.enqueue_event(eventnames.FRIEND_SOLD,
                                   actor=actor)

        self.__agent.gold += animal.level
        self.__agent.team[actor[1]] = Empty()

    def move(self, roster_init, roster_final):
        # attacking unit in roster position 0
        if roster_init - roster_final == 0:
            return

        moved_animal = self.__agent.team[roster_init]
        self.__agent.team[roster_init] = Empty()
        # if moving right, push final unit left
        if roster_init - roster_final > 0:
            # push final unit left
            self.__agent.team.make_summon_room_with_left_shift_at(roster_final)
            self.__agent.team[roster_final] = moved_animal

        # if moving left, push final unit right
        if roster_init - roster_final < 0:
            # push final unit right
            self.__agent.team.make_summon_room_with_right_shift_at(roster_final)
            self.__agent.team[roster_final] = moved_animal
        pass

    def combine(self, roster_init, roster_final):
        # final unit keeps held item
        # choose max of each of both units stats, increase final unit xp by init unit xp

        # guard clause should be same animal type
        team = self.__agent.team
        if not isinstance(team[roster_init], type(team[roster_final])):
            return

        anim1 = team[roster_init]
        anim2 = team[roster_final]
        anim1.atk = max(anim1.atk, anim2.atk)
        anim1.battle_atk = max(anim1.battle_atk, anim2.battle_atk)
        anim1.hp = max(anim1.hp, anim2.hp)
        anim1.battle_hp = max(anim1.battle_hp, anim2.battle_hp)

        level = anim2.level
        for _ in anim1.xp:
            anim2.increase_xp(1)
            new_level = anim2.level

            if new_level - level == 1:
                self.__agent.enqueue_event(eventnames.ON_LEVEL,
                                           actor=("team", roster_final))
            level = new_level
        team[roster_init] = Empty()

    def end_turn(self):
        # save backup effects are performed in start battle
        # complete end turn effects
        self.__agent.enqueue_event(eventnames.END_TURN)
