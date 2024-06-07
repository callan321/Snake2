import pygame
from config.config import GameConfig
from ui.button import Button

class GameSizeButton(Button):
    def __init__(self, text, pos, config: GameConfig):
        self.config = config
        self.update_button_size()
        self.font = pygame.font.Font(None, self.config.GAME_SIZE_BUTTON_FONT_SIZE)
        self.bg = self.config.BACKGROUND_COLOR
        self.text_color = self.config.TEXT_COLOR
        self.highlighted_bg = self.config.TEXT_COLOR
        self.highlighted_text_color = self.config.BACKGROUND_COLOR
        self.border_radius = self.config.GAME_SIZE_BUTTON_BORDER_RADIUS
        super().__init__(text, pos, config)

    def update_button_size(self):
        self.size = (self.config.GAME_SIZE_BUTTON_WIDTH, self.config.GAME_SIZE_BUTTON_HEIGHT)
        self.width, self.height = self.size
        self.font = pygame.font.Font(None, self.config.GAME_SIZE_BUTTON_FONT_SIZE)

    def change_text(self, text):
        self.text_string = text
        color = self.highlighted_text_color if self.highlighted else self.text_color
        self.text = self.font.render(text, True, color)
        self.update_surface()

    def update_surface(self):
        self.update_button_size()
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
