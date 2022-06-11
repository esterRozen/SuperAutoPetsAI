from gym.spaces import Dict

from src.core import Engine

__all__ = ['EngineAPI']

_limit = 50


class EngineAPI:
    def __init__(self, engine: Engine, replay):
        self.engine = engine
        self.replay = replay

        self._action_lookup = {
            "sell": self.engine.sell,
            "buy": self.engine.buy,
            "reroll": self.engine.reroll,
            "end turn": self.engine.end_turn,
            "freeze": self.engine.freeze,
            "move": self.engine.move,
            "combine": self.engine.combine
        }

        self.__actions_this_turn = 0

    def action(self, *args):
        """
        Processes action state commands into engine readable commands
        Args:
            *args:

        Returns:

        """

        wins = self.engine.messenger.wins
        lives = self.engine.messenger.life

        if self.__actions_this_turn == _limit:
            self._action_lookup["end turn"]()
        else:
            self._action_lookup[args[0]](*args[1:])

        life_change = lives - self.engine.messenger.life

        reward = self.engine.messenger.wins - wins + life_change
        done = self.engine.messenger.wins == 10

        return self.current_state(), reward, done, None

    def current_state(self) -> Dict:
        pass

    def reset(self, mode: str):
        self.engine = self.engine.__class__(mode)
        return self.current_state()
