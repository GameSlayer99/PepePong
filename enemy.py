import pygame
import random
from pygame import mixer


class Enemy:
    """A class to store all enemy info."""

    def __init__(self, pp_settings, screen, ball, player):

        """Initialize the enemy and starting position."""
        self.pp_settings = pp_settings
        self.screen = screen
        self.ball = ball
        self.player = player

        # Load the enemy image and get its rect.
        self.image = pygame.image.load('images/pepeleft.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set the enemy's starting position.
        self.rect.left = 25
        self.rect.centery = self.screen_rect.centery

        # Set a movement flag
        self.moving_up = False
        self.moving_down = False

        # Store a decimal value for the player's center
        self.center = float(self.rect.centery)

    def update(self):
        """Update's the enemy's position."""
        if self.rect.top >= self.ball.rect.centery and self.ball.rect.centerx <= 500:
            self.rect.centery -= self.pp_settings.enemy_speed_factor
        if self.rect.bottom < self.ball.rect.centery and self.ball.rect.centerx <= 1000:
            self.rect.centery += self.pp_settings.enemy_speed_factor
        if self.rect.colliderect(self.ball.rect):
            if abs(self.rect.right - self.ball.rect.left) <= 20:
                paddle_hit = mixer.Sound('sounds/paddle_hit.wav')
                paddle_hit.play()
                self.pp_settings.ball_speed_factor_x = random.choice((10, 15))
                if self.ball.rect.centery < 200:
                    self.pp_settings.ball_speed_factor_y = random.choice((1, 5, 10))
                elif self.ball.rect.centery > 300:
                    self.pp_settings.ball_speed_factor_y = random.choice((-1, -5, -10))
                else:
                    self.pp_settings.ball_speed_factor_y = random.choice((1, -1, 5, -5, 10, -10))
                self.pp_settings.rally += 1

    def game_over_enemy(self):
        self.center = 250

    def blitme(self):
        """Draw the player character"""
        self.screen.blit(self.image, self.rect)
