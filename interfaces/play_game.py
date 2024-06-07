import pygame
from rendering.game_ui import GameUI
from rendering.game_renderer import GameRenderer
from logic.game_logic import GameLogic
from config.config import GameConfig
from interfaces.event_handler import EventHandler

class PlayGame:
    """Manages the main game loop and game state."""

    def __init__(self, screen: pygame.Surface, width: int, height: int, config: GameConfig) -> None:
        """Initialize the PlayGame class.
        
        Args:
            screen (pygame.Surface): The pygame display surface.
            width (int): The width of the game area.
            height (int): The height of the game area.
            config (GameConfig): The game configuration.
        """
        self.screen = screen
        self.config = config
        self.clock = pygame.time.Clock()
        self.ui = GameUI(screen, config)
        self.renderer = GameRenderer(screen, width, height, config)
        self.logic = GameLogic(width, height, controller_type='AI', snake_size=config.snake_size)
        self.speed = config.game_speed
        self.return_to_menu = False
        self.running = True
        self.paused = False
        self.last_update_time = pygame.time.get_ticks()
        self.event_handler = EventHandler(self)

    def run(self) -> str:
        """Run the main game loop."""
        while self.running:
            self.clock.tick(self.config.FPS)
            self.handle_time()
            self.event_handler.handle_events()
            self.update_game_elements()
            self.draw()
            if self.return_to_menu:
                return self.config.MENU

    def handle_time(self) -> None:
        """Handle the game timing and updates based on game speed."""
        current_time = pygame.time.get_ticks()
        if not self.paused and current_time - self.last_update_time > 1000 // self.speed:
            self.last_update_time = current_time
            self.logic.update()

    def update_game_elements(self) -> None:
        """Update game elements such as UI and renderer dimensions."""
        self.ui.update_dimensions()
        self.renderer.update_screen_size()

    def draw(self) -> None:
        """Draw the game elements."""
        self.renderer.draw(self.logic.snake, self.logic.food, self.logic.controller.current_move)
        self.ui.draw()
        pygame.display.flip()
