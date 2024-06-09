import pygame
from config.config import GameConfig

class TitleText:
    def __init__(self, text: str, config: GameConfig):
        self.config = config
        self.text = text
        self.surface = None
        self.rect = None
        self.update()

    def update(self):
        """Update the text surface and its rectangle."""
        self.title_font = pygame.font.Font(None, self.config.TITLE_FONT_SIZE)
        self.surface = self.title_font.render(
            self.text, True, self.config.TEXT_COLOR
        )
        self.rect = self.surface.get_rect()
        
    def update_position(self, x: int, y: int):
        """Set the position of the text to be centered around (x, y)."""
        self.rect.center = (x, y)
        

    def draw(self, screen: pygame.Surface):
        """Draw the text on the screen at its current position."""
        screen.blit(self.surface, self.rect)
        