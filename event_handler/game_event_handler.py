import pygame
from typing import TYPE_CHECKING
from logic.controller import HumanController
from event_handler.event_handler import EventHandler


if TYPE_CHECKING:
    from interfaces.play_game import PlayGame

class GameEventHandler(EventHandler):
    """Handles all events for the game."""

    def __init__(self, play_game: 'PlayGame') -> None:
        """Initialize the EventHandler with a reference to the PlayGame instance."""
        super().__init__(play_game.screen, play_game.config)
        self.play_game = play_game

    def update_ui_elements(self) -> None:
        """Update the Ui elements after a window resize."""
        self.play_game.ui.update_dimensions()
        self.play_game.renderer.update_screen_size()

    def handle_mouse_button_down(self, event: pygame.event.Event) -> None:
        """Handle the mouse button down event."""
        if self.play_game.ui.back_button.click(event):
            self.play_game.running = False
        if self.play_game.ui.speed_button.click(event):
            self.play_game.config.game_speed = self.play_game.ui.speed_button.current_speed

    def handle_key_down(self, event: pygame.event.Event) -> None:
        """Handle the key down event."""
        if isinstance(self.play_game.logic.controller, HumanController):
            self.play_game.logic.controller.handle_keydown(event)
        if event.key == pygame.K_p:
            self.play_game.paused = not self.play_game.paused
        elif event.key == pygame.K_SPACE:
            self.play_game.config.game_speed *= 4

    def handle_key_up(self, event: pygame.event.Event) -> None:
        """Handle the key up event."""
        if event.key == pygame.K_SPACE:
            self.play_game.config.game_speed //= 4
