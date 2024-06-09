from rendering.renderer import Renderer
from config.config import GameConfig
import pygame
from typing import List
from ui.menu_button import MenuButton


class MainMenuUIManager(Renderer):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        super().__init__(screen, config)
        self.buttons: List[MenuButton] = []
        self.title_font = pygame.font.Font(None, self.config.TITLE_FONT_SIZE)
        self.title_text = self.title_font.render(
            self.config.GAME_TITLE, True, self.config.TEXT_COLOR
        )
        self.create_Buttons()

    def create_Buttons(self):
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
        self.title_rect = self.title_text.get_rect(
            center=(
                self.center_w,
                self.center_h
                - self.config.TITLE_Y_OFFSET_MULTIPLIER * self.config.MB_HEIGHT,
            )
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
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.update_highlight(mouse_pos)

    def draw(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.screen.blit(self.title_text, self.title_rect)
        for button in self.buttons:
            button.show(self.screen)
