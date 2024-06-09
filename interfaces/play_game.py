import pygame
from rendering.game_ui_manager import GameUIManager
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
        self.ui = GameUIManager(screen, config)
        self.renderer = GameRenderer(screen, config)
        self.event_handler = GameEventHandler(self)
        self.logic = GameLogic(
            config.game_width,
            config.game_height,
            controller_type="AI",
            snake_size=config.snake_size,
        )

    def update_game_logic(self) -> bool:
        """Update the game logic."""
        return self.logic.update()

    def handle_events(self) -> None:
        """Handle the game events."""
        self.event_handler.handle_events()

    def update(self) -> None:
        """Update game elements such as UI and renderer dimensions and Draw the game elements."""
        self.ui.update()
        self.renderer.update(
            self.logic.snake, self.logic.food, self.logic.controller.current_move
        )
