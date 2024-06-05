# play_game.py
import pygame
import sys
from button import MenuButton
from snake import Snake
from food import Food, SpawnGenerator
import globals as g

class PlayGame:
    def __init__(self, screen):
        # Flags
        self.running = True
        self.return_to_menu = False
        
        # Game Logic
        self.width, self.height  = g.BOARD_WIDTH, g.BOARD_HEIGHT
        start_pos = (0, 0)
        snake_size = 1

        self.last_move = "D"
        self.snake = Snake(start_pos, snake_size)
        self.spawn_generator = SpawnGenerator(self.width, self.height, start_pos)
        self.food = Food()
        
        # UI logic
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button = MenuButton("Back", (g.BUTTON_PADDING, g.BUTTON_PADDING))    
        self.off_x = (self.screen_width - g.BORDER_RECT_WIDTH) // 2
        self.off_y = (self.screen_height - g.BORDER_RECT_HEIGHT) // 2

    def update_game_elements(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button.rect.topleft = (g.BUTTON_PADDING, g.BUTTON_PADDING)
        self.off_x = (self.screen_width - g.BORDER_RECT_WIDTH) // 2
        self.off_y = (self.screen_height - g.BORDER_RECT_HEIGHT) // 2

    def draw_border(self):
        pygame.draw.rect(
            self.screen,
            g.BORDER_COLOR,
            pygame.Rect(
                (self.screen_width - g.BORDER_RECT_WIDTH) // 2 - g.BORDER_THICKNESS,
                (self.screen_height - g.BORDER_RECT_HEIGHT) // 2 - g.BORDER_THICKNESS,
                g.BORDER_RECT_WIDTH + g.BORDER_THICKNESS * 2,
                g.BORDER_RECT_HEIGHT + g.BORDER_THICKNESS * 2,
            ),
            g.BORDER_THICKNESS,
        )

    def run(self):
        while self.running:
            self.handle_events()
            self.update_game_elements()
            self.update()
            if self.running:
                self.draw()
            self.clock.tick(g.FRAME_RATE)
            if self.return_to_menu:
                return "menu"

    def handle_events(self):
        changed_direction = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(
                    (event.w, event.h), pygame.RESIZABLE
                )
            elif self.back_button.click(event):
                self.return_to_menu = True

            if event.type == pygame.KEYDOWN:
                if not changed_direction:
                    if event.key == pygame.K_RIGHT and self.last_move != "L":
                        self.last_move = "R"
                        changed_direction = True
                    elif event.key == pygame.K_LEFT and self.last_move != "R":
                        self.last_move = "L"
                        changed_direction = True
                    elif event.key == pygame.K_DOWN and self.last_move != "U":
                        self.last_move = "D"
                        changed_direction = True
                    elif event.key == pygame.K_UP and self.last_move != "D":
                        self.last_move = "U"
                        changed_direction = True

    def update(self):
        direction = g.directions[self.last_move]
        self.snake.update(direction, self.food.get_position())
        head_pos = self.snake.get_head()
        tail_pos = self.snake.get_last_tail()
        
        self.spawn_generator.insert(tail_pos)
        self.spawn_generator.remove(head_pos)
        
        self.food.update(head_pos, self.spawn_generator)
        
        if self.snake.check_collision(self.width, self.height):
            self.running = False

    def draw(self):
        self.screen.fill(g.BACKGROUND_COLOR)  # Use the global background color
        self.draw_border()
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update_highlight(mouse_pos)
        self.back_button.show(self.screen)

        # self.draw_grid()
        self.draw_snake()
        self.draw_food()
        pygame.display.flip()

    def draw_snake(self):
        for pos in self.snake.get_body():
            position = (
                pos[0] * g.CELLSIZE + self.off_x,
                pos[1] * g.CELLSIZE + self.off_y,
            )
            size = (g.CELLSIZE, g.CELLSIZE)
            rect = pygame.Rect(position, size)
            pygame.draw.rect(
                self.screen, g.GREEN_SNAKE, rect, border_radius=g.MB_BORDER_RADIUS
            )

    def draw_food(self):
        if not self.food.get_position():
            return
        x, y = self.food.get_position()
        position = (
            x * g.CELLSIZE + self.off_x + g.FOOD_SIZE // 2,
            y * g.CELLSIZE + self.off_y + g.FOOD_SIZE // 2,
        )
        size = (g.CELLSIZE - g.FOOD_SIZE, g.CELLSIZE - g.FOOD_SIZE)
        rect = pygame.Rect(position, size)
        pygame.draw.rect(self.screen, g.FOOD_COLOR, rect, border_radius=g.FOOD_BORDER_RADIUS)


