# Import all relevant libraries.
import pygame
import game_functions as gf

from pygame import mixer
from settings import Settings
from player import Player
from enemy import Enemy
from ball import Ball
from startup import Startup


def run_game():
    # Initialize pygame, the clock, settings, screen, icon, and title.
    pygame.init()
    clock = pygame.time.Clock()
    pp_settings = Settings()
    screen = pygame.display.set_mode((pp_settings.screen_width, pp_settings.screen_height))
    icon = pygame.image.load('images/Pepe.bmp').convert_alpha()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Pepe Pong!')
    mixer.music.load('sounds/main_theme.wav')
    pygame.mixer.music.set_volume(0.05)
    mixer.music.play(-1)
    # Establish variables.
    player = Player(pp_settings, screen)
    ball = Ball(pp_settings, screen, player)
    enemy = Enemy(pp_settings, screen, ball, player)
    startup = Startup(screen, player, 'Press SPACE to play!')

# Start the main loop for the game.
    while True:
        gf.check_events(pp_settings)
        clock.tick(60)
        print(clock.get_fps())
        if pp_settings.game_active:
            enemy.update()
            player.update()
            ball.update()
            gf.update_screen(pp_settings, screen, player, enemy, ball)
        else:
            gf.update_screen_startup(screen, pp_settings, player, enemy, startup)


run_game()
