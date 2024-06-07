import pygame
from config.config import GameConfig
from ui.button import Button

class SpeedButton(Button):
    def __init__(self, pos, config: GameConfig):
        self.config = config
        self.current_speed = self.config.game_speed
        self.border_radius = self.config.MB_BORDER_RADIUS
        self.font = pygame.font.Font(None, self.config.BUTTON_FONT_SIZE)
        self.bg = self.config.BACKGROUND_COLOR
        self.text_color = self.config.TEXT_COLOR
        self.highlighted_bg = self.config.TEXT_COLOR
        self.highlighted_text_color = self.config.BACKGROUND_COLOR
        self.highlighted = False
        super().__init__(f"Speed: {self.current_speed // 5 - 1}", pos, config)

    def update_button_size(self):
        self.font = pygame.font.Font(None, self.config.BUTTON_FONT_SIZE)
        text_surface = self.font.render(self.text_string, True, self.text_color)
        self.size = (text_surface.get_width() + 20, text_surface.get_height() + 10)
        self.width, self.height = self.size

    def change_text(self, text):
        self.text_string = text
        color = self.highlighted_text_color if self.highlighted else self.text_color
        self.text = self.font.render(text, True, color)
        self.update_surface()

    def update_surface(self):
        self.update_button_size()
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
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
        if self.current_speed > 55:
            self.current_speed = 10
        self.change_text(f"Speed: {self.current_speed // 5 - 1}")
        self.config.settings['game_settings']['game_speed'] = self.current_speed
        self.config.save_settings()
