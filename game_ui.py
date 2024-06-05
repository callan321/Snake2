import pygame
import pygame_gui
from button import MenuButton
import globals as g

class GameUI:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()

        # Load sounds
        self.hover_sound = pygame.mixer.Sound('hover.wav')
        self.click_sound = pygame.mixer.Sound('play.wav')
        
        self.back_button = MenuButton("Back", (g.BUTTON_PADDING, g.BUTTON_PADDING), hover_sound=self.hover_sound, click_sound=self.click_sound)
        
        # Pygame GUI Manager
        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        
        # Slider
        self.speed_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((self.screen_width // 2 - 150, 10), (300, 50)),
            start_value=10,  # Default speed
            value_range=(5, 30),
            manager=self.manager
        )

    def update_dimensions(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button.rect.topleft = (g.BUTTON_PADDING, g.BUTTON_PADDING)
        self.manager.set_window_resolution((self.screen_width, self.screen_height))
        self.speed_slider.set_relative_position((self.screen_width // 2 - 150, 10))

    def handle_back_button(self, event):
        if self.back_button.click(event):
            return True
        return False

    def handle_speed_slider(self, event):
        if self.speed_slider.rect.collidepoint(event.pos):
            relative_x = event.pos[0] - self.speed_slider.rect.left
            percentage = relative_x / self.speed_slider.rect.width
            new_speed = (
                percentage
                * (
                    self.speed_slider.value_range[1]
                    - self.speed_slider.value_range[0]
                )
                + self.speed_slider.value_range[0]
            )
            self.speed_slider.set_current_value(new_speed)
            return int(new_speed)
        return None

    def handle_events(self, event):
        self.manager.process_events(event)

    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self):
        self.manager.draw_ui(self.screen)
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update_highlight(mouse_pos)
        self.back_button.show(self.screen)
