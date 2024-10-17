import random
import sys

import pygame

import config as cf
import particle
from button import Button
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
        self.dt = 0
        self.playtime = 0
        self.current_state = GameState.GAME_SELECT
        self.menu_chooser = 0
        self.game_type = None
        self.visibility = 1
        self.particles = []
        self.background = pygame.Surface(cf.SCREEN.get_size()).convert()
        self.background.fill(cf.BLACK)
        self.group = pygame.sprite.Group()
        self.round_started = False
        self.target = None
        self.correct_key = None

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
            self.dt = self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def update(self):
        cf.SCREEN.blit(self.background, (0, 0))
        if self.current_state == GameState.PLAYING:
            self.playtime += self.dt
            if self.playtime > 4000:
                self.round_started = True
                self.play_round()
            particle.update(self.particles)

        else: # updates for other game states
            pass

    def draw(self):
        if not self.current_state == GameState.PLAYING:
            buttons = self.get_current_menu_buttons()
            for button in buttons:
                button.draw()
            self.hovered_button().hover()

        if 4000 > self.playtime > 1000:
            cf.print_text(str(4-(self.playtime // 1000)),
                          cf.WHITE,
                          cf.NORMAL_FONT,
                          cf.SCREEN,
                          cf.SCREEN_RECT.center)

        if self.round_started:
            instruction_text = "TRYKK PÅ"
            if self.game_type == GameType.LETTERS:
                instruction_text += " BOKSTAVEN..."
            if self.game_type == GameType.NUMBERS:
                instruction_text += " TALLET..."
            cf.print_text(instruction_text,
                          cf.WHITE,
                          cf.NORMAL_FONT,
                          cf.SCREEN,
                          (cf.SCREEN_RECT.centerx,
                           cf.SCREEN_RECT.centery-100))

        if self.target and self.playtime > 6000:
            cf.print_text(str(self.target),
                          cf.WHITE,
                          cf.TARGET_FONT,
                          cf.SCREEN,
                          (cf.SCREEN_RECT.centerx,
                           cf.SCREEN_RECT.centery+100))

        particle.draw(self.particles)
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
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == self.correct_key:
                    particle.spawn_many_colors(20, self.particles)
                if event.key == pygame.K_SPACE:
                    particle.spawn_many_colors(20, self.particles)
                else:
                    pass # handle mistake case

    def play_round(self):
        if not self.target:
            if self.game_type == GameType.LETTERS:
                self.target, self.correct_key = (
                    random.choice(list(cf.LETTERS.items()))
                )
            if self.game_type == GameType.NUMBERS:
                self.target, self.correct_key = (
                    random.choice(list(cf.NUMBERS.items()))
                )

    def get_current_menu_buttons(self):
        if self.current_state == GameState.GAME_SELECT:
            return self.game_select_buttons
        if self.current_state == GameState.VISIBILITY_SELECT:
            return self.visibility_select_buttons
        return []
    
    def hovered_button(self):
        active_buttons = self.get_current_menu_buttons()
        return active_buttons[self.menu_chooser%len(active_buttons)]


if __name__ == "__main__":
    game = Game()
    game.run()
