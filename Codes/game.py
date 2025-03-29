import pygame as pg
import pygame.mixer_music

from Codes.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from Codes.menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
     while True:
            menu = Menu(self.window)
            menu.run()
            pass

