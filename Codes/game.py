import pygame as pg
import pygame.mixer_music

from Codes.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from Codes.Level import Level
from Codes.menu import Menu
from Codes.Entity import Entity


class Game:
    def __init__(self):
        pg.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
     while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                entity_objeto = Entity(self.window)
                level = Level(self.window, 'Level', menu_return,entity_objeto )
                level_return = level.run()
            elif menu_return == MENU_OPTION[1]:
                pygame.quit()
                quit()
            else:
                pass

