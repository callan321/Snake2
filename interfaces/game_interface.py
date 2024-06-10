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
        self.clock = pygame.time.Clock()
        self.time_accumulator = 0  # Time accumulator for logic updates
        self.curr_speed = self.config.game_speed
        self.mult = False

    def handle_logic(self) -> None:
        """Handle the game timing and updates based on game speed."""
        delta_time = self.clock.tick(self.config.FPS)  # Get the time elapsed since the last frame in milliseconds
        if not self.paused:
            self.time_accumulator += delta_time

            # Calculate the update interval based on actual game speed
            update_interval = GameInterface.MILLISECONDS_PER_SECOND // self.curr_speed

            # Update the game logic based on the time accumulated
            while self.time_accumulator >= update_interval:
                if not self.update_game_logic():
                    self.running = False
                    break
                self.time_accumulator -= update_interval


    @abstractmethod
    def update_game_logic(self) -> bool:
        """Update the game logic. Must be implemented by subclasses."""
        pass
    

