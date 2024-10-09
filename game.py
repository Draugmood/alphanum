import sys
import random
import pygame
import config as cf

from button import Button, ButtonType
from enum import Enum, auto

class GameState(Enum):
    GAME_SELECT = auto()
    VISIBILITY_SELECT = auto()
    PLAYING = auto()
    EXIT = auto()

class GameType(Enum):
    NUMBERS = auto()
    LETTERS = auto()



class Game:
    def __init__(self):
        self.clock = cf.CLOCK
        self.current_state = GameState.GAME_SELECT
        self.menu_chooser = 0
        self.game_type = None
        self.visibility = 1
        self.particles = []
        self.background = pygame.Surface(cf.SCREEN.get_size()).convert()
        self.background.fill(cf.BLACK)
        self.group = pygame.sprite.Group()
        self.game_select_buttons = [
            Button("BOKSTAVER", 300, self.set_game_type, args=(GameType.LETTERS,)),
            Button("TALL", 500, self.set_game_type, args=(GameType.NUMBERS,))
        ]

        self.visibility_select_buttons = [
            Button("SYNLIG", 200, self.set_visibility, args=(1,)),
            Button("SKJULT", 400, self.set_visibility, args=(0,)),
            Button("TILBAKE", 600, self.reset_menu, args=())
        ]
        

    def set_game_type(self, game_type):
        self.game_type = game_type
        self.menu_chooser = 0
        self.current_state = GameState.VISIBILITY_SELECT

    def set_visibility(self, visibility):
        self.visibility = visibility
        self.menu_chooser = 0
        self.current_state = GameState.PLAYING

    def reset_menu(self):
        self.visibility = 1
        self.game_type = None
        self.menu_chooser = 0
        self.current_state = GameState.GAME_SELECT

    def run(self):
        while self.current_state != GameState.EXIT:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def update(self):
        cf.SCREEN.blit(self.background, (0, 0))
        if self.current_state == GameState.PLAYING:
            handle_particles(self.particles)
        else: # updates for other game states
            pass

    def draw(self):
        if not self.current_state == GameState.PLAYING:
            buttons = self.get_current_menu_buttons()
            for button in buttons:
                button.draw()
            self.hovered_button().hover()
        self.group.draw(cf.SCREEN)
        pygame.display.flip()

    def handle_events(self):
        match self.current_state:
            case GameState.GAME_SELECT:
                self.handle_menu_events()
            case GameState.VISIBILITY_SELECT:
                self.handle_menu_events()
            case GameState.PLAYING:
                self.handle_game_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    case pygame.K_UP:
                        self.menu_chooser -= 1
                    case pygame.K_DOWN:
                        self.menu_chooser += 1
                    case pygame.K_SPACE:
                        self.hovered_button().call_func()

    def handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if (event.key == pygame.K_LSHIFT
                   or event.key == pygame.K_LESS
                   or event.key == pygame.K_LCTRL
                   or event.key == pygame.K_CAPSLOCK
                   or event.key == pygame.K_a
                   or event.key == pygame.K_TAB
                   or event.key == pygame.K_q
                   or event.key == 124
                   or event.key == pygame.K_1
                   or event.key == pygame.K_F1):
                    spawn_colors(20, self.particles, 1, cf.COL_1)
                if (event.key == pygame.K_z
                   or event.key == pygame.K_x
                   or event.key == pygame.K_LMETA
                   or event.key == pygame.K_LALT
                   or event.key == pygame.K_s
                   or event.key == pygame.K_d
                   or event.key == pygame.K_w
                   or event.key == pygame.K_e
                   or event.key == pygame.K_2
                   or event.key == pygame.K_3
                   or event.key == pygame.K_F2
                   or event.key == pygame.K_F3):
                    spawn_colors(20, self.particles, 2, cf.COL_2)
                if (event.key == pygame.K_c
                   or event.key == pygame.K_v
                   or event.key == pygame.K_f
                   or event.key == pygame.K_g
                   or event.key == pygame.K_r
                   or event.key == pygame.K_t
                   or event.key == pygame.K_4
                   or event.key == pygame.K_5
                   or event.key == pygame.K_F4
                   or event.key == pygame.K_F5
                   or event.key == pygame.K_F6):
                   spawn_colors(20, self.particles, 3, cf.COL_3)
                if (event.key == pygame.K_b
                   or event.key == pygame.K_n
                   or event.key == pygame.K_h
                   or event.key == pygame.K_j
                   or event.key == pygame.K_y
                   or event.key == pygame.K_u
                   or event.key == pygame.K_6
                   or event.key == pygame.K_7
                   or event.key == pygame.K_F7
                   or event.key == pygame.K_F8):
                   spawn_colors(20, self.particles, 4, cf.COL_4)
                if (event.key == pygame.K_m
                   or event.key == pygame.K_COMMA
                   or event.key == pygame.K_RALT
                   or event.key == pygame.K_k
                   or event.key == pygame.K_l
                   or event.key == pygame.K_i
                   or event.key == pygame.K_o
                   or event.key == pygame.K_8
                   or event.key == pygame.K_9
                   or event.key == pygame.K_F9
                   or event.key == pygame.K_F10):
                   spawn_colors(20, self.particles, 5, cf.COL_5)
                if (event.key == pygame.K_PERIOD
                   or event.key == pygame.K_MINUS
                   or event.key == pygame.K_MENU
                   or event.key == pygame.K_RCTRL
                   or event.key == 248
                   or event.key == 230
                   or event.key == pygame.K_p
                   or event.key == 229
                   or event.key == pygame.K_0
                   or event.key == pygame.K_PLUS
                   or event.key == pygame.K_F11
                   or event.key == pygame.K_F12):
                   spawn_colors(20, self.particles, 6, cf.COL_6)
                if (event.key == pygame.K_RSHIFT
                   or event.key == pygame.K_UP
                   or event.key == pygame.K_LEFT
                   or event.key == pygame.K_DOWN
                   or event.key == pygame.K_QUOTE
                   or event.key == pygame.K_RETURN
                   or event.key == 1073741824
                   or event.key == pygame.K_BACKSLASH
                   or event.key == pygame.K_BACKSPACE
                   or event.key == pygame.K_INSERT
                   or event.key == pygame.K_DELETE):
                   spawn_colors(20, self.particles, 7, cf.COL_7)
                if (event.key == pygame.K_KP1
                   or event.key == pygame.K_KP2
                   or event.key == pygame.K_RIGHT
                   or event.key == pygame.K_KP0
                   or event.key == pygame.K_KP4
                   or event.key == pygame.K_KP5
                   or event.key == pygame.K_KP7
                   or event.key == pygame.K_KP8
                   or event.key == pygame.K_NUMLOCK
                   or event.key == pygame.K_KP_DIVIDE
                   or event.key == pygame.K_HOME
                   or event.key == pygame.K_END):
                   spawn_colors(20, self.particles, 8, cf.COL_8)
                if (event.key == pygame.K_KP3
                   or event.key == pygame.K_KP_ENTER
                   or event.key == pygame.K_KP_PERIOD
                   or event.key == pygame.K_KP6
                   or event.key == pygame.K_KP_PLUS
                   or event.key == pygame.K_KP9
                   or event.key == pygame.K_KP_MULTIPLY
                   or event.key == pygame.K_KP_MINUS
                   or event.key == pygame.K_PAGEUP
                   or event.key == pygame.K_PAGEDOWN):
                   spawn_colors(20, self.particles, 9, cf.COL_9)

    def get_current_menu_buttons(self):
        if self.current_state == GameState.GAME_SELECT:
            return self.game_select_buttons
        if self.current_state == GameState.VISIBILITY_SELECT:
            return self.visibility_select_buttons
        return []
    
    def hovered_button(self):
        active_buttons = self.get_current_menu_buttons()
        return active_buttons[self.menu_chooser%len(active_buttons)]


def handle_particles(all_ptcl):
    for particle in all_ptcl:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        pygame.draw.circle(cf.SCREEN,
                       particle[3],
                       (int(particle[0][0]), int(particle[0][1])),
                       int(particle[2]))
        if particle[2] <= 0:
            all_ptcl.remove(particle)


def spawn_colors(num_part, part_list, pos, col):
    for _ in range(num_part):
        x_pos = cf.SCREEN_NINTH*pos-(cf.SCREEN_NINTH/2) + random.randint(-40, 40)
        y_pos = cf.SCREEN_RECT.h-15
        x_vel = random.randint(0, 20)/10 - 1
        y_vel = -random.randint(2, 7)
        size = random.randint(4, 20)

        part_list.append([[x_pos, y_pos],
                          [x_vel, y_vel],
                          size,
                          col])


if __name__ == "__main__":
    game = Game()
    game.run()
