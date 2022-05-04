from Core.Overseer.BaseAgent import BaseAgent
from Core.GameElements import *


class Triggers(BaseAgent):
    def __init__(self, mode):
        super(Triggers, self).__init__(mode)

    # acting should be the animal that is doing something
    # event raiser should be the animal whose triggers are going off.

    def before_attack(self):
        self.handle(self.team.rightmost_unit().trigger("before attack"))

    # apply to unit that acted (was bought)
    def buy(self):
        pass

    # apply to all units
    def buy_food(self):
        pass

    # apply to all units
    def buy_T1_pet(self):
        pass

    # apply to unit that acted (ate food)
    def eat_food(self):
        pass

    # apply to all units
    def end_turn(self):
        pass

    # apply to units left of event raiser
    def friend_ahead_faints(self):
        pass

    # apply to all units except event raiser
    def friend_bought(self):
        pass

    # apply to all units except event raiser
    def friend_eats_food(self):
        pass

    # apply to all units
    def friend_faints(self):
        pass

    # apply to all units
    def friend_sold(self):
        pass

    # apply to units except event raiser
    def friend_summoned_battle(self):
        pass

    # apply to units except event raiser
    def friend_summoned_shop(self):
        pass

    # apply to unit that event (got hurt)
    def hurt(self):
        pass

    # apply to unit acting (knocked unit out)
    def knock_out(self):
        pass

    # apply to unit that raised event (got knocked out)
    def on_faint(self):
        pass

    # apply to unit that raised event (went up a level)
    def on_level(self):
        pass

    # apply to unit that raised event (got sold)
    def sell(self):
        pass

    # apply to all units
    def start_battle(self):
        pass

    # apply to all units
    def start_turn(self):
        pass

##############################################################
    # handles damage system, will check for faint
    # deal damage to friendly unit
    def damage_team(self, damage, pos):
        pass

    # deal damage to enemy unit
    def deal_enemy(self, damage, pos):
        pass

