import pygame
from config.config import GameConfig
from interfaces.interface import Interface
from rendering.main_menu_renderer import MainMenuUIManager
from event_handler.menu_event_handler import MenuEventHandler


class MainMenu(Interface):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        """Initialize the main menu with screen and configuration."""
        super().__init__(screen, config)
        self.ui = MainMenuUIManager(screen, config)
        self.envent_handler = MenuEventHandler(self)
        self.choice = ""

    def handle_events(self) -> None:
        """Draw the game elements."""
        self.envent_handler.handle_events()

    def update(self) -> None:
        """Update UI elements such as UI and renderer dimensions."""
        self.ui.update()


