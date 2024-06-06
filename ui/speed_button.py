import pygame
import globals as g
from ui.button import Button

class SpeedButton(Button):
    def __init__(self, text, pos):
        self.font = pygame.font.Font(None, g.BUTTON_FONT_SIZE)
        self.bg = g.BACKGROUND_COLOR
        self.text_color = g.TEXT_COLOR
        self.highlighted_bg = g.TEXT_COLOR
        self.highlighted_text_color = g.BACKGROUND_COLOR
        self.size = (g.MB_WIDTH, g.MB_HEIGHT)
        self.width, self.height = self.size
        self.border_radius = g.MB_BORDER_RADIUS 
        super().__init__(text, pos)
        self.current_speed = 10

    def change_text(self, text):
        self.text_string = text
        color = self.highlighted_text_color if self.highlighted else self.text_color
        self.text = self.font.render(text, True, color)
        self.update_surface()

    def update_surface(self):
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        bg_color = self.highlighted_bg if self.highlighted else self.bg
        pygame.draw.rect(
            self.surface, bg_color, (0, 0, self.width, self.height), border_radius=self.border_radius
        )
        self.surface.blit(
            self.text,
            (
                self.width // 2 - self.text.get_width() // 2,
                self.height // 2 - self.text.get_height() // 2,
            ),
        )
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update_speed(self):
        self.current_speed += 5
        if self.current_speed > 30:
            self.current_speed = 10
        self.change_text(f"Speed: {self.current_speed//5 - 1}")

    def get_speed(self):
        return self.current_speed

