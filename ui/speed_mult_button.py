from ui.cycle_button import CycleButton
from config.config import GameConfig

class SpeedMultButton(CycleButton):
  
    def get_options(self):
        return self.config.GAME_SPEED_MULT_OPT
    
    def get_attr(self):
        return self.config.game_speed_mult
    
    def get_id(self):
        return "game_speed_mult"
    
    def get_text(self, speed : int):
        if speed == 0.3: return "Snail"
        return f"Turbo: x{speed}"