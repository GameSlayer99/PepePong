import pygame


class Settings:
    """A class to store all Pepe Pong settings."""

    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (0, 0, 0)
        self.background = pygame.image.load('images/background2.jpg')

        # Player settings
        self.player_speed_factor = 20

        # Enemy settings
        self.enemy_speed_factor = 10

        # Ball settings
        self.ball_speed_factor_x = 10
        self.ball_speed_factor_y = 5

        # Score settings
        self.player_score = 0
        self.enemy_score = 0
        self.rally = 0

        # Game scoreboard font
        self.game_font = pygame.font.Font('ArcadeNormal-ZDZ.ttf', 30)

        # Game startup flag.
        self.game_active = False
