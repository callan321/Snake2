from ui.standard_button import StandardButton
from config.config import GameConfig

class GameSizeButton(StandardButton):
    def __init__(self, text: str, config: GameConfig) -> None:
        """Initialize a game size button with text, position, and configuration."""
        super().__init__(text, config)
        self.number_of_cells = None
        self.snake_size = None
   

    def get_width(self): 
        return self.config.sm_width
    
    def get_border_radius(self):
        """Get the border radius of the menu button."""
        return self.config.sm_br
  
    def handle_click(self):
        """Handle the click event for the game size button."""
        self.config.settings['attributes']['number_of_cells'] = self.number_of_cells
        self.config.settings['attributes']['snake_size'] = self.snake_size
        self.config.save_settings()
        self.config.number_of_cells = self.number_of_cells
        self.config.snake_size = self.snake_size
