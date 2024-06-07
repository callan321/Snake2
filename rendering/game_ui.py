import pygame
from ui.back_button import BackButton
from ui.speed_button import SpeedButton
from config.config import GameConfig

class GameUI:
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        self.screen = screen
        self.config = config
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button = BackButton(self.config.BACK, (0, 0), config)
        self.speed_button = SpeedButton(
            "Speed: 1",
            (self.config.screen_width // 2 - self.config.SPEED_BUTTON_WIDTH * 0.75, self.config.SPEED_BUTTON_PADDING_TOP),
            config=config
        )
        self.update_dimensions()

    def update_dimensions(self) -> None:
        self.back_button.rect.topleft = (0, 0)
        self.back_button.update()
        self.speed_button.rect.topleft = (self.config.screen_width // 2 - self.config.SPEED_BUTTON_WIDTH * 0.75, self.config.SPEED_BUTTON_PADDING_TOP)
        self.speed_button.update()

    def draw(self) -> None:
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update_highlight(mouse_pos)
        self.back_button.show(self.screen)
        self.speed_button.update_highlight(mouse_pos)
        self.speed_button.show(self.screen)
        pygame.display.flip()

