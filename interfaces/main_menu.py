import pygame
from config.config import GameConfig
from interfaces.interface import Interface
from rendering.main_menu_renderer import MainMenuRender
from event_handler.menu_event_handler import MenuEventHandler


class MainMenu(Interface):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        """Initialize the main menu with screen and configuration."""
        super().__init__(screen, config)
        self.renderer = MainMenuRender(screen, config)
        self.event_handler = MenuEventHandler(self)

    def handle_events(self) -> None:
        """Handle the game events."""
        self.event_handler.handle_events()

    def update_ui_elements(self) -> None:
        """Update UI elements such as UI and renderer dimensions."""
        self.renderer.update_button_positions()

    def draw(self) -> None:
        """Draw the game elements."""
        self.renderer.display_menu()
