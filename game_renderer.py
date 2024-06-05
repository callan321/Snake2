import pygame
import globals as g

class GameRenderer:
    def __init__(self, screen, cell_size, offset_x, offset_y, width, height):
        self.screen = screen
        self.cell_size = cell_size
        self.off_x = offset_x
        self.off_y = offset_y
        self.width = width
        self.height = height

    def update_offset(self, offset_x, offset_y):
        self.off_x = offset_x
        self.off_y = offset_y

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

    def draw_snake(self, snake, last_move):
        body = list(snake.get_body())  # Convert deque to list

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
                    if last_move == "R":
                        left_eye = pygame.Rect(position[0] + eye_offset, position[1] + eye_height, eye_width, eye_height)
                        right_eye = pygame.Rect(position[0] + eye_offset, position[1] + size - 2 * eye_height, eye_width, eye_height)
                    elif last_move == "L":
                        left_eye = pygame.Rect(position[0] + size - eye_offset - eye_width, position[1] + eye_height, eye_width, eye_height)
                        right_eye = pygame.Rect(position[0] + size - eye_offset - eye_width, position[1] + size - 2 * eye_height, eye_width, eye_height)
                    elif last_move == "D":
                        left_eye = pygame.Rect(position[0] + eye_height, position[1] + eye_offset, eye_height, eye_width)
                        right_eye = pygame.Rect(position[0] + size - 2 * eye_height, position[1] + eye_offset, eye_height, eye_width)
                    elif last_move == "U":
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

    def draw_food(self, food):
        if not food.get_position():
            return
        x, y = food.get_position()
        position = (
            x * self.cell_size + self.off_x + g.FOOD_SIZE // 2,
            y * self.cell_size + self.off_y + g.FOOD_SIZE // 2,
        )
        size = (self.cell_size - g.FOOD_SIZE, self.cell_size - g.FOOD_SIZE)
        rect = pygame.Rect(position, size)
        pygame.draw.rect(self.screen, g.FOOD_COLOR, rect, border_radius=g.FOOD_BORDER_RADIUS)

    def draw(self, snake, food, last_move):
        self.screen.fill(g.BACKGROUND_COLOR)  # Use the global background color
        self.draw_border()
        self.draw_snake(snake, last_move)
        self.draw_food(food)
