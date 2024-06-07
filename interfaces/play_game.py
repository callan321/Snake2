import pygame
import sys
from rendering.game_ui import GameUI
from rendering.game_renderer import GameRenderer
from logic.controller import HumanController
from logic.game_logic import GameLogic
from config.config import GameConfig

class PlayGame(GameLogic):
    def __init__(self, screen, width, height, config: GameConfig):
        super().__init__(width, height, snake_size= config.snake_size)
        self.config = config
        self.last_update_time = pygame.time.get_ticks()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.ui = GameUI(screen, config)
        self.renderer = GameRenderer(screen, self.width, self.height, config)
        self.speed = self.config.game_speed
        
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
                self.config.update_config(event.w, event.h)
                self.ui.update_dimensions()
                self.renderer.update_screen_size()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.ui.handle_back_button(event):
                    self.return_to_menu = True
                elif self.ui.handle_speed_button(event):
                    self.config.update_speed()
                    self.speed = self.config.game_speed if not pygame.key.get_pressed()[pygame.K_SPACE] else self.config.game_speed * 2

            elif event.type == pygame.KEYDOWN:
                if isinstance(self.controller, HumanController):
                    self.controller.handle_keydown(event)
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                elif event.key == pygame.K_SPACE:
                    self.speed = self.speed * 2

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.speed = self.speed // 2

            self.ui.handle_events(event)

    def update_game_elements(self):
        self.ui.update_dimensions()
        self.renderer.update_screen_size()
