from ui.cycle_button import CycleButton
from config.config import GameConfig

class ModeButton(CycleButton):


    def get_id(self):
        return 'game_mode'

    def get_options(self):
        return self.config.GAME_MODES

    def get_attr(self):
        return self.config.game_mode

    def get_text(self, mode: str):
        return f"{mode}"
