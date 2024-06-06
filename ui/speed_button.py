import pygame
from config import GameConfig
from ui.button import Button

class SpeedButton(Button):
    def __init__(self, pos, initial_speed, config: GameConfig):
        self.config = config
        self.font = pygame.font.Font(None, config.BUTTON_FONT_SIZE)
        self.bg = config.BACKGROUND_COLOR
        self.text_color = config.TEXT_COLOR
        self.highlighted_bg = config.TEXT_COLOR
        self.highlighted_text_color = config.BACKGROUND_COLOR
        self.size = (config.MB_WIDTH, config.MB_HEIGHT)
        self.width, self.height = self.size
        self.border_radius = config.MB_BORDER_RADIUS
        self.current_speed = initial_speed
        super().__init__(f"Speed: {self.current_speed // 5 - 1}", pos, config)
        self.change_text(f"Speed: {self.current_speed // 5 - 1}")

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
        self.change_text(f"Speed: {self.current_speed // 5 - 1}")

    def get_speed(self):
        return self.current_speed