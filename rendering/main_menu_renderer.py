from rendering.renderer import Renderer
from config.config import GameConfig
import pygame
from typing import List
from ui.menu_button import MenuButton
from ui.text import TitleText


class MainMenuUIManager(Renderer):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        super().__init__(screen, config)
        self.buttons: List[MenuButton] = []
        self.create_buttons()
        self.title = TitleText(config.GAME_TITLE, config)
        self.update_element_positions()  # Ensure positions are set initially

    def create_buttons(self):
        button_labels = [
            self.config.PLAY,
            self.config.PLAY2,
            self.config.OPTIONS,
            self.config.REPLAY,
            self.config.QUIT,
        ]
        for label in button_labels:
            button = MenuButton(label, self.config)
            self.buttons.append(button)

    def update_element_positions(self):
        """Update button positions when the screen is resized."""
        self.title.update_position(
            self.center_w,
            self.center_h
            - self.config.TITLE_Y_OFFSET_MULTIPLIER * self.config.MB_HEIGHT,
        )

        for i, button in enumerate(self.buttons):
            button.update(
                (
                    self.center_w - self.config.MB_WIDTH // 2,
                    self.center_h
                    + i * self.config.MB_HEIGHT
                    - self.config.MB_Y_OFFSET * self.config.MB_HEIGHT,
                )
            )

    def update_elements(self):
        """Display the menu with the title and buttons."""
        self.title.update()
        self.update_element_positions()  # Ensure positions are updated
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.update_highlight(mouse_pos)

    def draw(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.title.draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)
