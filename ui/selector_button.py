from ui.hover_button import HoverButton
from config.config import GameConfig

class ControllerButton(HoverButton):
    def __init__(self, config: GameConfig) -> None:
        """Initialize a speed button with text, position, and configuration."""
        super().__init__(self.get_text(config.p1_controller), config)
        self.idx = config.CONTROLLER_TYPES.index(config.p1_controller)
    def get_size(self) -> tuple[int, int]:
        """Get the size of the speed button."""
        return  self.config.CS_BUTTON_WIDTH, self.config.CS_BUTTON_HEIGHT

    def get_default_colors(self) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
        """Get the default text and background colors of the speed button."""
        return self.config.TEXT_COLOR, self.config.BACKGROUND_COLOR

    def get_border_radius(self) -> int:
        """Get the border radius of the speed button."""
        return self.config.CS_BORDER_RADIUS

    def get_font_size(self):
        return  self.config.BUTTON_FONT_SIZE
    
    def handle_click(self):
        """Handle the click event for the speed button."""
        self.idx = (self.idx + 1) % len(self.config.CONTROLLER_TYPES)
        new_type = self.config.CONTROLLER_TYPES[self.idx]
        self.change_text(self.get_text(new_type))
        self.config.settings['game_settings']["player1_controller"] = new_type
        self.config.save_settings()
        self.config.p1_controller = new_type
        
    def get_text(self, controller : str):
        return f"Controller type: {controller}"