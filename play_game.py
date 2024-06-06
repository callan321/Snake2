import pygame
import sys
from snake import Snake
from food import Food, SpawnGenerator
import globals as g
from game_ui import GameUI
from game_renderer import GameRenderer
import pygame_gui
from controller import Controller, AIController, HumanController

class GameLogic:
    def __init__(self, width, height, controller_type='Combined', snake_size = 3):
        adjust_start_x = lambda x: x - 1 if width % 2 == 0 else x
        start_x = adjust_start_x(width // 2)
        start_pos = (start_x, 0)
        self.width, self.height =  width, height
        
        self.snake = Snake(start_pos, snake_size)
        self.spawn_generator = SpawnGenerator(self.width, self.height, start_pos)
        self.food = Food()
        
        self.controller = Controller.select(controller_type)


    def update(self):
        if isinstance(self.controller, AIController):
            direction = self.controller.get_direction(self.snake.get_head(), self.food.get_position())
        else:
            direction = self.controller.get_direction()

        self.snake.update((direction), self.food.get_position())
        head_pos = self.snake.get_head()
        tail_pos = self.snake.get_last_tail()

        if head_pos == self.food.get_position():
            # Assuming there's a method to play a sound in the logic class
            self.handle_food_collision()

        self.spawn_generator.insert(tail_pos)
        self.spawn_generator.remove(head_pos)
        self.food.update(head_pos, self.spawn_generator)

        if self.snake.check_collision(self.width, self.height):
            self.running = False

    def handle_food_collision(self):
        pass  # Implement sound handling or other logic here


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


