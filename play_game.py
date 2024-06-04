import pygame
import globals as g
from button import MenuButton
import sys


class PlayGame:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button = MenuButton("Back", (g.BUTTON_PADDING, g.BUTTON_PADDING))
        self.return_to_menu = False

    def update_game_elements(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.back_button.rect.topleft = (g.BUTTON_PADDING, g.BUTTON_PADDING)

    def draw_border(self):
        pygame.draw.rect(
            self.screen,
            g.BORDER_COLOR,
            pygame.Rect(
                (self.screen_width - g.BORDER_RECT_WIDTH) // 2,
                (self.screen_height - g.BORDER_RECT_HEIGHT) // 2,
                g.BORDER_RECT_WIDTH,
                g.BORDER_RECT_HEIGHT,
            ),
            g.BORDER_THICKNESS,
        )
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update_game_elements()
            self.update()
            self.draw()
            self.clock.tick(g.FRAME_RATE)  # Limit to the global frame rate
            if self.return_to_menu:
                return "menu"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(
                    (event.w, event.h), pygame.RESIZABLE
                )
            elif self.back_button.click(event):
                self.return_to_menu = True

    def update(self):
        
        pass

    def draw(self):
        self.screen.fill(g.BACKGROUND_COLOR)  # Use the global background color
        self.draw_border()
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update_highlight(mouse_pos)
        self.back_button.show(self.screen)
        pygame.display.flip()
