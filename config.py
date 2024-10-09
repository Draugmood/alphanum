"""Config module for baby screen lock game"""
import os
import pygame

pygame.init()

# Colors
BLACK = pygame.Color(0, 0, 0)

BLUE = pygame.Color(0, 0, 104)
MAROON = pygame.Color(136, 0, 21)
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

COL_1 = pygame.Color(255, 0, 0)
COL_2 = pygame.Color(255, 127, 0)
COL_3 = pygame.Color(255, 255, 0)
COL_4 = pygame.Color(0, 255, 0)
COL_5 = pygame.Color(0, 255, 127)
COL_6 = pygame.Color(0, 255, 255)
COL_7 = pygame.Color(0, 0, 255)
COL_8 = pygame.Color(127, 0, 255)
COL_9 = pygame.Color(255, 0, 255)

# Globals
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_RECT = pygame.Rect(0, 0, SCREEN.width, SCREEN.height)
CLOCK = pygame.time.Clock()
SCREEN_NINTH = int(SCREEN_RECT.w/9)

BUTTON_DIM = (350, 150) # change to be relative to screen dims
MENU_BUTTON_FONT = pygame.font.Font(None, 50)


# Text rendering
def print_text(text, color, text_font, surface, pos):
    text = text_font.render(text, 1, color)
    text_pos = text.get_rect(center=pos)
    surface.blit(text, text_pos)

NORMAL_FONT = pygame.font.Font(None, 50)

# Images
def load_image(name):
    """Function for loading images from the 'resources' folder"""
    fullname = os.path.join("assets", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print("Cannot load image:", name)
        raise SystemExit(message)
    image = image.convert_alpha()

    return image

CLOSE_BTN = "close.png"
