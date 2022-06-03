from typing import TYPE_CHECKING, Tuple

from ....game_elements.abstract_elements import Animal
from ....game_elements.game_objects.animals import Fly_Friend
from ....game_elements.game_objects.equipment import Coconut

if TYPE_CHECKING:
    from ... import MessageAgent


class Tier6:
    @staticmethod
    def boar(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(actor).temp_buff(2, 2)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).temp_buff(4, 4)
        elif agent.actor(actor).level == 3:
            agent.actor(actor).temp_buff(6, 6)

    # not 100% sure how to implement cat.
    @staticmethod
    def cat(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        # TODO
        pass

    @staticmethod
    def dragon(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.buff(agent.team.friends(actor[1]), 1, 1)
        elif agent.actor(actor).level == 2:
            agent.buff(agent.team.friends(actor[1]), 2, 2)
        else:
            agent.buff(agent.team.friends(actor[1]), 2, 2)

    @staticmethod
    def fly(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        fly_friend = Fly_Friend()

        fly_friend.battle_hp = 4 * fainted.level
        fly_friend.battle_atk = 4 * fainted.level
        fly_friend.hp = 4 * fainted.level
        fly_friend.atk = 4 * fainted.level

        agent.summon(fly_friend, target)

    @staticmethod
    def gorilla(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.actor(actor).held = Coconut()

    @staticmethod
    def leopard(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        # TODO
        pass

    @staticmethod
    def mammoth(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], fainted: Animal):
        if fainted.level == 1:
            agent.buff(agent.team.friends(actor[1]), 2, 2)
        elif fainted.level == 2:
            agent.buff(agent.team.friends(actor[1]), 4, 4)
        else:
            agent.buff(agent.team.friends(actor[1]), 6, 6)

    @staticmethod
    def octopus(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        # TODO
        pass

    @staticmethod
    def sauropod(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.gold += 1

    @staticmethod
    def snake(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        target = agent.team_opposing_(actor).random_units_idx(1)
        if actor[0] == "team":
            target_tup = ("enemy", target[0])
        else:
            target_tup = ("team", target[0])

        agent.deal_ability_damage_handle_hurt(5 * agent.actor(actor).level,
                                              actor, target_tup)

    # how to do this??
    @staticmethod
    def tiger(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        # TODO use animal id to get ability and trigger it
        pass

    @staticmethod
    def tyrannosaurus(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.gold < 3:
            return
        if agent.actor(actor).level == 1:
            agent.buff(agent.team.units(), 2, 1)
        elif agent.actor(actor).level == 2:
            agent.buff(agent.team.units(), 4, 2)
        else:
            agent.buff(agent.team.units(), 6, 3)
