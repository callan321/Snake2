import pygame
from config.config import GameConfig
from rendering.renderer import Renderer
from ui.text import TitleText
from typing import List
from ui.standard_button import StandardButton
from ui.game_size_button import GameSizeButton
from ui.p1_button import P1Button
from ui.p2_button import P2Button
from ui.mode_button import ModeButton
from ui.snakes_button import SnakesButton


class OptRenderer(Renderer):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        super().__init__(screen, config)
        self.heading = TitleText(config.OPTIONS, config)
        self.gs_buttons: List[GameSizeButton] = []
        self.buttons = []
        self.create_buttons(config)

    def create_buttons(self, config: GameConfig):
        self.back_button = StandardButton(config.BACK, config)
        self.buttons.append(self.back_button)
        self.p1_button = P1Button(config)
        self.buttons.append(self.p1_button)
        self.p2_button = P2Button(config)
        self.buttons.append(self.p2_button)
        self.n_snakes_button = SnakesButton(config)
        self.buttons.append(self.n_snakes_button)
        self.mode = ModeButton(config)
        self.buttons.append(self.mode)
        button_data = self.config.GAME_SIZE_BUTTONS
        for label, values in button_data.items():
            button = GameSizeButton(label, self.config)
            button.number_of_cells = values["number_of_cells"]
            button.snake_size = values["snake_size"]
            self.gs_buttons.append(button)
        self.buttons = self.buttons + self.gs_buttons
        
    def update_element_positions(self):
        self.heading.update(self.center_w, self.center_h - self.center_h // 2)

        button_width = self.config.sm_width
        total_width = len(self.config.GAME_SIZE_BUTTONS) * button_width
        start_x = self.center_w - (total_width // 2) + (button_width // 2)
        for i, button in enumerate(self.gs_buttons):  # Update cell selection buttons
            button.update(start_x + i * button_width - button_width // 2, self.center_h)
        self.p1_button.update(
            self.center_w - self.config.lg_width,
            self.center_h + self.config.std_height,
        )
        self.p2_button.update(
            self.center_w,
            self.center_h + self.config.std_height,
        )
        self.back_button.update(
            self.center_w - self.config.std_width // 2,
            self.center_h + 2 * self.config.std_height,
        )
        self.n_snakes_button.update(
            self.center_w - self.config.std_width // 2,
            self.center_h - 2 * self.config.std_height,
        )
        self.mode.update(
            self.center_w - self.config.std_width // 2,
            self.center_h -  self.config.std_height,
        )
        
    def draw(self):
        """Display the options menu with the title and buttons."""
        self.screen.fill(self.config.BACKGROUND_GREEN)
        self.draw_objects(self.buttons  + [self.heading])

