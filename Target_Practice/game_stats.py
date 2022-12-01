class GameStats:

    def __init__(self, tp_game):
        self.settings = tp_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.rectangles_left = self.settings.rectangle_limit


