import pygame
from abc import ABC, abstractmethod
from config.config import GameConfig
from ui.button import Button

class HoverButton(Button, ABC):
    def __init__(self, text: str, config: GameConfig) -> None:
        """Initialize a hover button with text, position, and configuration."""
        super().__init__(config)
        self.text_string = text
        self.highlighted = False
        self.font = None
        self.surface = None
        self.rect = None
        

    def get_colors(self):
        """Get the text and background colors based on the highlight state."""
        default_text_color, default_bg_color = self.get_default_colors()
        text_color = default_bg_color if self.highlighted else default_text_color
        bg_color = default_text_color if self.highlighted else default_bg_color
        return text_color, bg_color

    def update(self, new_pos: tuple[int, int] = None) -> None:
        """Update the button position and surface."""
   
        self._x, self._y = new_pos
        self.size = self.get_size()
        self.width, self.height = self.size
        self.font = pygame.font.Font(None, self.get_font_size())
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        text_color, bg_color = self.get_colors()
        border_radius = self.get_border_radius()
        pygame.draw.rect(
            self.surface,
            bg_color,
            (0, 0, self.width, self.height),
            border_radius=border_radius,
        )
        text_surface = self.font.render(self.text_string, True, text_color)
        self.surface.blit(
            text_surface,
            (
                self.width // 2 - text_surface.get_width() // 2,
                self.height // 2 - text_surface.get_height() // 2,
            ),
        )
        self.rect = pygame.Rect(self._x, self._y, self.width, self.height)
    
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
    def get_size(self):
        """Get the size of the button."""
        pass

    @abstractmethod
    def get_default_colors(self):
        """Get the default text and background colors of the button."""
        pass
    
    @abstractmethod
    def get_border_radius(self):
        """Get the border radius of the button."""
        pass
    
    def get_font_size(self):
        """Get the font size of the button."""
        pass 