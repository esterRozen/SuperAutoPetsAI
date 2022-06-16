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
        self.agent = agent
        self.agent.set_shopper(self)

    def start_turn(self):
        # load backup team into normal team
        # reset temp stats
        self.agent.load_backup()
        self.agent.reset_temp_stats()

        # shop flows
        self.agent.turn += 1
        self.agent.shop.start_turn()

        # events
        # start turn
        self.agent.enqueue_event(eventnames.START_TURN)
        self.agent.handle_events()

    def toggle_freeze(self, pos: int):
        self.agent.shop.toggle_freeze(pos)
        return

    def reroll(self):
        if self.agent.gold < 1:
            return
        self.agent.gold -= 1
        self.agent.shop.reroll()
        return

    def buy(self, item_pos: int, target_pos: int):
        # differentiate between food/equipment and animals!
        # presume it is a valid purchase
        shop_slot = self.agent.shop.roster[item_pos]

        if isinstance(shop_slot.item, Empty) or isinstance(shop_slot, Unarmed):
            return

        # guard clause, no gold, no purchase.
        if self.agent.gold < shop_slot.item.cost:
            return

        if isinstance(self.agent.team.animals[target_pos], Empty):
            self.__buy_to_empty_response(shop_slot, target_pos)
            self.agent.handle_events()
            return

        if isinstance(shop_slot.item, self.agent.team[target_pos].__class__):
            self.__buy_to_same_response(shop_slot, target_pos)
            self.agent.handle_events()
            return

        if isinstance(shop_slot.item, Equipment):
            self.__buy_equipment_response(shop_slot, target_pos)
            self.agent.handle_events()
            return

        self.__buy_different_animal_response(shop_slot, target_pos)
        self.agent.handle_events()
        return

    def __buy_to_empty_response(self, shop_slot, target_pos: int):
        if isinstance(shop_slot.item, Equipment):
            return

        target = ("team", target_pos)
        item: Animal = shop_slot.item

        self.agent.gold -= item.cost
        shop_slot.buy()

        self.agent.team.animals[target_pos] = item

        self.agent.enqueue_event(eventnames.FRIEND_SUMMONED_SHOP,
                                 actor=target)

        self.agent.enqueue_event(eventnames.FRIEND_BOUGHT,
                                 actor=target)

        self.agent.enqueue_event(eventnames.BUY,
                                 actor=target)
        if item.tier == 1:
            self.agent.enqueue_event(eventnames.BUY_T1_PET)
        return

    def __buy_to_same_response(self, shop_slot, target_pos: int):
        target_unit = self.agent.team[target_pos]
        target = ("team", target_pos)

        item: Animal = shop_slot.buy()
        self.agent.gold -= item.cost

        target_unit.increase_xp(1)

        self.agent.enqueue_event(eventnames.FRIEND_BOUGHT,
                                 actor=target)

        self.agent.enqueue_event(eventnames.BUY,
                                 actor=target)

        if item.tier == 1:
            self.agent.enqueue_event(eventnames.BUY_T1_PET,
                                     actor=("team", target_pos))
        return

    def __buy_equipment_response(self, shop_slot, target_pos: int):
        item: Equipment = shop_slot.item

        actor = ("team", target_pos)

        if item.is_targeted:
            # handle consumable targeted food e.g. pear
            # enqueue buy food ability for all units, if ability exists
            if isinstance(self.agent.team[target_pos], Empty):
                return

            self.agent.gold -= item.cost
            shop_slot.buy()

            self.agent.enqueue_event(eventnames.BUY_FOOD)

            if item.is_holdable:
                self.agent.team[target_pos].held = item
            else:
                # perform food effects
                self.agent.func[item.id](self.agent, ("team", target_pos), ("team", target_pos))

            # enqueue "eat food" ability of animal that ate, if ability exists
            self.agent.enqueue_event(eventnames.EAT_FOOD,
                                     actor=actor)

            # enqueue "friend eats food" ability of friends, if ability exists
            self.agent.enqueue_event(eventnames.FRIEND_EATS_FOOD,
                                     actor=actor)
            return
        else:
            if self.agent.team.size < 1:
                return

            self.agent.gold -= item.cost
            shop_slot.buy()

            # handle non targeted food e.g. sushi
            self.agent.enqueue_event(eventnames.BUY_FOOD)

            # perform food effects
            # food function will enqueue proper EAT FOOD and FRIEND EATS FOOD events.
            self.agent.func[item.id](self.agent, ("team", target_pos), ("team", target_pos))
            return

    def __buy_different_animal_response(self, shop_slot, target_pos: int):
        if not self.agent.team.has_summon_space:
            return

        actor = ("team", target_pos)
        animal: Animal = shop_slot.item
        self.agent.gold -= animal.cost
        self.agent.team.summon(animal, target_pos)

        self.agent.enqueue_event(eventnames.FRIEND_SUMMONED_SHOP,
                                 actor=actor)

        self.agent.enqueue_event(eventnames.FRIEND_BOUGHT,
                                 actor=actor)

        self.agent.enqueue_event(eventnames.BUY,
                                 actor=actor)
        if animal.tier == 1:
            self.agent.enqueue_event(eventnames.BUY_T1_PET,
                                     actor=actor)
        return

    def summon(self, unit: Animal, target: Tuple[str, int]):
        if target[0] == "enemy":
            return

        success = self.agent.team_of_(target).summon(unit, target[1])

        if not success:
            return

        self.agent.enqueue_event(eventnames.IS_SUMMONED,
                                 actor=target,
                                 target=target)

        self.agent.enqueue_event(eventnames.FRIEND_SUMMONED_SHOP,
                                 actor=target,
                                 target=target)

        self.agent.handle_events()
        return

    def sell(self, pos: int):
        actor = ("team", pos)
        if isinstance(self.agent.actor(actor), Empty):
            return

        animal = self.agent.actor(actor)

        # enqueue sell event and friend sold event
        self.agent.enqueue_event(eventnames.SELL,
                                 actor=actor)

        self.agent.enqueue_event(eventnames.FRIEND_SOLD,
                                 actor=actor)

        self.agent.gold += animal.level
        self.agent.team[actor[1]] = Empty()

        self.agent.handle_events()
        return

    def move(self, roster_init, roster_final):
        # attacking unit in roster position 0
        if roster_init - roster_final == 0:
            return

        moved_animal = self.agent.team[roster_init]
        self.agent.team[roster_init] = Empty()
        # if moving right, push final unit left
        if roster_init - roster_final > 0:
            # push final unit left
            self.agent.team.make_summon_room_with_left_shift_at(roster_final)
            self.agent.team[roster_final] = moved_animal

        # if moving left, push final unit right
        if roster_init - roster_final < 0:
            # push final unit right
            self.agent.team.make_summon_room_with_right_shift_at(roster_final)
            self.agent.team[roster_final] = moved_animal
        return

    def combine(self, roster_init, roster_final):
        # final unit keeps held item
        # choose max of each of both units stats, increase final unit xp by init unit xp

        # guard clause should be same animal type
        team = self.agent.team
        if not isinstance(team[roster_init], type(team[roster_final])):
            return

        anim1 = team[roster_init]
        anim2 = team[roster_final]
        anim1.atk = max(anim1.atk, anim2.atk)
        anim1.battle_atk = max(anim1.battle_atk, anim2.battle_atk)
        anim1.hp = max(anim1.hp, anim2.hp)
        anim1.battle_hp = max(anim1.battle_hp, anim2.battle_hp)

        level = anim2.level
        for _ in range(anim1.xp):
            anim2.increase_xp(1)
            new_level = anim2.level

            if new_level - level == 1:
                self.agent.enqueue_event(eventnames.ON_LEVEL,
                                         actor=("team", roster_final))
            level = new_level
        team[roster_init] = Empty()

        self.agent.handle_events()
        return

    def end_turn(self):
        # save backup effects are performed in start battle
        # complete end turn effects
        self.agent.enqueue_event(eventnames.END_TURN)
        self.agent.handle_events()
        return
