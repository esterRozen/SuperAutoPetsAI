from typing import TYPE_CHECKING, Tuple

from .. import eventnames
from ..game_elements.abstract_elements import Empty, Unarmed, Equipment, Animal
from ..game_elements.shop import ShopSlot

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
        self.agent.gold = 10
        self.agent.shop.start_turn()

        # events
        # start turn
        self.agent.enqueue_event(eventnames.START_TURN)
        self.agent.handle_events()

    def toggle_freeze(self, pos: int) -> int:
        shop_slot = self.agent.shop[pos]
        if isinstance(shop_slot.item, Empty) or isinstance(shop_slot.item, Unarmed):
            return -1

        self.agent.shop.toggle_freeze(pos)
        return 0

    def reroll(self) -> int:
        if self.agent.gold < 1:
            return -1
        self.agent.gold -= 1
        self.agent.shop.reroll()
        return 0

    def buy(self, item_pos: int, target_pos: int) -> int:
        # differentiate between food/equipment and animals!
        # presume it is a valid purchase
        shop_slot: ShopSlot = self.agent.shop.roster[item_pos]

        if isinstance(shop_slot.item, Empty) or isinstance(shop_slot.item, Unarmed):
            return -1

        # guard clause, no gold, no purchase.
        if self.agent.gold < shop_slot.item.cost:
            return -1

        if isinstance(shop_slot.item, Animal):
            return self._buy_animal_response(shop_slot, target_pos)

        if isinstance(shop_slot.item, Equipment):
            return self.__buy_food_response(shop_slot, target_pos)

    def _buy_animal_response(self, shop_slot, target_pos: int) -> int:
        if isinstance(self.agent.team.animals[target_pos], Empty):
            success = self.__buy_to_empty_response(shop_slot, target_pos)
            self.agent.handle_events()
            return success

        if isinstance(shop_slot.item, self.agent.team[target_pos].__class__):
            success = self.__buy_to_same_response(shop_slot, target_pos)
            self.agent.handle_events()
            return success

        success = self.__buy_different_animal_response(shop_slot, target_pos)
        self.agent.handle_events()
        return success

    def __buy_to_empty_response(self, shop_slot, target_pos: int) -> int:
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
        return 0

    def __buy_to_same_response(self, shop_slot, target_pos: int) -> int:
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
        return 0

    def __buy_different_animal_response(self, shop_slot, target_pos: int) -> int:
        if not self.agent.team.has_summon_space:
            return -1

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
        return 0

    def __buy_food_response(self, shop_slot, target_pos: int) -> int:
        item: Equipment = shop_slot.item

        if item.is_targeted:
            success = self.__buy_targeted_food(shop_slot, target_pos)
            self.agent.handle_events()
            return success

        success = self.__buy_non_targeted_food(shop_slot, target_pos)
        self.agent.handle_events()
        return success

    def __buy_targeted_food(self, shop_slot, target_pos: int) -> int:
        # handle consumable targeted food e.g. pear
        # enqueue buy food ability for all units, if ability exists
        if isinstance(self.agent.team[target_pos], Empty):
            return -1

        item = shop_slot.item
        actor = ("team", target_pos)
        self.agent.gold -= item.cost
        shop_slot.buy()

        self.agent.enqueue_event(eventnames.BUY_FOOD)

        if item.is_holdable:
            self.agent.team[target_pos].held = item
        else:
            self.agent.func[item.id](self.agent, ("team", target_pos), ("team", target_pos))

        # enqueue "eat food" ability of animal that ate, if ability exists
        self.agent.enqueue_event(eventnames.EAT_FOOD,
                                 actor=actor)

        # enqueue "friend eats food" ability of friends, if ability exists
        self.agent.enqueue_event(eventnames.FRIEND_EATS_FOOD,
                                 actor=actor)
        return 0

    def __buy_non_targeted_food(self, shop_slot, target_pos: int) -> int:
        if self.agent.team.size < 1:
            return -1
        item = shop_slot.item

        self.agent.gold -= item.cost
        shop_slot.buy()

        # handle non targeted food e.g. sushi, canned food
        self.agent.enqueue_event(eventnames.BUY_FOOD)

        # perform food effects
        # food function will enqueue proper EAT FOOD and FRIEND EATS FOOD events.
        self.agent.func[item.id](self.agent, ("team", target_pos), ("team", target_pos))
        return 0

    def summon(self, unit: Animal, target: Tuple[str, int]) -> int:
        if target[0] == "enemy":
            return -1

        success = self.agent.team_of_(target).summon(unit, target[1])

        if not success:
            return -1

        self.agent.enqueue_event(eventnames.IS_SUMMONED,
                                 actor=target,
                                 target=target)

        self.agent.enqueue_event(eventnames.FRIEND_SUMMONED_SHOP,
                                 actor=target,
                                 target=target)

        self.agent.handle_events()

        return 0

    def sell(self, pos: int) -> int:
        actor = ("team", pos)
        if isinstance(self.agent.actor(actor), Empty):
            return -1

        animal = self.agent.actor(actor)

        # enqueue sell event and friend sold event
        self.agent.enqueue_event(eventnames.SELL,
                                 actor=actor,
                                 removed=animal)

        self.agent.enqueue_event(eventnames.FRIEND_SOLD,
                                 actor=actor)

        self.agent.gold += animal.level
        self.agent.team[actor[1]] = Empty()

        self.agent.handle_events()
        return 0

    def move(self, roster_init, roster_final) -> int:
        # attacking unit in roster position 0
        if isinstance(self.agent.team[roster_init], Empty):
            return -1

        if roster_init - roster_final == 0:
            return -1

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

        return 0

    def combine(self, roster_init, roster_final) -> int:
        # final unit keeps held item
        # choose max of each of both units stats, increase final unit xp by init unit xp

        team = self.agent.team
        # guard clause, unit combining should not be empty
        if isinstance(team[roster_init], Empty):
            return -1

        # guard clause, unit combined should not be empty
        if isinstance(team[roster_final], Empty):
            return -1

        # guard clause, units should not be each other
        if roster_init - roster_final == 0:
            return -1

        # guard clause should be same animal type
        if not isinstance(team[roster_init], type(team[roster_final])):
            return -1

        anim1 = team[roster_init]
        anim2 = team[roster_final]
        anim2.atk = max(anim1.atk, anim2.atk)
        anim2.battle_atk = max(anim1.battle_atk, anim2.battle_atk)
        anim2.hp = max(anim1.hp, anim2.hp)
        anim2.battle_hp = max(anim1.battle_hp, anim2.battle_hp)

        higher = max(anim1, anim2, key=lambda anim: anim.xp).xp
        lower = min(anim1, anim2, key=lambda anim: anim.xp).xp

        anim2.xp = higher
        anim1.xp = lower

        level = anim2.level
        for _ in range(anim1.xp + 1):
            anim2.increase_xp(1)
            new_level = anim2.level

            if new_level - level == 1:
                self.agent.enqueue_event(eventnames.ON_LEVEL,
                                         actor=("team", roster_final))
            level = new_level
        team[roster_init] = Empty()

        self.agent.handle_events()
        return 0

    def end_turn(self):
        # save backup effects are performed in start battle
        # complete end turn effects
        self.agent.enqueue_event(eventnames.END_TURN)
        self.agent.handle_events()
        return
