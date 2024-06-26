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
            self.handle_logic()
            self.handle_events()
            self.draw()
            pygame.display.flip()

            
    def handle_logic(self) -> None:
        self.clock.tick(self.config.FPS)

    @abstractmethod
    def handle_events(self) -> None:
        """Handle the game events."""
        pass

    @abstractmethod
    def draw(self) -> None:
        """Draw the game elements."""
        pass



