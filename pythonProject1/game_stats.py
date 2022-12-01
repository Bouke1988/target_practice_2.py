class GameStats:
    def __init__(self, rg_game):
        self.settings = rg_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.rockets_left = self.settings.rockets_limit