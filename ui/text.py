import pygame
from config.config import GameConfig

class TitleText:
    def __init__(self, text: str, config: GameConfig):
        self.config = config
        self.text = text
        self.surface = None
        self.rect = None
        

    def update(self, x: int, y: int):
        """Update the text surface and its rectangle."""
        self.title_font = pygame.font.Font(None, self.config.tital_f_size)
        self.surface = self.title_font.render(self.text, True, self.config.TEXT_COLOR)
        self.rect = self.surface.get_rect(center=(x, y))

    def draw(self, screen: pygame.Surface):
        """Draw the text on the screen at its current position."""
        screen.blit(self.surface, self.rect)