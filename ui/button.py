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
        self.rect = pygame.Rect(0, 0, 0, 0)  # Initial rect with zero size
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA)  # Initialize surface with zero size
        self.text_string = ""  # Initialize text_string to an empty string
    
    @abstractmethod
    def handle_click(self):
        """Handle the button logic."""
        pass
    
    @abstractmethod
    def change_text(self, text: str) -> None:
        """Change the button text. Must be implemented in subclasses."""
        pass

    def show(self, screen: pygame.Surface) -> None:
        """Display the button on the screen."""
        screen.blit(self.surface, self.rect.topleft)

    def click(self, event: pygame.event.Event) -> bool:
        """Handle button click event."""
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                if self.click_sound:
                    self.click_sound.play()
                self.handle_click()  # Call the button's specific click handling
                return True
        return False

    def update_highlight(self, mouse_pos: tuple[int, int]) -> None:
        """Update button highlight based on mouse position."""
        previously_highlighted = self.highlighted
        self.highlighted = self.rect.collidepoint(mouse_pos)

        if self.highlighted and not previously_highlighted:
            if self.hover_sound:
                self.hover_sound.play()
        elif not self.highlighted and previously_highlighted:
            if self.hover_sound:
                self.hover_sound.stop()

        self.change_text(self.text_string)

    @abstractmethod
    def update(self, new_pos: tuple[int, int] = None) -> None:
        """Update the button position. Must be implemented in subclasses."""
        pass
