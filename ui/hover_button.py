import pygame
from abc import ABC, abstractmethod
from config.config import GameConfig

class HoverButton(ABC):
    def __init__(self, text: str, config: GameConfig, font=None) -> None:
        """Initialize a hover button with text, position, and configuration."""
        self.config = config
        self.text_string = text
        self.highlighted = False
        self.hover_sound = self.config.HOVER_SOUND
        self.click_sound = self.config.CLICK_SOUND
        self.font = font
        self.width = self.get_width()
        self.height = self.get_height()

    @abstractmethod
    def get_width(self):
        """Get the size of the button."""
        pass

    @abstractmethod
    def get_height(self):
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

    @abstractmethod
    def get_font_size(self):
        """Get the font size of the button."""
        pass

    @abstractmethod
    def handle_click(self):
        """Handle the button logic."""
        pass

    def get_colors(self):
        """Get the text and background colors based on the highlight state."""
        default_text_color, default_bg_color = self.get_default_colors()
        text_color = default_bg_color if self.highlighted else default_text_color
        bg_color = default_text_color if self.highlighted else default_bg_color
        return text_color, bg_color

    def update_position(self, pos_x: int, pos_y: int) -> None:
        """Update the button position."""
        self._x = pos_x
        self._y = pos_y
        self.width = self.get_width()  # Ensure width is set here
        self.height = self.get_height()  # Ensure height is set here
        self.rect = pygame.Rect(self._x, self._y, self.width, self.height)

    def render(self) -> None:
        """Render the button surface."""
        self.font = pygame.font.Font(None, self.get_font_size())
        self.surface = pygame.Surface(self.get_size(), pygame.SRCALPHA)
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

    def update(self, pos_x: int, pos_y: int) -> None:
        """Update the button's position and render it."""
        self.update_position(pos_x, pos_y)
        self.render()

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

        if self.highlighted != previously_highlighted:
            self.render()

    def get_size(self):
        return self.get_width(), self.get_height()

    def click(self, event: pygame.event.Event) -> bool:
        """Handle button click event."""
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                self.click_sound.play()
                return self.handle_click()
        return False

    def draw(self, screen: pygame.Surface) -> None:
        """Display the button on the screen."""
        screen.blit(self.surface, self.rect.topleft)

    def change_text(self, text: str) -> None:
        """Change the button text and update the surface."""
        self.text_string = text
        self.render()

    def get_text(self):
        return self.text_string
