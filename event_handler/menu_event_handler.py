from event_handler.event_handler import EventHandler
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces.main_menu import MainMenu

class MenuEventHandler(EventHandler):
    def __init__(self, menu: 'MainMenu') -> None:
        self.menu = menu
    
    
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.menu.config.update_config(event.w, event.h)
            else:
                for button in self.menu.renderer.buttons:
                    if button.click(event):
                        self.menu.choice  = button.handle_click()
                        self.menu.running = False