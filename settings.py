import pygame
from pygame import mixer


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

        # Game Sounds
        self.paddle_hit = mixer.Sound('sounds/paddle_hit.wav')
        self.wall_hit = mixer.Sound('sounds/wall_hit.wav')
        self.score = mixer.Sound('sounds/good_ending.wav')
        self.good_ending = mixer.Sound('sounds/good_ending1.wav')
        self.bad_ending = mixer.Sound('sounds/bad_ending.wav')
        pygame.mixer.Sound.set_volume(self.paddle_hit, 0.05)
        pygame.mixer.Sound.set_volume(self.wall_hit, 0.05)
        pygame.mixer.Sound.set_volume(self.score, 0.1)
        pygame.mixer.Sound.set_volume(self.good_ending, 0.1)
        pygame.mixer.Sound.set_volume(self.bad_ending, 0.1)
