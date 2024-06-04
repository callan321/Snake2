import pygame
import globals as g
from button import MenuButton
import sys
from collections import deque
import random


class HashQueue:
    def __init__(self, positions):
        self.data = deque()
        self.hash_map = {}
        for pos in positions:
            self.hash_map[pos] = 0

    def add_front(self, element):
        self.data.appendleft(element)
        if element in self.hash_map:
            self.hash_map[element] += 1

    def add_back(self, element):
        self.data.append(element)
        if element in self.hash_map:
            self.hash_map[element] += 1

    def pop_back(self):
        element = self.data.pop()
        if element in self.hash_map:
            self.hash_map[element] -= 1

    def peak_front(self):
        return self.data[0]

    def peak_back(self):
        return self.data[-1]

    def check(self, element):
        if self.hash_map[element] > 1:
            return True

    def get_data(self):
        return self.data


class Snake:
    def __init__(self, start_pos, positions, size=3):
        self.body = HashQueue(positions)
        self.body.add_back(start_pos)
        for _ in range(size - 1):
            self.grow()

    def update(self, direction, food):
        self.move(direction)
        if self.check_food(food):
            self.grow()

    def grow(self):
        tail_x, tail_y = self.body.peak_back()
        self.body.add_back((tail_x, tail_y))

    def move(self, direction):
        x, y = g.directions[direction]
        head_x, head_y = self.get_head()
        new_head = (head_x + x, head_y + y)
        self.body.add_front(new_head)
        self.body.pop_back()

    def get_body(self):
        return self.body.get_data()

    def get_head(self):
        return self.body.peak_front()

    def check_food(self, food):
        return self.get_head() == food.get_position()

    def check_collision(self):
        x, y = self.get_head()

        if x < 0 or x >= g.BOARD_WIDTH or y < 0 or y >= g.BOARD_HEIGHT:
            return True

        if self.body.check(self.get_head()):
            return True

        return False


class Food:
    def __init__(self, positions):
        self.pos = None
        self.positions = positions

    def update(self, snake):
        if self.pos == snake.get_head():
            self.pos = None
        elif self.pos is None:
            self.respawn(snake)

    def respawn(self, snake):
        snake_body_set = set(snake.get_body())
        available_positions = self.positions - snake_body_set
        if available_positions:
            self.pos = random.choice(list(available_positions))
        else:
            self.pos = None

    def get_position(self):
        return self.pos


class PlayGame:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button = MenuButton("Back", (g.BUTTON_PADDING, g.BUTTON_PADDING))
        self.return_to_menu = False
        positions = self.get_board_positions(g.BOARD_WIDTH, g.BOARD_HEIGHT)
        self.last_move = "D"
        self.snake = Snake((5, 5), positions)
        self.food = Food(positions)
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
                g.BORDER_RECT_WIDTH + g.BORDER_THICKNESS*2,
                g.BORDER_RECT_HEIGHT + g.BORDER_THICKNESS*2,
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
        self.snake.update(self.last_move, self.food)
        self.food.update(self.snake)
        if self.snake.check_collision():
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

    # Draw snake on screen
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

    # Draw grid on scree
    '''
    def draw_grid(self):

        for x in range(0, g.SCREEN_WIDTH, g.CELLSIZE):

            pygame.draw.line(
                self.screen,
                g.GRID_COLOR,
                (self.off_x + x, self.off_y),
                (self.off_x + x, self.off_y + g.SCREEN_HEIGHT),
            )
        for y in range(0, g.SCREEN_HEIGHT, g.CELLSIZE):
            pygame.draw.line(
                self.screen,
                g.GRID_COLOR,
                (self.off_x + 0, self.off_y + y),
                (self.off_x + g.SCREEN_WIDTH, self.off_y + y),
            )
    '''
    def get_board_positions(self, width, height):
        return {(x, y) for x in range(width) for y in range(height)}
