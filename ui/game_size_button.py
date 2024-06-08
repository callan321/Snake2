from ui.hover_button import HoverButton
from config.config import GameConfig

class GameSizeButton(HoverButton):
    def __init__(self, text: str, config: GameConfig) -> None:
        """Initialize a game size button with text, position, and configuration."""
        super().__init__(text, config)
        self.number_of_cells = None
        self.snake_size = None
   

    def get_size(self):
        """Get the size of the game size button."""
        return self.config.GS_BUTTON_WIDTH, self.config.GS_BUTTON_HEIGHT

    def get_default_colors(self):
        """Get the default text and background colors of the game size button."""
        return self.config.TEXT_COLOR, self.config.BACKGROUND_COLOR

    def get_border_radius(self):
        """Get the border radius of the game size button."""
        return self.config.GS_BORDER_RADIUS

    def handle_click(self):
        """Handle the click event for the game size button."""
        self.config.settings['game_settings']['number_of_cells'] = self.number_of_cells
        self.config.settings['game_settings']['snake_size'] = self.snake_size
        self.config.save_settings()
        self.config.number_of_cells = self.number_of_cells
        self.config.snake_size = self.snake_size
