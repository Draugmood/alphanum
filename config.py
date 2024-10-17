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

COLORLIST = [WHITE,COL_1,COL_2,COL_3,COL_4,COL_5,COL_6,COL_7,COL_8,COL_9]

# Globals
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_RECT = pygame.Rect(0, 0, SCREEN.width, SCREEN.height)
CLOCK = pygame.time.Clock()
SCREEN_NINTH = int(SCREEN_RECT.w/9)

BUTTON_DIM = (350, 150) # change to be relative to screen dims
MENU_BUTTON_FONT = pygame.font.Font(None, 50)

AXIS_RATIO = 0.875      # 7/8 ratio

# Game content
LETTERS = {
    "A": pygame.K_a,
    "B": pygame.K_b,
    "C": pygame.K_c,
    "D": pygame.K_d,
    "E": pygame.K_e,
    "F": pygame.K_f,
    "G": pygame.K_g,
    "H": pygame.K_h,
    "I": pygame.K_i,
    "J": pygame.K_j,
    "K": pygame.K_k,
    "L": pygame.K_l,
    "M": pygame.K_m,
    "N": pygame.K_n,
    "O": pygame.K_o,
    "P": pygame.K_p,
    "Q": pygame.K_q,
    "R": pygame.K_r,
    "S": pygame.K_s,
    "T": pygame.K_t,
    "U": pygame.K_u,
    "V": pygame.K_v,
    "W": pygame.K_w,
    "X": pygame.K_x,
    "Y": pygame.K_y,
    "Z": pygame.K_z,
    "Æ": 230,
    "Ø": 248,
    "Å": 229
}

NUMBERS = {
    0: pygame.K_0,
    1: pygame.K_1,
    2: pygame.K_2,
    3: pygame.K_3,
    4: pygame.K_4,
    5: pygame.K_5,
    6: pygame.K_6,
    7: pygame.K_7,
    8: pygame.K_8,
    9: pygame.K_9
}

# Text rendering
def print_text(text, color, text_font, surface, pos):
    text = text_font.render(text, 1, color)
    text_pos = text.get_rect(center=pos)
    surface.blit(text, text_pos)

NORMAL_FONT = pygame.font.Font(None, 50)
TARGET_FONT = pygame.font.Font(None, 180)

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
