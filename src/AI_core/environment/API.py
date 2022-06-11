from gym.spaces import Dict

from src.core import Engine

__all__ = ['EngineAPI']

_limit = 50


class EngineAPI:
    def __init__(self, engine: Engine, replay):
        self.engine = engine
        self.replay = replay
        self.__free_actions_this_turn = 0

    def action(self, *args):
        """
        Processes action state commands into engine readable commands
        Args:
            *args:

        Returns:

        """
        reward = 0
        done = False

        if args[0] == "sell":
            self.engine.sell(args[1])
        elif args[0] == "buy":
            self.engine.buy(args[1], args[2])
        elif args[0] == "reroll":
            self.engine.reroll()
        elif args[0] == "end turn":
            self.engine.end_turn()

            # get a team to fight using the replay sampler.
            reward = self.engine.fight(self.replay.sample)
            done = self.engine.messenger.life == 0 or self.engine.messenger.wins == 10
            self.__free_actions_this_turn = 0

        elif self.__free_actions_this_turn > _limit:
            return self.current_state(), -0.1, False, None

        elif args[0] == "freeze":
            self.engine.freeze(args[1])
            self.__free_actions_this_turn += 1
        elif args[0] == "move":
            self.engine.move(args[1], args[2])
            self.__free_actions_this_turn += 1
        elif args[0] == "combine":
            self.engine.combine(args[1], args[2])
            self.__free_actions_this_turn += 1

        return self.current_state(), reward, done, None

    def current_state(self) -> Dict:
        pass

    def reset(self, mode: str):
        self.engine = self.engine.__class__(mode)
        return self.current_state()
