import pygame
from config.config import GameConfig
from ui.hover_button import HoverButton

class GameSizeButton(HoverButton):
    def __init__(self, text: str, pos: tuple[int, int], config: GameConfig) -> None:
        """Initialize a game size button with text, position, and configuration."""
        super().__init__(text, pos, config)

    def get_size(self):
        """Get the size of the game size button."""
        return self.config.GS_BUTTON_WIDTH, self.config.GS_BUTTON_HEIGHT

    def get_default_colors(self):
        """Get the default text and background colors of the game size button."""
        return self.config.TEXT_COLOR, self.config.BACKGROUND_COLOR

    def get_border_radius(self):
        """Get the border radius of the game size button."""
        return self.config.GS_BORDER_RADIUS
