import pygame
from ui.back_button import BackButton
from ui.speed_button import SpeedButton
from config.config import GameConfig
from rendering.renderer import Renderer

class GameUI(Renderer):
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        super().__init__(screen, config)
        self.back_button = BackButton(self.config.BACK, config)
        self.speed_button = SpeedButton(
            f"Speed: {config.game_speed // 5 - 1}",
            config=config
        )


    def update_dimensions(self) -> None:
        self.update_positions()
        self.back_button.update((self.center_w, 0))
        self.speed_button.update((self.center_w, self.config.GAME_HEIGHT + self.config.SB_HEIGHT))

    def draw(self) -> None:
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update_highlight(mouse_pos)
        self.back_button.show(self.screen)
        self.speed_button.update_highlight(mouse_pos)
        self.speed_button.show(self.screen)
        pygame.display.flip()
