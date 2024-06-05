import pygame
import sys
import pygame_gui
from button import MenuButton
from snake import Snake
from food import Food, SpawnGenerator
import globals as g

class PlayGame:
    def __init__(self, screen, mode='singleplayer', size = 10):
        # Flags
        self.running = True
        self.return_to_menu = False

        # Adjustable
        self.speed = 10
        
        # Game Logic
        self.width, self.height  = g.BOARD_WIDTH, g.BOARD_HEIGHT
        start_pos = (0, 0)
        snake_size = 3

        self.cell_size = g.CELLSIZE
        self.last_move = "D"
        self.snake = Snake(start_pos, snake_size)
        self.spawn_generator = SpawnGenerator(self.width, self.height, start_pos)
        self.food = Food()
        
        # UI logic
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.screen_width, self.screen_height = self.screen.get_size()
        
        # Load sounds
        self.hover_sound = pygame.mixer.Sound('hover.wav')
        self.click_sound = pygame.mixer.Sound('play.wav')
        self.food_sound = pygame.mixer.Sound('food.wav')
        
        self.back_button = MenuButton("Back", (g.BUTTON_PADDING, g.BUTTON_PADDING), hover_sound=self.hover_sound, click_sound=self.click_sound)
        
        self.off_x = (self.screen_width - self.width * self.cell_size) // 2
        self.off_y = (self.screen_height - self.height * self.cell_size) // 2
        
        # Pygame GUI Manager
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        
        # Slider
        self.speed_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((self.screen_width//2 - 150, 10), (300, 50)),
            start_value=self.speed,
            value_range=(5, 30),
            manager=self.manager
        )
        
        # Time management
        self.last_update_time = pygame.time.get_ticks()

    def update_game_elements(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button.rect.topleft = (g.BUTTON_PADDING, g.BUTTON_PADDING)
        self.off_x = (self.screen_width - self.width * self.cell_size) // 2
        self.off_y = (self.screen_height - self.height * self.cell_size) // 2
        
        # Update GUI manager dimensions
        self.manager.set_window_resolution((self.screen_width, self.screen_height))
        self.speed_slider.set_relative_position((self.screen_width//2 - 150, 10))

    def draw_border(self):
        pygame.draw.rect(
            self.screen,
            g.BORDER_COLOR,
            pygame.Rect(
                self.off_x - g.BORDER_THICKNESS,
                self.off_y - g.BORDER_THICKNESS,
                self.width * self.cell_size + g.BORDER_THICKNESS * 2,
                self.height * self.cell_size + g.BORDER_THICKNESS * 2,
            ),
            g.BORDER_THICKNESS,
        )

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0  # Maintain constant 60 FPS
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time > 1000 // self.speed:
                self.last_update_time = current_time
                self.update()

            self.handle_events()
            self.manager.update(time_delta)
            self.update_game_elements()
            if self.running:
                self.draw()
            self.manager.draw_ui(self.screen)
            pygame.display.flip()
            
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.click(event):
                    self.return_to_menu = True
                # Check if the click is on the slider
                elif self.speed_slider.rect.collidepoint(event.pos):
                    relative_x = event.pos[0] - self.speed_slider.rect.left
                    percentage = relative_x / self.speed_slider.rect.width
                    new_speed = percentage * (self.speed_slider.value_range[1] - self.speed_slider.value_range[0]) + self.speed_slider.value_range[0]
                    self.speed_slider.set_current_value(new_speed)
                    self.speed = int(new_speed)

            if event.type == pygame.KEYDOWN:
                if not changed_direction:
                    new_direction = None
                    if event.key == pygame.K_RIGHT and self.last_move != "L":
                        new_direction = "R"
                    elif event.key == pygame.K_LEFT and self.last_move != "R":
                        new_direction = "L"
                    elif event.key == pygame.K_DOWN and self.last_move != "U":
                        new_direction = "D"
                    elif event.key == pygame.K_UP and self.last_move != "D":
                        new_direction = "U"

                    if new_direction:
                        next_position = self.get_next_head_position(new_direction)
                        if not self.snake_collides_with_self(next_position):
                            self.last_move = new_direction
                            changed_direction = True

            self.manager.process_events(event)
            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED and event.ui_element == self.speed_slider:
                self.speed = int(event.value)

    def get_next_head_position(self, direction):
        head_x, head_y = self.snake.get_head()
        if direction == "R":
            return (head_x + 1, head_y)
        elif direction == "L":
            return (head_x - 1, head_y)
        elif direction == "D":
            return (head_x, head_y + 1)
        elif direction == "U":
            return (head_x, head_y - 1)

    def snake_collides_with_self(self, next_position):
        return next_position in self.snake.get_body()

    def update(self):
        direction = g.directions[self.last_move]
        self.snake.update(direction, self.food.get_position())
        head_pos = self.snake.get_head()
        tail_pos = self.snake.get_last_tail()
        
        if head_pos == self.food.get_position():
            self.food_sound.play()  # Play food sound when snake eats food
        
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

        self.draw_snake()
        self.draw_food()

    def draw_snake(self):
        body = list(self.snake.get_body())  # Convert deque to list

        # Ensure body is a list and has elements
        if body:
            # Head size
            max_size = self.cell_size
            min_size = max_size // 2  # Minimum size for the tail

            # Calculate the size step for each segment
            size_step = (max_size - min_size) / (len(body) - 1) if len(body) > 1 else 0

            for i, pos in enumerate(body):
                size = max_size - int(i * size_step)
                half_diff = (max_size - size) // 2  # Center the smaller squares
                position = (
                    pos[0] * self.cell_size + self.off_x + half_diff,
                    pos[1] * self.cell_size + self.off_y + half_diff,
                )
                rect = pygame.Rect(position, (size, size))

                # Calculate border radius based on size
                border_radius = min(size // 2, g.SNAKE_BORDER_RADIUS)

                if i == 0:
                    # Draw the head with curved edges
                    pygame.draw.rect(self.screen, g.BLACK, rect, border_radius=border_radius)
                    # Create a surface for the outline with transparency
                    outline_surface = pygame.Surface((size, size), pygame.SRCALPHA)
                    pygame.draw.rect(outline_surface, (*g.GREEN_BLACK, 128), outline_surface.get_rect(), 2, border_radius=border_radius)
                    self.screen.blit(outline_surface, position)

                    # Draw eyes based on the direction
                    eye_width = size // 5
                    eye_height = size // 10
                    eye_offset = size // 3
                    if self.last_move == "R":
                        left_eye = pygame.Rect(position[0] + eye_offset, position[1] + eye_height, eye_width, eye_height)
                        right_eye = pygame.Rect(position[0] + eye_offset, position[1] + size - 2 * eye_height, eye_width, eye_height)
                    elif self.last_move == "L":
                        left_eye = pygame.Rect(position[0] + size - eye_offset - eye_width, position[1] + eye_height, eye_width, eye_height)
                        right_eye = pygame.Rect(position[0] + size - eye_offset - eye_width, position[1] + size - 2 * eye_height, eye_width, eye_height)
                    elif self.last_move == "D":
                        left_eye = pygame.Rect(position[0] + eye_height, position[1] + eye_offset, eye_height, eye_width)
                        right_eye = pygame.Rect(position[0] + size - 2 * eye_height, position[1] + eye_offset, eye_height, eye_width)
                    elif self.last_move == "U":
                        left_eye = pygame.Rect(position[0] + eye_height, position[1] + size - eye_offset - eye_width, eye_height, eye_width)
                        right_eye = pygame.Rect(position[0] + size - 2 * eye_height, position[1] + size - eye_offset - eye_width, eye_height, eye_width)

                    # Draw the eyes as rectangles
                    pygame.draw.rect(self.screen, g.GREEN_SNAKE, left_eye)
                    pygame.draw.rect(self.screen, g.GREEN_SNAKE, right_eye)
                else:
                    # Draw the body with curved edges
                    pygame.draw.rect(self.screen, g.GREEN_SNAKE, rect, border_radius=border_radius)
                    # Create a surface for the outline with transparency
                    outline_surface = pygame.Surface((size, size), pygame.SRCALPHA)
                    pygame.draw.rect(outline_surface, (*g.BLACK, 128), outline_surface.get_rect(), 2, border_radius=border_radius)
                    self.screen.blit(outline_surface, position)

                
    def draw_food(self):
        if not self.food.get_position():
            return
        x, y = self.food.get_position()
        position = (
            x * self.cell_size + self.off_x + g.FOOD_SIZE // 2,
            y * self.cell_size + self.off_y + g.FOOD_SIZE // 2,
        )
        size = (self.cell_size - g.FOOD_SIZE, self.cell_size - g.FOOD_SIZE)
        rect = pygame.Rect(position, size)
        pygame.draw.rect(self.screen, g.FOOD_COLOR, rect, border_radius=g.FOOD_BORDER_RADIUS)
