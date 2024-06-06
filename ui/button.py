import pygame
from abc import ABC, abstractmethod
import globals as g 

class Button(ABC):
    def __init__(self, text, pos, hover_sound= g.HOVER_SOUND, click_sound=g.CLICK_SOUND):
        self.x, self.y = pos
        self.text_string = text
        self.highlighted = False
        self.hover_sound = pygame.mixer.Sound(hover_sound) 
        self.click_sound = pygame.mixer.Sound(click_sound)
        self.change_text(text)
        self.update_surface()
        self.rect = pygame.Rect(self.x, self.y, *self.size)

    @abstractmethod
    def change_text(self, text):
        pass

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if self.click_sound:
                        self.click_sound.play()
                    return True
        return False

    def update_highlight(self, mouse_pos):
        previously_highlighted = self.highlighted
        self.highlighted = self.rect.collidepoint(mouse_pos)
        
        if self.highlighted and not previously_highlighted:
            if self.hover_sound:
                self.hover_sound.play()
        elif not self.highlighted and previously_highlighted:
            if self.hover_sound:
                self.hover_sound.stop()

        self.change_text(self.text_string)

    def update_surface(self):
        pass




