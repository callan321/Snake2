import pygame
import sys

from game_ui import GameUI
from game_renderer import GameRenderer
import pygame_gui
from controller import Controller, AIController, HumanController
from game_logic import GameLogic



class PlayGame(GameLogic):
    def __init__(self, screen, width, height, cell_size):
        super().__init__(width, height)
        self.cell_size = cell_size
        self.last_update_time = pygame.time.get_ticks()
        self.base_speed = 10
        self.speed = self.base_speed
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        self.ui = GameUI(screen)
        self.renderer = GameRenderer(screen, self.cell_size, self.width, self.height)

        self.return_to_menu = False
        self.running = True
        self.paused = False

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            current_time = pygame.time.get_ticks()
            if not self.paused and current_time - self.last_update_time > 1000 // self.speed:
                self.last_update_time = current_time
                self.update()

            self.handle_events()
            self.ui.update(time_delta)
            self.update_game_elements()
            self.renderer.draw(self.snake, self.food, self.controller.current_move)
            self.ui.draw()
            pygame.display.flip()

            if self.return_to_menu:
                return "menu"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.ui.handle_back_button(event):
                    self.return_to_menu = True
                else:
                    new_speed = self.ui.handle_speed_slider(event)
                    if new_speed is not None:
                        self.base_speed = new_speed
                        self.speed = new_speed if not pygame.key.get_pressed()[pygame.K_SPACE] else new_speed * 2

            elif event.type == pygame.KEYDOWN:
                if isinstance(self.controller, HumanController):
                    self.controller.handle_keydown(event)
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                elif event.key == pygame.K_SPACE:
                    self.speed = self.base_speed * 2

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.speed = self.base_speed

            self.ui.handle_events(event)
            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED and event.ui_element == self.ui.speed_slider:
                self.base_speed = int(event.value)
                self.speed = self.base_speed if not pygame.key.get_pressed()[pygame.K_SPACE] else self.base_speed * 2

    def update_game_elements(self):
        self.ui.update_dimensions()
        self.renderer.update_screen_size()


