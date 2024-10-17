import pygame
import config as cf

from enum import Enum, auto


class Button:
    """Button object for navigating the menus"""
    def __init__(self, txt, y_pos, func, args):
        self.txt = txt
        self.dimensions = cf.BUTTON_DIM
        self.pos = (cf.SCREEN_RECT.centerx, y_pos)
        self.rect = pygame.Rect((self.pos), (self.dimensions))
        self.rect.center = self.rect.topleft
        self.func = func
        self.color = cf.MAROON
        self.args = args

    def draw(self):
        """Draws the button on the screen, and prints text on top"""
        pygame.draw.rect(cf.SCREEN, self.color, self.rect)
        if pygame.font:
            cf.print_text(self.txt, cf.WHITE, cf.MENU_BUTTON_FONT, cf.SCREEN, self.pos)

    def hover(self):
        """Buttons change color when targeted"""
        self.color = cf.BLUE
        self.draw()
        self.color = cf.MAROON

    def call_func(self): # surely there are cleaner solutions than this but it is what it is
        """Executes a buttons function"""
        if self.func:
            self.func(*self.args)
