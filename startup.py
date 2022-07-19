import pygame.font


class Startup:
    """A class to define the startup menu."""
    def __init__(self, screen, player, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.player = player

        # Set the dimensions and properties of the menu.
        self.width, self.height = 1000, 150
        self.menu_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font('ArcadeNormal-ZDZ.ttf', 40)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.menu_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_menu(self):
        self.screen.fill(self.menu_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
