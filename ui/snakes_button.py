from ui.cycle_button import CycleButton
from config.config import GameConfig

class SnakesButton(CycleButton):
        
    def get_options(self):
        return self.config.N_SNAKES
    
    def get_attr(self):
        return self.config.n_snakes

    def get_id(self):
        return 'n_snakes'
    
    def get_text(self, n : int):
        return f"Snakes: {n}"