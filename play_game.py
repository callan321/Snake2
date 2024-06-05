import pygame
import sys
from snake import Snake
from food import Food, SpawnGenerator
import globals as g
from game_ui import GameUI
from game_renderer import GameRenderer
import pygame_gui
from controller import GameController

class PlayGame:
    def __init__(self, screen, mode="singleplayer", size=10):
        # Flags
        self.running = True
        self.return_to_menu = False

        # Adjustable
        self.speed = 10

        # Game Logic
        self.width, self.height = g.BOARD_WIDTH, g.BOARD_HEIGHT
        start_pos = (0, 0)
        snake_size = 3

        self.cell_size = g.CELLSIZE
        self.snake = Snake(start_pos, snake_size)
        self.spawn_generator = SpawnGenerator(self.width, self.height, start_pos)
        self.food = Food()
        
        #
        self.controller = GameController()
        
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.screen_width, self.screen_height = self.screen.get_size()

        # Time management
        self.last_update_time = pygame.time.get_ticks()

        # Initialize GameUI, GameRenderer, and GameController
        self.ui = GameUI(screen)
        self.renderer = GameRenderer(
            screen,
            self.cell_size,
            (self.screen_width - self.width * self.cell_size) // 2,
            (self.screen_height - self.height * self.cell_size) // 2,
            self.width,
            self.height,
        )
        

    def update_game_elements(self):
        self.ui.update_dimensions()
        self.renderer.update_offset(
            (self.screen_width - self.width * self.cell_size) // 2,
            (self.screen_height - self.height * self.cell_size) // 2,
        )

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0  # Maintain constant 60 FPS
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time > 1000 // self.speed:
                self.last_update_time = current_time
                self.update()

            self.handle_events()
            self.ui.update(time_delta)
            self.update_game_elements()
            if self.running:
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
                self.screen = pygame.display.set_mode(
                    (event.w, event.h), pygame.RESIZABLE
                )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.ui.handle_back_button(event):
                    self.return_to_menu = True
                else:
                    new_speed = self.ui.handle_speed_slider(event)
                    if new_speed is not None:
                        self.speed = new_speed

            if event.type == pygame.KEYDOWN:
                if not self.controller.changed_direction:
                    self.controller.handle_keydown(event)

            self.ui.handle_events(event)
            if (
                event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED
                and event.ui_element == self.ui.speed_slider
            ):
                self.speed = int(event.value)

    def update(self):
       

        self.controller.reset_changed_direction()
        
        self.snake.update(self.controller.direction, self.food.get_position())
        head_pos = self.snake.get_head()
        tail_pos = self.snake.get_last_tail()

        if head_pos == self.food.get_position():
            self.ui.back_button.click_sound.play()  # Play food sound when snake eats food

        self.spawn_generator.insert(tail_pos)
        self.spawn_generator.remove(head_pos)

        self.food.update(head_pos, self.spawn_generator)

        if self.snake.check_collision(self.width, self.height):
            self.running = False




