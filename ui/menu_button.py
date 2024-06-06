import pygame
import globals as g
from ui.button import Button

class MenuButton(Button):
    def __init__(self, text, pos, hover_sound=None, click_sound=None):
        self.font = pygame.font.Font(None, g.BUTTON_FONT_SIZE)
        self.bg = g.MB_BG_COLOR
        self.text_color = g.MB_T_COLOR
        self.highlighted_bg = g.MB_HBG_COLOR
        self.highlighted_text_color = g.MB_HT_COLOR
        self.size = (g.MB_WIDTH, g.MB_HEIGHT)
        self.width, self.height = self.size
        self.border_radius = g.MB_BORDER_RADIUS 
        super().__init__(text, pos, hover_sound, click_sound)

    def change_text(self, text):
        self.text_string = text
        color = self.highlighted_text_color if self.highlighted else self.text_color
        self.text = self.font.render(text, True, color)
        self.update_surface()

    def update_surface(self):
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        bg_color = self.highlighted_bg if self.highlighted else self.bg
        self.surface.fill(g.TRANSPARENT)
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


