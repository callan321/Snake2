from event_handler.event_handler import EventHandler
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces.main_menu import MainMenu

class MenuEventHandler(EventHandler):
    def __init__(self, menu: 'MainMenu') -> None:
        super().__init__(menu.screen, menu.config)
        self.menu = menu
                              

    def handle_mouse_button_down(self, event: pygame.event.Event) -> None:
        """Handle the mouse button down event."""
        for button in self.menu.ui.buttons:
            if button.click(event):
                self.menu.choice  = button.get_text()
                self.menu.running = False 

    def handle_key_down(self, event: pygame.event.Event) -> None:
        """Handle the key down event."""
        if event.key == pygame.K_SPACE:
            self.menu.choice  = self.config.PLAY
            self.menu.running = False 

    def handle_key_up(self, event: pygame.event.Event) -> None:
        """Handle the key up event."""
        pass
    
    def handle_mouse_pos(self, mouse_pos):
        self.update_hightlight(mouse_pos, self.menu.ui.buttons)