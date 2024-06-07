import pygame
from abc import ABC, abstractmethod
from config.config import GameConfig

class Button(ABC):
    def __init__(self, config: GameConfig):
        self.config = config
        self.highlighted = False
        self.hover_sound = pygame.mixer.Sound(config.HOVER_SOUND)
        self.click_sound = pygame.mixer.Sound(config.CLICK_SOUND)
        self.rect = pygame.Rect(0, 0, 0, 0)  # Initial rect with zero size
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA)  # Initialize surface with zero size

    @abstractmethod
    def change_text(self, text: str) -> None:
        pass

    def show(self, screen: pygame.Surface) -> None:
        screen.blit(self.surface, self.rect.topleft)

    def click(self, event: pygame.event.Event) -> bool:
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                if self.click_sound:
                    self.click_sound.play()
                return True
        return False

    def update_highlight(self, mouse_pos: tuple[int, int]) -> None:
        previously_highlighted = self.highlighted
        self.highlighted = self.rect.collidepoint(mouse_pos)

        if self.highlighted and not previously_highlighted:
            if self.hover_sound:
                self.hover_sound.play()
        elif not self.highlighted and previously_highlighted:
            if self.hover_sound:
                self.hover_sound.stop()

        self.change_text(self.text_string)

    @abstractmethod
    def update(self, new_pos: tuple[int, int]) -> None:
        pass


class A:
    def __init__(self):
        pass 

class B:
    def __init__(self, a):
        self.z = a
        self.c = C(a)
class C:
    def __init__(self, a):
        self.z = a 
    
a = A()
b = B(a)