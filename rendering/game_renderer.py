import pygame
from config.config import GameConfig
from collections import deque
from typing import Tuple, List, Deque

class GameRenderer:
    def __init__(self, screen, config: GameConfig):
        self.screen = screen
        self.config = config
        self.WIDTH = config.game_width
        self.HEIGHT = config.game_height

    def update_offsets(self):
        self.cell_size = self.config.cell_size
        screen_width, screen_height = self.screen.get_size()
        self.off_x = (screen_width - self.WIDTH * self.cell_size) // 2
        self.off_y = (screen_height - self.HEIGHT * self.cell_size) // 2

    def update_sizes(self):
        self.SNAKE_BORDER_RADIUS = self.cell_size // 3
        self.FOOD_SIZE = self.cell_size // 6

    def update_screen_size(self):
        self.update_offsets()
        self.update_sizes()

    def draw_border(self):
        pygame.draw.rect(
            self.screen,
            self.config.BORDER_COLOR,
            pygame.Rect(
                self.off_x - self.config.gbt,
                self.off_y - self.config.gbt,
                self.WIDTH * self.cell_size + self.config.gbt * 2,
                self.HEIGHT * self.cell_size + self.config.gbt * 2,
            ),
            self.config.gbt,
        )

    def draw_snake(self, snake, last_direction: Tuple[int, int]):
        body = snake

        if body:
            max_size = self.cell_size
            min_size = max_size // 2
            size_step = (max_size - min_size) / (len(body) - 1) if len(body) > 1 else 0

            for i, pos in enumerate(body):
                size = max_size - int(i * size_step)
                half_diff = (max_size - size) // 2
                position = (
                    pos[0] * self.cell_size + self.off_x + half_diff,
                    pos[1] * self.cell_size + self.off_y + half_diff,
                )
                rect = pygame.Rect(position, (size, size))
                border_radius = min(size // 2, self.SNAKE_BORDER_RADIUS)

                if i == 0:
                    pygame.draw.rect(self.screen, self.config.BORDER_COLOR, rect, border_radius=border_radius)
                    outline_surface = pygame.Surface((size, size), pygame.SRCALPHA)
                    pygame.draw.rect(outline_surface, self.config.BORDER_COLOR, outline_surface.get_rect(), 2, border_radius=border_radius)
                    self.screen.blit(outline_surface, position)
                    
                    eye_width = size // 4
                    eye_height = size // 8
                    eye_offset = size // 3
                    
                    left_eye = right_eye = pygame.Rect(0, 0, eye_width, eye_height)
                    tongue_points = [(0, 0), (0, 0), (0, 0)]

                    if last_direction == (1, 0):  # Right
                        left_eye = pygame.Rect(position[0] + eye_offset, position[1] + eye_height, eye_width, eye_height)
                        right_eye = pygame.Rect(position[0] + eye_offset, position[1] + size - 2 * eye_height, eye_width, eye_height)
                        tongue_points = [(position[0] + size + eye_width, position[1] + size // 2),
                                         (position[0] + size, position[1] + size // 2 - eye_height),
                                         (position[0] + size, position[1] + size // 2 + eye_height)]
                    elif last_direction == (-1, 0):  # Left
                        left_eye = pygame.Rect(position[0] + size - eye_offset - eye_width, position[1] + eye_height, eye_width, eye_height)
                        right_eye = pygame.Rect(position[0] + size - eye_offset - eye_width, position[1] + size - 2 * eye_height, eye_width, eye_height)
                        tongue_points = [(position[0] - eye_width, position[1] + size // 2),
                                         (position[0], position[1] + size // 2 - eye_height),
                                         (position[0], position[1] + size // 2 + eye_height)]
                    elif last_direction == (0, 1):  # Down
                        left_eye = pygame.Rect(position[0] + eye_height, position[1] + eye_offset, eye_height, eye_width)
                        right_eye = pygame.Rect(position[0] + size - 2 * eye_height, position[1] + eye_offset, eye_height, eye_width)
                        tongue_points = [(position[0] + size // 2, position[1] + size + eye_height),
                                         (position[0] + size // 2 - eye_width, position[1] + size),
                                         (position[0] + size // 2 + eye_width, position[1] + size)]
                    elif last_direction == (0, -1):  # Up
                        left_eye = pygame.Rect(position[0] + eye_height, position[1] + size - eye_offset - eye_width, eye_height, eye_width)
                        right_eye = pygame.Rect(position[0] + size - 2 * eye_height, position[1] + size - eye_offset - eye_width, eye_height, eye_width)
                        tongue_points = [(position[0] + size // 2, position[1] - eye_height),
                                         (position[0] + size // 2 - eye_width, position[1]),
                                         (position[0] + size // 2 + eye_width, position[1])]
                    
                    pygame.draw.rect(self.screen, self.config.GREEN_SNAKE, left_eye)
                    pygame.draw.rect(self.screen, self.config.GREEN_SNAKE, right_eye)
                    pygame.draw.polygon(self.screen, self.config.RED, tongue_points)
                else:
                    pygame.draw.rect(self.screen, self.config.GREEN_SNAKE, rect, border_radius=border_radius)
                    outline_surface = pygame.Surface((size, size), pygame.SRCALPHA)
                    pygame.draw.rect(outline_surface, (*self.config.BORDER_COLOR, self.config.SNAKE_TRANS), outline_surface.get_rect(), 2, border_radius=border_radius)
                    self.screen.blit(outline_surface, position)

    def draw_food(self, food):
        if not food:
            return
        x, y = food
        position = (
            x * self.cell_size + self.off_x + self.FOOD_SIZE // 2,
            y * self.cell_size + self.off_y + self.FOOD_SIZE // 2,
        )
        size = (self.cell_size - self.FOOD_SIZE, self.cell_size - self.FOOD_SIZE)
        rect = pygame.Rect(position, size)
        pygame.draw.rect(self.screen, self.config.FOOD_COLOR, rect)

    def draw(self, snakes: List[Deque[Tuple[int, int]]], directions: List[Tuple[int, int]], food):
        self.draw_border()
        for snake, direction in zip(snakes, directions):
            self.draw_snake(snake, direction)
        self.draw_food(food)

    def update(self, snakes: List[Deque[Tuple[int, int]]], directions: List[Tuple[int, int]], food):
        self.update_screen_size()
        self.draw(snakes, directions, food)