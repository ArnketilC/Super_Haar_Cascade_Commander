
class GameStats():
    """Stats during the game."""

    def __init__(self, settings):
        """Construct stats class."""
        self.settings = settings
        self.game_run = False
        self.high_score = 0
        self.level = 1
        self.score = 0
        self.lives = settings["player_lives"]


    def reset(self, settings):
        """Reset to initials settings."""
        self.score = 0
        self.level = 1
