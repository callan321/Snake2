from ui.hover_button import HoverButton
from config.config import GameConfig


class StandardButton(HoverButton):
    def __init__(self, text: str, config: GameConfig) -> None:
        """Initialize a menu button with text, position, and configuration."""
        super().__init__(text, config)
        self.config = config

    def get_width(self):
        """Get the size of the button."""
        return self.config.std_width

    def get_height(self):
        """Get the size of the button."""
        return self.config.std_height

    def get_default_colors(self):
        """Get the default text and background colors of the menu button."""
        return self.config.TEXT_COLOR, self.config.BACKGROUND_GREEN

    def get_border_radius(self):
        """Get the border radius of the menu button."""
        return self.config.std_br

    def get_font_size(self):
        return self.config.std_f_size

    def handle_click(self):
        """Handle the click event for the menu button."""
        return True

    def get_choice(self):
        return self.text_string
