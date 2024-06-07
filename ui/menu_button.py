from config.config import GameConfig
from ui.hover_button import HoverButton

class MenuButton(HoverButton):
    def __init__(self, text: str, pos: tuple[int, int], config: GameConfig) -> None:
        """Initialize a menu button with text, position, and configuration."""
        super().__init__(text, pos, config)
        self.config = config
        self.update()

    def get_size(self):
        """Get the size of the menu button."""
        return self.config.MB_WIDTH, self.config.MB_HEIGHT

    def get_default_colors(self):
        """Get the default text and background colors of the menu button."""
        return self.config.TEXT_COLOR, self.config.BACKGROUND_COLOR
    
    def get_border_radius(self):
        """Get the border radius of the menu button."""
        return self.config.MB_BORDER_RADIUS
