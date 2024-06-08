from ui.menu_button import MenuButton
from config.config import GameConfig

class BackButton(MenuButton):
    def __init__(self, text: str, config: GameConfig) -> None:
        """Initialize a menu button with text, position, and configuration."""
        super().__init__(text, config)


    def handle_click(self) -> bool:
        """Handle the click event for the menu button."""
        return True