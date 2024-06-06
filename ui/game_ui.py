import pygame
from ui.menu_button import MenuButton
from ui.speed_button import SpeedButton
import globals as g

class GameUI:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()

        # Load sounds
        self.hover_sound = pygame.mixer.Sound('hover.wav')
        self.click_sound = pygame.mixer.Sound('play.wav')
        
        self.back_button = MenuButton("Back", (g.BUTTON_PADDING, g.BUTTON_PADDING), hover_sound=self.hover_sound, click_sound=self.click_sound)
        self.speed_button = SpeedButton(
            f"Speed: 1", 
            (self.screen_width // 2 - 75, 10),
            hover_sound=self.hover_sound,
            click_sound=self.click_sound
        )

    def update_dimensions(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button.rect.topleft = (g.BUTTON_PADDING, g.BUTTON_PADDING)
        self.speed_button.rect.topleft = (self.screen_width // 2 - 75, 10)

    def handle_back_button(self, event):
        if self.back_button.click(event):
            return True
        return False

    def handle_speed_button(self, event):
        if self.speed_button.click(event):
            self.speed_button.update_speed()
            return True
        return False

    def get_current_speed(self):
        return self.speed_button.get_speed()

    def handle_events(self, event):
        pass  # No need for a manager here anymore

    def update(self, time_delta):
        pass  # No need for a manager update

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update_highlight(mouse_pos)
        self.back_button.show(self.screen)
        self.speed_button.update_highlight(mouse_pos)
        self.speed_button.show(self.screen)
