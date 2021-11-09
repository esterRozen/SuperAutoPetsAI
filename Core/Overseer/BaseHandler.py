class BaseHandler:
    def load(self, team, turn, gold=10, shop=None, hearts=4, battle_lost=False):
        pass

    def send_engine_message(self, message):
        pass

    def handle(self, message):
        pass
