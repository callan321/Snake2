from rendering.renderer import Renderer
from config.config import GameConfig
import pygame
from typing import List
from ui.menu_button import MenuButton

class MainMenuRender(Renderer):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        super().__init__(screen, config) 
        self.title_font = pygame.font.Font(None, self.config.TITLE_FONT_SIZE)
        self.title_text = self.title_font.render(self.config.GAME_TITLE, True, self.config.TEXT_COLOR)
        
        self.buttons: List[MenuButton] = []
        self.create_buttons(config)


    def create_buttons(self, config: GameConfig) -> None:
        """Create buttons for the main menu."""
        button_labels = [config.PLAY, config.PLAY2, config.OPTIONS, config.REPLAY, config.QUIT]
        for label in button_labels:
            button = MenuButton(
                label,
                self.config
            )
            self.buttons.append(button)
            
    def update_button_positions(self) -> None:
        """Update button positions when the screen is resized."""
        self.update_positions()

        
        self.title_rect = self.title_text.get_rect(
            center=(self.center_w, self.center_h - self.config.TITLE_Y_OFFSET_MULTIPLIER * self.config.MB_HEIGHT)
        )
        for i, button in enumerate(self.buttons):
            button.update((self.center_w - self.config.MB_WIDTH // 2, self.center_h + i * self.config.MB_HEIGHT - self.config.MB_Y_OFFSET * self.config.MB_HEIGHT))

    def display_menu(self) -> None:
        """Display the menu with the title and buttons."""
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.update_highlight(mouse_pos)
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.screen.blit(self.title_text, self.title_rect)
        for button in self.buttons:
            button.show(self.screen)

        
        
        
