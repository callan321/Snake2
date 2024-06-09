import pygame
from abc import ABC, abstractmethod
from config.config import GameConfig

class Button(ABC):
    def __init__(self, config: GameConfig):
        """Initialize a button with configuration settings."""
        self.config = config
        self.highlighted = False
        self.hover_sound = pygame.mixer.Sound(config.HOVER_SOUND)
        self.click_sound = pygame.mixer.Sound(config.CLICK_SOUND)
        self.rect = pygame.Rect(0, 0, 0, 0) 
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA)  
        self.text_string = ""  
    
    @abstractmethod
    def handle_click(self):
        """Handle the button logic."""
        pass
    
    @abstractmethod
    def change_text(self, text: str) -> None:
        """Change the button text. Must be implemented in subclasses."""
        pass

    def draw(self, screen: pygame.Surface) -> None:
        """Display the button on the screen."""
        screen.blit(self.surface, self.rect.topleft)

    def click(self, event: pygame.event.Event) -> bool:
        """Handle button click event."""
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                self.click_sound.play()
                result = self.handle_click()  
                return result
        return False

    @abstractmethod
    def update(self, new_pos: tuple[int, int] = None) -> None:
        """Update the button position. Must be implemented in subclasses."""
        pass
    
    def change_text(self, text: str) -> None:
        """Change the button text and update the surface."""
        self.text_string = text
