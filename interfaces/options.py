import pygame
from interfaces.interface import Interface
from config.config import GameConfig
from rendering.options_render import OptRenderer
from event_handler.options_event_handler import OptEventHandler

class Options(Interface):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        """Initialize the options menu with screen and configuration."""
        super().__init__(screen, config)
        self.ui = OptRenderer(screen, config)
        self.envent_handler = OptEventHandler(self)
        self.ui.init()


    def handle_events(self) -> None:
        """Handle the game events."""
        self.envent_handler.handle_events()


    def draw(self) -> None:
        """Draw the game elements."""
        self.ui.draw()



        


  

     

 
