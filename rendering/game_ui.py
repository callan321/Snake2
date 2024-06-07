import pygame
from ui.menu_button import MenuButton
from ui.speed_button import SpeedButton
from config.config import GameConfig

class GameUI:
    def __init__(self, screen, config: GameConfig):
        self.screen = screen
        self.config = config
        self.screen_width, self.screen_height = self.screen.get_size()

        # Initialize buttons with the initial positions
        self.back_button = MenuButton("Back", (0, 0), config)
        self.speed_button = SpeedButton(
            (self.config.screen_width // 2 - self.config.SPEED_BUTTON_WIDTH*0.75, self.config.SPEED_BUTTON_PADDING_TOP),
            config=config
        )

    def update_dimensions(self):
        self.back_button.rect.topleft = (0, 0)
        self.back_button.update_surface()
        self.back_button.update_button_size()
        self.speed_button.rect.topleft = (self.config.screen_width // 2 - self.config.SPEED_BUTTON_WIDTH*0.75, self.config.SPEED_BUTTON_PADDING_TOP)
        
        self.speed_button.update_surface()

    def handle_back_button(self, event):
        return self.back_button.click(event)

    def handle_speed_button(self, event):
        if self.speed_button.click(event):
            self.speed_button.update_speed()
            return True
        return False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update_highlight(mouse_pos)
        self.back_button.show(self.screen)
        self.speed_button.update_highlight(mouse_pos)
        self.speed_button.show(self.screen)
        pygame.display.flip()
