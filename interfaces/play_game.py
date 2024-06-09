import pygame
from rendering.game_ui import GameUI
from rendering.game_renderer import GameRenderer
from logic.game_logic import GameLogic
from config.config import GameConfig
from event_handler.game_event_handler import GameEventHandler
from interfaces.game_interface import GameInterface

class PlayGame(GameInterface):
    """Manages the main game loop and game state."""

    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        """Initialize the PlayGame class."""
        super().__init__(screen, config)
        self.ui = GameUI(screen, config)
        self.renderer = GameRenderer(screen, config)
        self.event_handler = GameEventHandler(self)
        self.logic = GameLogic(config.game_width, config.game_height, controller_type='AI', snake_size=config.snake_size)
        

    def update_game_logic(self) -> bool:
        """Update the game logic."""
        return self.logic.update()

    def handle_events(self) -> None:
        """Handle the game events."""
        self.event_handler.handle_events()

    def update_ui_elements(self) -> None:
        """Update game elements such as UI and renderer dimensions."""
        self.ui.update_dimensions()
        self.renderer.update_screen_size()

    def draw(self) -> None:
        """Draw the game elements."""
        self.renderer.draw(self.logic.snake, self.logic.food, self.logic.controller.current_move)
        self.ui.draw()
