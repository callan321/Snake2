from ui.hover_button import HoverButton
from config.config import GameConfig

class SpeedButton(HoverButton):
    def __init__(self, config: GameConfig) -> None:
        """Initialize a speed button with text, position, and configuration."""
        super().__init__(self.get_text(config.game_speed), config)
        self.current_speed = config.game_speed
        
    def get_size(self) -> tuple[int, int]:
        """Get the size of the speed button."""
        return  self.config.SB_WIDTH, self.config.SB_HEIGHT

    def get_default_colors(self) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
        """Get the default text and background colors of the speed button."""
        return self.config.TEXT_COLOR, self.config.BACKGROUND_COLOR

    def get_border_radius(self) -> int:
        """Get the border radius of the speed button."""
        return self.config.SB_BORDER_RADIUS

    def get_font_size(self):
        return  self.config.BUTTON_FONT_SIZE
    
    def handle_click(self) -> bool:
        """Handle the click event for the speed button."""
        self.current_speed += 5
        if self.current_speed > 55:
            self.current_speed = 10
        self.change_text(self.get_text(self.current_speed))
        self.config.settings['game_settings']['game_speed'] = self.current_speed
        self.config.save_settings()
        return True

    def get_text(self, speed : int):
        return f"Speed: {speed // 5 - 1}"