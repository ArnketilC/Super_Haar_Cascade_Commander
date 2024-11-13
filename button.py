"""Button class for space invader."""
import pygame


class Button():
    """Button class."""

    def __init__(self, settings, screen, txt):
        """Construct for button class."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.width = 600
        self.height = 60
        self.color = pygame.Color('white')
        self.txt_color = pygame.Color('black')
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prop_text(txt)

    def prop_text(self, txt):
        """Prop some txt to the button."""
        self.txt_as_image = self.font.render(txt, True, self.color, self.txt_color)
        self.txt_as_image_rect = self.txt_as_image.get_rect()
        self.txt_as_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button."""
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.txt_as_image, self.txt_as_image_rect)
