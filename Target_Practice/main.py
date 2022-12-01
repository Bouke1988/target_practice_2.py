"""14-2. Target Practice: Create a rectangle at the right edge of the screen that
moves up and down at a steady rate. Then have a ship appear on the left side
of the screen that the player can move up and down while firing bullets at the
moving, rectangular target. Add a Play button that starts the game, and when
the player misses the target three times, end the game and make the Play button reappear.
 Let the player restart the game with this Play button """

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from rectangle import Rectangle
from time import sleep
from game_stats import GameStats
from button import Button



class TargetPractice:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.rectangles = pygame.sprite.Group()
        self._create_rectangle()
        self.play_button = Button(self, "GO!")




    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.screen.fill(self.settings.bg_color)
                self._update_bullets()
                self.bullets.update()
                self._update_rectangles()
                self._check_rectangle_edges()
                self.ship.update()

            self._update_screen()



    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True

            self.rectangles.empty()
            self.bullets.empty()

            self._create_rectangle()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)
                self._rectangle_missed()
        collissions = pygame.sprite.groupcollide(
            self.bullets, self.rectangles, True, True)

        if collissions:
            self._rectangle_hit()

        if not self.rectangles:
            self.bullets.empty()
            self._create_rectangle()

    def _rectangle_missed(self):
        while self.settings.attempts_left >= 0:
            self.settings.attempts_left -= 1
            self.rectangles.empty()
            self.bullets.empty()
            self._create_rectangle()
            self.ship.center_ship()
            sleep(0.5)
            self.stats.game_active = False
            self.play_button.draw_button()

    def _create_rectangle(self):
        rectangle = Rectangle(self)
        self.rectangles.add(rectangle)

    def _update_rectangles(self):
        self.rectangles.update()


    def _check_rectangle_edges(self):
        for rectangle in self.rectangles.sprites():
            if rectangle._check_edges():
                self._change_rectangle_direction()
                break

    def _change_rectangle_direction(self):
        for rectangle in self.rectangles.sprites():
            rectangle.rect.x += self.settings.rectangle_drop_speed
            self.settings.rectangle_direction *= -1

    def _rectangle_hit(self):
        if self.stats.rectangles_left > 0:
            self.stats.rectangles_left -= 1
            self.rectangles.empty()
            self.bullets.empty()
            self._create_rectangle()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rectangles.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()

