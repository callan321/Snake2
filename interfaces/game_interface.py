import pygame
from abc import abstractmethod
from interfaces.interface import Interface

class GameInterface(Interface):
    """Abstract base class for game interfaces."""
    MILLISECONDS_PER_SECOND = 1000

    def __init__(self, screen: pygame.Surface, config) -> None:
        """Initialize the game interface with screen, dimensions, and configuration."""
        super().__init__(screen, config)
        self.paused = False
        self.last_update_time = pygame.time.get_ticks()

    def handle_logic(self) -> None:
        """Handle the game timing and updates based on game speed."""
        current_time = pygame.time.get_ticks()
        if not self.paused and current_time - self.last_update_time > GameInterface.MILLISECONDS_PER_SECOND // self.config.game_speed:
            self.last_update_time = current_time
            if not self.update_game_logic():
                self.running = False
        else:
            self.clock.tick(self.config.FPS)

    @abstractmethod
    def update_game_logic(self) -> bool:
        """Update the game logic. Must be implemented by subclasses."""
        pass 

