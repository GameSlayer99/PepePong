import pygame
import random


class Ball:
    """A class to store all ball info."""
    def __init__(self, pp_settings, screen, player):
        """Initialize the ball and starting position."""
        self.screen = screen
        self.pp_settings = pp_settings
        self.player = player

        # Draw the ball.
        self.ball = pygame.image.load('images/pxArtBall.png').convert_alpha()
        self.rect = self.ball.get_rect()
        self.screen_rect = screen.get_rect()

        # Set the ball's starting position.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def ball_restart(self):
        self.rect.center = (self.pp_settings.screen_width/2, self.pp_settings.screen_height/2)
        self.pp_settings.ball_speed_factor_x = random.choice((5, -5))
        self.pp_settings.ball_speed_factor_y = random.choice((5, -5))

    def update(self):
        """Update ball's information."""
        # Update the position.
        self.rect.centerx += self.pp_settings.ball_speed_factor_x
        self.rect.centery += self.pp_settings.ball_speed_factor_y
        if self.rect.top < 0 or self.rect.bottom > self.pp_settings.screen_height:
            self.pp_settings.ball_speed_factor_y *= -1
            self.pp_settings.wall_hit.play()

        # Update the score.
        if self.rect.right >= self.pp_settings.screen_width:
            self.pp_settings.enemy_score += 1
            self.pp_settings.score.play()
            self.ball_restart()
            self.pp_settings.rally = 0
        if self.rect.left <= 0:
            self.pp_settings.player_score += 1
            self.pp_settings.score.play()
            self.ball_restart()
            self.pp_settings.rally = 0

        # Reset the ball's position.
        if self.rect.colliderect(self.player.rect):
            if abs(self.rect.right - self.player.rect.left) <= 20:
                self.pp_settings.paddle_hit.play()
                self.pp_settings.ball_speed_factor_x = random.choice((-10, -15))
                if self.rect.centery < 200:
                    self.pp_settings.ball_speed_factor_y = random.choice((1, 5, 10, 15))
                elif self.rect.centery > 300:
                    self.pp_settings.ball_speed_factor_y = random.choice((-1, -5, -10, -15))
                else:
                    self.pp_settings.ball_speed_factor_y = random.choice((1, -1, 5, -5, 10, -10, 15, -15))
                self.pp_settings.rally += 1

        # Add the scoreboard
        self.player_text = self.pp_settings.game_font.render(str(self.pp_settings.player_score), False, (255, 255, 255))
        self.enemy_text = self.pp_settings.game_font.render(str(self.pp_settings.enemy_score), False, (255, 255, 255))
        self.rally_text = self.pp_settings.game_font.render("Rally: " + str(self.pp_settings.rally), False, (255, 255, 255))

    def blitme(self):
        """Draw the ball and scoreboard."""
        self.screen.blit(self.ball, self.rect)
        self.screen.blit(self.player_text, (742.5, 25))
        self.screen.blit(self.enemy_text, (232.5, 25))
        self.screen.blit(self.rally_text, (125, 460))
