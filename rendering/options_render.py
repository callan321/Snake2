import pygame
from config.config import GameConfig
from rendering.renderer import Renderer
from ui.text import TitleText
from typing import List
from ui.standard_button import StandardButton
from ui.game_size_button import GameSizeButton
from ui.p1_button import P1Button


class OptRenderer(Renderer):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        super().__init__(screen, config)
        self.heading = TitleText(config.OPTIONS, config)
        self.gs_buttons: List[GameSizeButton] = []
        self.back_button = StandardButton(config.BACK, config)
        self.controller_button = P1Button(config)
        self.create_buttons()

    def create_buttons(self):
        button_data = self.config.GAME_SIZE_BUTTONS
        for label, values in button_data.items():
            button = GameSizeButton(label, self.config)
            button.number_of_cells = values["number_of_cells"]
            button.snake_size = values["snake_size"]
            self.gs_buttons.append(button)

    def update_element_positions(self):
        self.heading.update(self.center_w, self.center_h - self.center_h // 2)

        button_width = self.config.sm_width
        total_width = len(self.config.GAME_SIZE_BUTTONS) * button_width
        start_x = self.center_w - (total_width // 2) + (button_width // 2)
        for i, button in enumerate(self.gs_buttons):  # Update cell selection buttons
            button.update(start_x + i * button_width - button_width // 2, self.center_h)
        self.controller_button.update(
            self.center_w - self.config.lg_width // 2,
            self.center_h + self.config.std_height,
        )
        self.back_button.update(
            self.center_w - self.config.std_width // 2,
            self.center_h + 2 * self.config.std_height,
        )

    def update_elements(self):
        mouse_pos = pygame.mouse.get_pos()
        self.controller_button.update_highlight(mouse_pos)
        self.back_button.update_highlight(mouse_pos)
        for button in self.gs_buttons:
            button.update_highlight(mouse_pos)

    def draw(self):
        """Display the options menu with the title and buttons."""
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.heading.draw(self.screen)
        self.controller_button.draw(self.screen)
        self.back_button.draw(self.screen)
        for button in self.gs_buttons:
            button.draw(self.screen)
