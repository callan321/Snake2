
import pygame
from rendering.game_ui_manager import GameUIManager
from rendering.game_renderer import GameRenderer
from logic.game_logic_human import GameLogicHuman
from config.config import GameConfig
from event_handler.game_event_handler import GameEventHandler
from interfaces.game_interface import GameInterface

class PlayGame(GameInterface):
    """Manages the main game loop and game state."""

    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        """Initialize the PlayGame class."""
        super().__init__(screen, config)
        self.ui = GameUIManager(screen, config)
        self.game_rd = GameRenderer(screen, config)
        self.event_handler = GameEventHandler(self)
        self.nsnake = 2
        self.logic = GameLogicHuman(
            config.game_width,
            config.game_height,
            controller_type=config.p1,
            snake_size=config.snake_size,
            num_snakes= self.nsnake
        )
        self.ui.init()

    def update_game_logic(self) -> bool:
        """Update the game logic."""
        return self.logic.update()

    def handle_events(self) -> None:
        """Handle the game events."""
        self.event_handler.handle_events()

    def draw(self) -> None:
        """Update game elements such as UI and renderer dimensions and Draw the game elements."""
        self.ui.draw()
        n = self.logic.get_snake_count()
        snakes = [self.logic.get_snake_body(i) for i in range(n)]
        directions = [self.logic.get_snake_body_and_direction(i)[1] for i in range(n)]
        self.game_rd.update(
            snakes,
            directions,
            self.logic.get_food_position()
        )
