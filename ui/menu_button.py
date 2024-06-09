from ui.hover_button import HoverButton
from config.config import GameConfig

class MenuButton(HoverButton):
    def __init__(self, text: str, config: GameConfig) -> None:
        """Initialize a menu button with text, position, and configuration."""
        super().__init__(text, config)
        self.config = config

    def get_size(self):
        """Get the size of the menu button."""
        return self.config.MB_WIDTH, self.config.MB_HEIGHT

    def get_default_colors(self):
        """Get the default text and background colors of the menu button."""
        return self.config.TEXT_COLOR, self.config.BACKGROUND_COLOR

    def get_border_radius(self):
        """Get the border radius of the menu button."""
        return self.config.MB_BORDER_RADIUS

    def get_font_size(self):
        return  self.config.BUTTON_FONT_SIZE

    def handle_click(self):
        """Handle the click event for the menu button."""
        return self.text_string
