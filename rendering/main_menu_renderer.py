from rendering.renderer import Renderer
from config.config import GameConfig
import pygame
from typing import List
from ui.standard_button import StandardButton
from ui.text import TitleText


class MainMenuUIManager(Renderer):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        super().__init__(screen, config)
        self.buttons: List[StandardButton] = []
        self.title = TitleText(config.GAME_TITLE, config)
        self.create_buttons()

    def create_buttons(self):
        button_labels = [
            self.config.PLAY,
            self.config.PLAY2,
            self.config.OPTIONS,
            self.config.REPLAY,
            self.config.QUIT,
        ]
        for label in button_labels:
            button = StandardButton(label, self.config)
            self.buttons.append(button)

    def update_element_positions(self):
        """Update button positions when the screen is resized."""
        self.title.update(
            self.center_w,
            self.center_h
            - 3 * self.config.std_height,
        )

        for i, button in enumerate(self.buttons):
            button.update(
                self.center_w - self.config.std_width // 2,
                self.center_h
                + i * self.config.std_height
                - 2 * self.config.std_height,
            )

    def update_elements(self):
        """Display the menu with the title and buttons."""
        self.update_hightlight(self.buttons)

    def draw(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.draw_objects(self.buttons + [self.title])
