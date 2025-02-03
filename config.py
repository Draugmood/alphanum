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

COLORLIST = [WHITE, COL_1, COL_2, COL_3,
             COL_4, COL_5, COL_6, COL_7, COL_8, COL_9]

# Globals
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_RECT = pygame.Rect(0, 0, SCREEN.width, SCREEN.height)
CLOCK = pygame.time.Clock()
SCREEN_NINTH = int(SCREEN_RECT.w/9)

BUTTON_DIM = (350, 150)  # change to be relative to screen dims
MENU_BUTTON_FONT = pygame.font.Font(None, 50)

AXIS_RATIO = 0.875      # 7/8 ratio

# Game content
LETTERS = {
    "A a": pygame.K_a,
    "B b": pygame.K_b,
    "C c": pygame.K_c,
    "D d": pygame.K_d,
    "E e": pygame.K_e,
    "F f": pygame.K_f,
    "G g": pygame.K_g,
    "H h": pygame.K_h,
    "I i": pygame.K_i,
    "J j": pygame.K_j,
    "K k": pygame.K_k,
    "L l": pygame.K_l,
    "M m": pygame.K_m,
    "N n": pygame.K_n,
    "O o": pygame.K_o,
    "P p": pygame.K_p,
    "Q q": pygame.K_q,
    "R r": pygame.K_r,
    "S s": pygame.K_s,
    "T t": pygame.K_t,
    "U u": pygame.K_u,
    "V v": pygame.K_v,
    "W w": pygame.K_w,
    "X x": pygame.K_x,
    "Y y": pygame.K_y,
    "Z z": pygame.K_z,
    "Æ æ": 230,
    "Ø ø": 248,
    "Å å": 229
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


def print_text(text, color, text_font, surface, pos, align="center"):
    rendered_text = text_font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=pos)
    match align:
        case "center":
            text_rect.center = pos
        case "topright":
            text_rect.topright = pos
        case "topleft":
            text_rect.topleft = pos
    surface.blit(rendered_text, text_rect)


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
