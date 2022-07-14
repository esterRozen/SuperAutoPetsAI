from typing import TYPE_CHECKING, Tuple, Optional

from ....game_elements.abstract_elements import Animal, Empty
from ....game_elements.game_objects.animals import Fly_Friend, Tiger
from ....game_elements.game_objects.equipment import Coconut

if TYPE_CHECKING:
    from ... import MessageAgent


def tiger_check(func):
    def wrapper_tiger_ability(*args, **kwargs):
        func(*args, **kwargs)
        friend_behind = args[0].team_of_(args[2]).friend_behind(args[2][1])

        # check if tiger behind
        if not isinstance(friend_behind, Tiger):
            return

        # make sure we're in battle!!
        if friend_behind.locked:
            return

        # unpacking for readability
        agent: MessageAgent = args[0]
        actor: Tuple[str, int] = args[2]
        animal = agent.actor(actor)
        if isinstance(animal, Empty):
            animal = args[4]

        # repeat ability as that level.
        prior_xp = animal.xp
        if friend_behind.level == 1:
            animal.xp = 0
        elif friend_behind.level == 2:
            animal.xp = 2
        else:
            animal.xp = 5

        func(*args, **kwargs)
        animal.xp = prior_xp

    return wrapper_tiger_ability


class Tier6:
    @staticmethod
    def boar(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.actor(actor).level == 1:
            agent.actor(actor).temp_buff(4, 2)
        elif agent.actor(actor).level == 2:
            agent.actor(actor).temp_buff(8, 4)
        elif agent.actor(actor).level == 3:
            agent.actor(actor).temp_buff(12, 6)

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
            agent.buff(agent.team.friends(actor[1]), 3, 3)

    @staticmethod
    def fly(agent: 'MessageAgent',
            actor: Tuple[str, int], target: Tuple[str, int],
            fainted: Animal):
        fly_friend = Fly_Friend()

        fly_friend.battle_hp = 4 * agent.actor(actor).level
        fly_friend.battle_atk = 4 * agent.actor(actor).level
        fly_friend.hp = 4 * agent.actor(actor).level
        fly_friend.atk = 4 * agent.actor(actor).level

        agent.summon(fly_friend, target)

    @staticmethod
    def gorilla(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.actor(actor).held = Coconut()

    @staticmethod
    def leopard(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int], backup: Animal):
        if actor[0] == "team":
            team = "enemy"
        else:
            team = "team"

        damage = backup.battle_atk // 2
        for _ in range(agent.actor(actor).level):
            unit = agent.team_opposing_(actor).random_units_idx(1)[0]
            agent.deal_ability_damage_handle_hurt(damage, actor, (team, unit), backup)

    @staticmethod
    def mammoth(agent: 'MessageAgent',
                actor: Tuple[str, int], target: Tuple[str, int],
                fainted: Animal):
        if fainted.level == 1:
            agent.buff(agent.team.friends(actor[1]), 2, 2)
        elif fainted.level == 2:
            agent.buff(agent.team.friends(actor[1]), 4, 4)
        else:
            agent.buff(agent.team.friends(actor[1]), 6, 6)

    @staticmethod
    def octopus(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if actor[0] == "team":
            team = "enemy"
        else:
            team = "team"

        units = agent.team_opposing_(actor).random_units_idx(2)
        for unit in units:
            damage = 3 * agent.actor(actor).level
            agent.deal_ability_damage_handle_hurt(damage, actor, (team, unit))

    @staticmethod
    def sauropod(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        agent.gold += agent.actor(actor).level

    @staticmethod
    def snake(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        target = agent.team_opposing_(actor).random_units_idx(1)
        if actor[0] == "team":
            target_tup = ("enemy", target[0])
        else:
            target_tup = ("team", target[0])

        agent.deal_ability_damage_handle_hurt(5 * agent.actor(actor).level,
                                              actor, target_tup)

    @staticmethod
    def tiger(agent: 'MessageAgent',
              actor: Tuple[str, int], target: Tuple[str, int],
              fainted: Optional[Animal]):
        return

    @staticmethod
    def tyrannosaurus(agent: 'MessageAgent', actor: Tuple[str, int], target: Tuple[str, int]):
        if agent.gold < 3:
            return

        if agent.actor(actor).level == 1:
            agent.buff(agent.team.friends(actor[1]), 2, 1)
        elif agent.actor(actor).level == 2:
            agent.buff(agent.team.friends(actor[1]), 4, 2)
        else:
            agent.buff(agent.team.friends(actor[1]), 6, 3)
