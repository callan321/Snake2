from ui.menu_button import MenuButton
from config.config import GameConfig

class BackButton(MenuButton):
    def __init__(self, text: str, pos: tuple[int, int], config: GameConfig) -> None:
        """Initialize a menu button with text, position, and configuration."""
        super().__init__(text, pos, config)
        self.config = config
        self.update()

    def handle_click(self):
        """Handle the click event for the menu button."""
        return self.config.MENU
