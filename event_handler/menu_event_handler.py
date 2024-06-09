from event_handler.event_handler import EventHandler
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces.main_menu import MainMenu

class MenuEventHandler(EventHandler):
    def __init__(self, menu: 'MainMenu') -> None:
        super().__init__(menu.screen, menu.config)
        self.menu = menu
                              
    def update_ui_elements(self) -> None:
        """Handle the window resize event."""
        pass 
    
    def handle_mouse_button_down(self, event: pygame.event.Event) -> None:
        """Handle the mouse button down event."""
        for button in self.menu.ui.buttons:
            if button.click(event):
                self.menu.choice  = button.handle_click()
                self.menu.running = False 

    def handle_key_down(self, event: pygame.event.Event) -> None:
        """Handle the key down event."""
        pass

    def handle_key_up(self, event: pygame.event.Event) -> None:
        """Handle the key up event."""
        pass