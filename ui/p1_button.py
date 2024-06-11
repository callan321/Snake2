from ui.cycle_button import CycleButton
from config.config import GameConfig

class P1Button(CycleButton):   

    def get_width(self):
        return self.config.lg_width
    
    def get_id(self):
        return 'p1'
    
    def get_options(self):
        return self.config.CONTROLLER_TYPES
    
    def get_attr(self):
        return self.config.p1
    
    def get_text(self, controller : str):
        return f"P1 Controller: {controller}"
    


