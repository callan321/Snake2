import pygame
from ui.standard_button import StandardButton
from ui.speed_button import SpeedButton
from ui.speed_mult_button import SpeedMultButton
from config.config import GameConfig
from rendering.renderer import Renderer


class GameUIManager(Renderer):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        super().__init__(screen, config)
        self.back_button = StandardButton(self.config.BACK, config)
        self.speed_button = SpeedButton(config)
        self.speed_mult = SpeedMultButton(config)

    def update_element_positions(self):
        self.update_positions()
        self.back_button.update(0, 0)
        self.speed_button.update(self.center_w - self.config.std_width // 2, 0)
        self.speed_mult.update(self.center_w - self.config.std_width//2, self.screen_h - self.config.std_height)


    def update_elements(self):
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update_highlight(mouse_pos)
        self.speed_button.update_highlight(mouse_pos)
        self.speed_mult.update_highlight(mouse_pos)

    def draw(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.speed_button.draw(self.screen)
        self.back_button.draw(self.screen)
        self.speed_mult.draw(self.screen)


        
        