import pygame
import sys
from abc import ABC, abstractmethod
from config.config import GameConfig


class EventHandler(ABC):
    """Handles all events for the game."""

    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        """Initialize the EventHandler with a reference to the PlayGame instance."""
        self.screen = screen
        self.config = config

    def handle_events(self) -> None:
        """Process all pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.VIDEORESIZE:
                self.handle_resize(event)
                self.update_ui_elements()
            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                or event.type == pygame.MOUSEBUTTONUP
            ):
                self.handle_mouse_button_down(event)
            elif event.type == pygame.KEYDOWN:
                self.handle_key_down(event)
            elif event.type == pygame.KEYUP:
                self.handle_key_up(event)

    def quit_game(self) -> None:
        """Quit the game and exit the program."""
        pygame.quit()
        sys.exit()

    def handle_resize(self, event: pygame.event.Event) -> None:
        """Handle the window resize event."""
        self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        self.config.update_config(event.w, event.h)

    @abstractmethod
    def update_ui_elements(self) -> None:
        """Handle the window resize event."""
        pass 
    
    @abstractmethod
    def handle_mouse_button_down(self, event: pygame.event.Event) -> None:
        """Handle the mouse button down event."""
        pass 

    @abstractmethod
    def handle_key_down(self, event: pygame.event.Event) -> None:
        """Handle the key down event."""
        pass

    @abstractmethod
    def handle_key_up(self, event: pygame.event.Event) -> None:
        """Handle the key up event."""
        pass
