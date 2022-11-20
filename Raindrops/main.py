import sys
import pygame
from settings import Settings
from raindrop import Raindrop

class RainDrop:
    def __init__(self):
        pygame.init()
        self.settings =Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Make it rain!")

        self.raindrops = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _create_drops(self):
        rain = Raindrop(self)
        rain_width, rain_height = rain.rect.size

        available_space_x = self.settings.screen_width - rain_width
        self.number_rains_x = available_space_x // (2 * rain_width)

        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * rain_height)

        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_row(self, row_number):
        for rain_number in range(self.number_rains_x):
            self._create_drop(rain_number, row_number)

    def _create_drop(self, rain_number, row_number):
        rain = Raindrop(self)
        rain_width, rain_height = rain.rect.size
        rain.rect.x = rain_width + 2 * rain_width * rain_number
        rain.y = 2 * rain.rect.height * row_number
        rain.rect.y = rain.y
        self.raindrops.add(rain)


    def _update_raindrops(self):
        self.raindrops.update()
        make_new_drops = False
        for rain in self.raindrops.copy():
            if rain.check_disappeared():
                self.raindrops.remove(rain)
                make_new_drops = True

        if make_new_drops:
            self._create_row(0)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()



if __name__ == '__main__':
    rd = RainDrop()
    rd.run_game()

