import pygame
from config.config import GameConfig
from ui.button import Button

class MenuButton(Button):
    def __init__(self, text: str, pos: tuple[int, int], config: GameConfig) -> None:
        super().__init__(config)
        self.text_string = text
        self._x, self._y = pos
        self.font = pygame.font.Font(None, self.config.BUTTON_FONT_SIZE)
        self.update_surface()

    def update_button_size(self) -> None:
        self.size = (self.config.MB_WIDTH, self.config.MB_HEIGHT)
        self.width, self.height = self.size

    def change_text(self, text: str) -> None:
        self.text_string = text
        self.update_surface()

    def update_surface(self) -> None:
        self.update_button_size()
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        bg_color = self.config.TEXT_COLOR if self.highlighted else self.config.BACKGROUND_COLOR
        text_color = self.config.BACKGROUND_COLOR if self.highlighted else self.config.TEXT_COLOR
        pygame.draw.rect(self.surface, bg_color, (0, 0, self.width, self.height), border_radius=self.config.MB_BORDER_RADIUS)
        text_surface = self.font.render(self.text_string, True, text_color)
        self.surface.blit(text_surface, (self.width // 2 - text_surface.get_width() // 2, self.height // 2 - text_surface.get_height() // 2))
        self.rect = pygame.Rect(self._x, self._y, self.width, self.height)

    def update(self, new_pos: tuple[int, int]) -> None:
        self._x, self._y = new_pos
        self.update_surface()
