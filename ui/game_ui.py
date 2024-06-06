import pygame
from ui.menu_button import MenuButton
from ui.speed_button import SpeedButton
from config import GameConfig

class GameUI:
    def __init__(self, screen, initial_speed, config: GameConfig):
        self.screen = screen
        self.config = config
        self.screen_width, self.screen_height = self.screen.get_size()

        # Initialize buttons with the initial positions
        self.back_button = MenuButton("Back", (self.config.BUTTON_PADDING, self.config.BUTTON_PADDING), config)
        self.speed_button = SpeedButton(
            (self.screen_width // 2 - self.config.SPEED_BUTTON_WIDTH // 2, self.config.SPEED_BUTTON_PADDING_TOP),
            initial_speed=initial_speed,
            config=config
        )

    def update_dimensions(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button.rect.topleft = (self.config.BUTTON_PADDING, self.config.BUTTON_PADDING)
        self.speed_button.rect.topleft = (self.screen_width // 2 - self.config.SPEED_BUTTON_WIDTH // 2, self.config.SPEED_BUTTON_PADDING_TOP)

    def handle_back_button(self, event):
        return self.back_button.click(event)

    def handle_speed_button(self, event):
        if self.speed_button.click(event):
            self.speed_button.update_speed()
            return True
        return False

    def get_current_speed(self):
        return self.speed_button.get_speed()

    def handle_events(self, event):
        # Handle any additional events if needed
        pass

    def update(self, time_delta):
        # Update any additional logic if needed
        pass

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update_highlight(mouse_pos)
        self.back_button.show(self.screen)
        self.speed_button.update_highlight(mouse_pos)
        self.speed_button.show(self.screen)
        pygame.display.flip()