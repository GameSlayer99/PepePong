import sys
import pygame
from pygame import mixer
from time import sleep
from startup import Startup


def check_events(pp_settings):
    """Respond to key-presses and mouse events."""
    for event in pygame.event.get():
        if pp_settings.game_active:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pp_settings.game_active = False
                    pygame.mixer.music.pause()
        else:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pp_settings.game_active = True
                    pygame.mixer.music.unpause()


def update_screen(pp_settings, screen, player, enemy, ball):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen through each cycle of loop.
    screen.fill(pp_settings.bg_color)
    screen.blit(pp_settings.background, (0, 0))

    pygame.draw.line(screen, (255, 0, 0), (499, 0), (499, 500), 12)
    pygame.draw.line(screen, (0, 255, 0), (499, 0), (499, 500), 8)
    pygame.draw.line(screen, (255, 255, 255), (499, 0), (499, 500), 4)
    pygame.draw.circle(screen, (255, 0, 0), (500, 250), 14)
    pygame.draw.circle(screen, (0, 255, 0), (500, 250), 12)
    pygame.draw.circle(screen, (0, 0, 0), (500, 250), 10)
    player.blitme()
    enemy.blitme()
    ball.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

    # Initiate game over.
    if pp_settings.game_active:
        if pp_settings.player_score >= 10 and (pp_settings.player_score - pp_settings.enemy_score >= 2):
            pygame.mixer.music.pause()
            player.game_over_player()
            enemy.game_over_enemy()
            sleep(1)
            pp_settings.good_ending.play()
            startup = Startup(screen, player, "Great Job!")
            update_screen_startup(screen, pp_settings, player, enemy, startup)
            sleep(3)
            pp_settings.game_active = False
            pp_settings.player_score = 0
            pp_settings.enemy_score = 0

        elif pp_settings.enemy_score >= 10 and (pp_settings.enemy_score - pp_settings.player_score >= 2):
            pygame.mixer.music.pause()
            player.game_over_player()
            enemy.game_over_enemy()
            sleep(1)
            pp_settings.bad_ending.play()
            startup = Startup(screen, player, "Better luck next time!")
            update_screen_startup(screen, pp_settings, player, enemy, startup)
            sleep(2.5)
            pp_settings.game_active = False
            pp_settings.player_score = 0
            pp_settings.enemy_score = 0


def update_screen_startup(screen, pp_settings, player, enemy, startup):
    """Establishes initial game appearance without animating anything."""
    screen.fill(pp_settings.bg_color)
    screen.blit(pp_settings.background, (0, 0))
    pygame.draw.line(screen, (255, 0, 0), (499, 0), (499, 500), 12)
    pygame.draw.line(screen, (0, 255, 0), (499, 0), (499, 500), 8)
    pygame.draw.line(screen, (255, 255, 255), (499, 0), (499, 500), 4)
    pygame.draw.circle(screen, (255, 0, 0), (500, 250), 14)
    pygame.draw.circle(screen, (0, 255, 0), (500, 250), 12)
    pygame.draw.circle(screen, (0, 0, 0), (500, 250), 10)
    player.rect.centery = player.screen_rect.centery
    enemy.rect.centery = player.screen_rect.centery
    player.blitme()
    enemy.blitme()
    startup.draw_menu()
    pygame.display.flip()
