import sys
import pygame
from settings import Settings
from rain import Rain


class RainGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode((
                    self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Make it RAIN")
        self.rain = Rain(self)
        self.rains = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self._update_rains()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rains.draw(self.screen)
        pygame.display.flip()

    def _create_fleet(self):
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        available_space_x = self.settings.screen_width - (2 * rain_width)

        rain_height = self.rain.rect.height
        number_rains_x = available_space_x // (2 * rain_width)
        available_space_y = (self.settings.screen_height -
                             (3 * rain_height) - rain_height)
        number_rows = available_space_y // (2 * rain_height)
        for row_number in range(number_rows):
            for rain_number in range(number_rains_x):
                self._create_rain(rain_number, row_number)

    def _create_rain(self, rain_number, row_number):
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain_width = rain.rect.width
        rain.x = rain_width + 2 * rain_width * rain_number
        rain.rect.x = rain.x
        rain.rect.y = rain_height + 2 * rain.rect.height * row_number
        self.rains.add(rain)

    def _update_rains(self):
        self.rains.update()

if __name__ == '__main__':
    rg = RainGame()
    rg.run_game()

