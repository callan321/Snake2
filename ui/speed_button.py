from ui.cycle_button import CycleButton
from config.config import GameConfig

class SpeedButton(CycleButton):
        
    def get_options(self):
        return self.config.GSPEEDS
    
    def get_attr(self):
        return self.config.game_speed

    def get_id(self):
        return 'game_speed'
    
    def get_text(self, speed : int):
        return f"Speed: {speed // 10}"