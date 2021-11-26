import pygame


class Player:
    """A class to store all player info"""
    def __init__(self, pp_settings, screen):
        """Initialize the player and starting position"""
        self.screen = screen
        self.pp_settings = pp_settings

        # Load the player image and get its rect
        self.image = pygame.image.load('images/peperight.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set the player's starting position
        self.rect.right = 975
        self.rect.centery = self.screen_rect.centery

        # Set a movement flag
        self.moving_up = False
        self.moving_down = False

        # Store a decimal value for the player's center
        self.center = float(self.rect.centery)

    def update(self):
        """Update player's position based on movement flag."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.pp_settings.player_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.pp_settings.player_speed_factor

        # Update rect object from self.center.
        self.rect.centery = self.center

    def game_over_player(self):
        self.center = 250

    def blitme(self):
        """Draw the player character"""
        self.screen.blit(self.image, self.rect)
