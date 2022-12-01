import pygame
from pygame.sprite import Sprite

class Rectangle(Sprite):
    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.image = pygame.image.load('images/rectangle.bmp')
        self.screen_rect = tp_game.screen.get_rect()

        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.right


        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def _check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        self.y += (self.settings.rectangle_speed *
                   self.settings.rectangle_direction)

        self.rect.y = self.y

