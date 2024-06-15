import pygame
from logic.controller.human_controllers import HumanController
from event_handler.event_handler import EventHandler
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces.play_game import PlayGame

class GameEventHandler(EventHandler):
    """Handles all events for the game."""

    def __init__(self, play_game: "PlayGame") -> None:
        """Initialize the EventHandler with a reference to the PlayGame instance."""
        super().__init__(play_game.screen, play_game.config)
        self.play_game = play_game
        self.HIT_SOUND = self.play_game.config.HIT_SOUND
        self.sound_played = False  # Flag to track if the sound has been played

    def handle_mouse_button_down(self, event: pygame.event.Event) -> None:
        """Handle the mouse button down event."""
        if self.play_game.ui.back_button.click(event):
            self.play_game.running = False
        if self.play_game.ui.speed_button.click(event):
            if not self.play_game.mult:
                self.play_game.curr_speed = self.config.game_speed
            else:
                self.play_game.curr_speed = (
                    self.config.game_speed * self.config.game_speed_mult
                )

        self.play_game.ui.speed_mult.click(event)

    def handle_key_down(self, event: pygame.event.Event) -> None:
        """Handle the key down event."""
        if 0 in self.play_game.logic.controllers:
                self.play_game.logic.get_controller(0).handle_keydown(event)
        

                  
        if event.key == pygame.K_p:
            self.play_game.paused = not self.play_game.paused
            self.play_game.game_rd.paused = self.play_game.paused
        elif event.key == pygame.K_SPACE:
            self.play_game.curr_speed *= self.play_game.config.game_speed_mult
            self.play_game.mult = True
        elif event.key == pygame.K_ESCAPE:
            self.play_game.running = False
            

    def handle_key_up(self, event: pygame.event.Event) -> None:
        """Handle the key up event."""
        if event.key == pygame.K_SPACE:
            if self.play_game.mult == False:
                pass
            else:
                self.play_game.curr_speed //= self.play_game.config.game_speed_mult
                self.play_game.mult = False

    def handle_mouse_pos(self, mouse_pos):
        self.update_hightlight(mouse_pos, self.play_game.ui.buttons)

    def reset_ui(self):
        self.play_game.ui.init()

    def handle_sounds(self):
        if self.play_game.logic.get_snake_just_ate():
            if not self.sound_played:
                self.HIT_SOUND.play()
                self.sound_played = True  # Set the flag to True after playing the sound
        else:
            self.sound_played = False  # Reset the flag when the event is no longer true
