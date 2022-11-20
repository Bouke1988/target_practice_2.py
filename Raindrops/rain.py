import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    def __init__(self, rg_game):
        super().__init__()
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.image = pygame.image.load('images/rain.bmp')
        self.screen_rect = rg_game.screen.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.top or self.rect.bottom < 0:
            return True


    def update(self):
        self.x += (self.settings.rain_speed *
                self.settings.fleet_direction)
        self.rect.x = self.x


