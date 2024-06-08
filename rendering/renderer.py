import pygame
import sys
from ui.menu_button import MenuButton
from config.config import GameConfig
from typing import List


class Renderer:
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        self.screen = screen
        self.config = config
        self.screen_w, self.screen_h, self.center_w, self.center_h = self.update_positions()

        
    def update_positions(self) -> None:
        """Update positions of the title and buttons based on screen size."""
        self.screen_width, self.screen_height = self.screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2
        return self.screen_width, self.screen_height, self.center_w, self.center_h