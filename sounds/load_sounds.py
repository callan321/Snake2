import pygame 

def load_sounds():
    return {
        'hover': pygame.mixer.Sound('sounds/hover.wav'),
        'click': pygame.mixer.Sound('sounds/play.wav'),
        # Add more sounds as needed
    }