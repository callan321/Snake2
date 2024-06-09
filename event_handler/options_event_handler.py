from event_handler.event_handler import EventHandler
from config.config import GameConfig
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces.options import Options


class OptEventHandler(EventHandler):
    def __init__(self, options : 'Options') -> None:
        """Initialize the EventHandler with a reference to the PlayGame instance."""
        super().__init__(options.screen, options.config)
        self.options = options 
    
    def handle_mouse_button_down(self, event: pygame.event.Event) -> None:
        """Handle the mouse button down event."""
        if self.options.ui.back_button.click(event):
            self.options.running = False 
        for button in self.options.ui.gs_buttons:
            if button.click(event):
                button.handle_click()
        self.options.ui.controller_button.click(event)
            
    
    def handle_key_down(self, event: pygame.event.Event) -> None:
        """Handle the key down event."""
        pass

    
    def handle_key_up(self, event: pygame.event.Event) -> None:
        """Handle the key up event."""
        pass