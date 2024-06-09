from abc import ABC, abstractmethod
import pygame
from config.config import GameConfig


class Interface(ABC):
    """Base interface class for game interfaces with default handle_time implementation."""

    def __init__(self, screen: pygame.Surface, config : GameConfig) -> None:
        """Initialize the game interface with screen, dimensions, and configuration."""
        self.screen = screen
        self.config = config
        self.running = True
        self.clock = pygame.time.Clock()


    def run(self) -> str:
        """Run the main game loop."""
        while self.running:
            self.handle_time()
            self.handle_events()
            self.update_ui_elements()
            self.draw()
            pygame.display.flip()

            
    def handle_time(self) -> None:
        self.clock.tick(self.config.FPS)

    @abstractmethod
    def handle_events(self) -> None:
        """Handle the game events."""
        raise NotImplementedError("This method must be overridden.")

    @abstractmethod
    def update_ui_elements(self) -> None:
        """Update UI elements such as UI and renderer dimensions."""
        raise NotImplementedError("This method must be overridden.")

    @abstractmethod
    def draw(self) -> None:
        """Draw the game elements."""
        raise NotImplementedError("This method must be overridden.")




