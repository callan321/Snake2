import pygame
import sys
from ui.menu_button import MenuButton
from config.config import GameConfig
from typing import List
from interfaces.interface import Interface
from rendering.main_menu_renderer import MainMenuRender

class MainMenu(Interface):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        """Initialize the main menu with screen and configuration."""
        super().__init__(screen, config)
        self.renderer = MainMenuRender(screen, config)

            
    def handle_events(self) -> None:
        """Handle the game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.config.update_config(event.w, event.h)
                self.update_positions()
            else:
                for button in self.renderer.buttons:
                    if button.click(event):
                        self.choice  = button.handle_click()
                        self.running = False
                     


    def update_ui_elements(self) -> None:
        """Update UI elements such as UI and renderer dimensions."""
        self.renderer.update_button_positions()
        


    def draw(self) -> None:
        """Draw the game elements."""
        self.renderer.display_menu()
    