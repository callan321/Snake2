import pygame
import sys
from typing import TYPE_CHECKING
from logic.controller import HumanController

if TYPE_CHECKING:
    from play_game import PlayGame

class EventHandler:
    """Handles all events for the game."""

    def __init__(self, play_game: 'PlayGame') -> None:
        """Initialize the EventHandler with a reference to the PlayGame instance."""
        self.play_game = play_game

    def handle_events(self) -> None:
        """Process all pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.VIDEORESIZE:
                self.handle_resize(event)
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_button_down(event)
            elif event.type == pygame.KEYDOWN:
                self.handle_key_down(event)
            elif event.type == pygame.KEYUP:
                self.handle_key_up(event)

    def quit_game(self) -> None:
        """Quit the game and exit the program."""
        pygame.quit()
        sys.exit()

    def handle_resize(self, event: pygame.event.Event) -> None:
        """Handle the window resize event."""
        self.play_game.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        self.play_game.config.update_config(event.w, event.h)
        self.play_game.ui.update_dimensions()
        self.play_game.renderer.update_screen_size()

    def handle_mouse_button_down(self, event: pygame.event.Event) -> None:
        """Handle the mouse button down event."""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_game.ui.back_button.rect.collidepoint(mouse_pos):
            if self.play_game.ui.back_button.click(event):
                self.play_game.return_to_menu = True
        elif self.play_game.ui.speed_button.rect.collidepoint(mouse_pos):
            if self.play_game.ui.speed_button.click(event):
                self.play_game.speed = self.play_game.ui.speed_button.current_speed

    def handle_key_down(self, event: pygame.event.Event) -> None:
        """Handle the key down event."""
        if isinstance(self.play_game.logic.controller, HumanController):
            self.play_game.logic.controller.handle_keydown(event)
        if event.key == pygame.K_p:
            self.play_game.paused = not self.play_game.paused
        elif event.key == pygame.K_SPACE:
            self.play_game.speed *= 4

    def handle_key_up(self, event: pygame.event.Event) -> None:
        """Handle the key up event."""
        if event.key == pygame.K_SPACE:
            self.play_game.speed //= 4
