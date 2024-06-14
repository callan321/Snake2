from ui.cycle_button import CycleButton
from config.config import GameConfig

class SpeedButton(CycleButton):
    def __init__(self, config: GameConfig) -> None:
        """Initialize a speed button with text, position, and configuration."""
        super().__init__(config)

    def get_options(self):
        return self.config.GSPEEDS
    
    def get_attr(self):
        return self.config.game_speed

    def get_id(self):
        return 'game_speed'
    
    def get_text(self, delete):
        return ["Snail", "Gecko", "Python"][self.idx]