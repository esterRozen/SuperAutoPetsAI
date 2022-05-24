from typing import TYPE_CHECKING, Union

from ..eventnames import *
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

    def start_turn(self):
        # load backup team into normal team
        # reset temp stats
        self.__agent.load_backup()
        self.__agent.reset_temp_stats()

        # events
        # start turn
        self.__agent.handle_event(START_TURN)

        # shop flows
        self.__agent.shop.start_turn()

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
            self.__agent.event_raiser = target_pos
            self.__buy_to_empty_response(shop_slot, target_pos)
            return

        if isinstance(shop_slot.item, self.__agent.team.animals[target_pos].__class__):
            self.__agent.event_raiser = target_pos
            self.__buy_to_same_response(shop_slot, target_pos)
            return

        if isinstance(shop_slot.item, Equipment):
            self.__agent.event_raiser = target_pos
            self.__buy_equipment_response(shop_slot, target_pos)

        self.__agent.event_raiser = target_pos
        self.__buy_different_animal_response(shop_slot, target_pos)
        return

    def __buy_to_empty_response(self, shop_slot, target_pos: int):
        if isinstance(shop_slot.item, Equipment):
            return

        item: Animal = shop_slot.item

        self.__agent.gold -= item.cost
        shop_slot.buy()

        self.__agent.team.animals[target_pos] = item

        self.__agent.handle_event(FRIEND_SUMMONED_SHOP)
        self.__agent.handle_event(FRIEND_BOUGHT)
        self.__agent.handle_event(BUY)
        if item.tier == 1:
            self.__agent.handle_event(BUY_T1_PET)
        return

    def __buy_to_same_response(self, shop_slot, target_pos: int):
        target_unit = self.__agent.team.animals[target_pos]

        item: Animal = shop_slot.item

        self.__agent.gold -= item.cost
        shop_slot.buy()

        target_unit.increase_xp(1)

        self.__agent.handle_event(FRIEND_BOUGHT)
        self.__agent.handle_event(BUY)
        if item.tier == 1:
            self.__agent.handle_event(BUY_T1_PET)
        return

    def __buy_equipment_response(self, shop_slot, target_pos: int):
        target_unit = self.__agent.team.animals[target_pos]

        item: Equipment = shop_slot.item

        self.__agent.gold -= item.cost
        shop_slot.buy()

        if item.is_targeted:
            if item.is_consumable:
                # handle consumable targeted food e.g. pear
                return
            # handle non-targeted food e.g. can, sushi
            return
        # handle equipment e.g. meat bone
        self.__agent.team.animals[target_pos].held = item
        return

    def __buy_different_animal_response(self, shop_slot, target_pos: int):
        if not self.__agent.team.has_summon_space:
            return

        animal: Animal = shop_slot.item
        self.__agent.gold -= animal.cost
        self.__agent.team.summon(animal, target_pos)

        self.__agent.handle_event(FRIEND_SUMMONED_SHOP)
        self.__agent.handle_event(FRIEND_BOUGHT)
        self.__agent.handle_event(BUY)
        if animal.tier == 1:
            self.__agent.handle_event(BUY_T1_PET)
        return

    def sell(self, pos: int):
        if isinstance(self.__agent.team.animals[pos], Empty):
            return

        # set event raiser
        # handle sell event and friend sold event
        self.__agent.event_raiser = pos
        self.__agent.handle_event(SELL)
        self.__agent.handle_event(FRIEND_SOLD)

        self.__agent.gold += 1

    def move(self, roster_init, roster_final):
        pass

    def combine(self, roster_init, roster_final):
        pass

    def end_turn(self):
        # save backup effects are performed in start battle
        # complete end turn effects
        self.__agent.handle_event(END_TURN)
