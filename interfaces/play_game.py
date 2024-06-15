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
        controllers = self.init_controller_types(config, config.n_snakes)
        self.logic = GameLogicHuman(
            config.game_width,
            config.game_height,
            controllers=controllers,
            snake_size=config.snake_size,
            num_snakes=config.n_snakes,
            game_mode=config.game_mode
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
        snake_data = self.logic.get_all_snakes_body_and_direction()
        self.game_rd.update(snake_data, self.logic.get_food_position())

    def init_controller_types(self, config: GameConfig, nsnake: int):
        controllers = []
        if nsnake == 1:
            return [config.p1]
        elif config.p1 == "Human" and config.p2 == "Human":
            controllers = ["WASD", "Arrow"]
        elif config.p1 == "Human" or config.p2 == "Human":
            controllers = ["Human"]
            
        for i in range(nsnake - len(controllers)):
            controllers += ["Greedy"]
        
        return controllers
