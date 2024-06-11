import pygame
from config.config import GameConfig
from abc import ABC, abstractmethod


class Renderer(ABC):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        self.screen = screen
        self.config = config
        self.screen_w, self.screen_h, self.center_w, self.center_h = 0, 0, 0, 0


    def update_positions(self) -> None:
        """Update positions of the title and buttons based on screen size."""
        self.screen_w, self.screen_h = self.screen.get_size()
        self.center_w = self.screen_w // 2
        self.center_h = self.screen_h // 2

        
    def update(self):
        self.update_positions()
        self.update_element_positions()
        self.update_elements()
        self.draw()

    @abstractmethod
    def update_element_positions(self):
        pass

    @abstractmethod
    def update_elements(self):
        pass

    @abstractmethod
    def draw(self):
        pass


