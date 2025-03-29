from math import trunc

import pygame.image
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Codes.Const import WINDOW_WIDTH, C_WHITE, C_PURPLE, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.react = self.surf.get_rect(left=0, top=0)

    def run(self):

        pygame.mixer_music.load('./asset/Menu2.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.react)
            self.menu_text(text_size=70, text='Mundo', text_color=(C_WHITE),
                           text_center_pos=(WINDOW_WIDTH / 2, 70))
            self.menu_text(text_size=70, text='de', text_color=(C_WHITE),
                           text_center_pos=(WINDOW_WIDTH / 2, 120))
            self.menu_text(text_size=70, text='Incertezas', text_color=(C_WHITE),
                           text_center_pos=(WINDOW_WIDTH / 2, 170))

            for i in range(len(MENU_OPTION)):
                self.menu_text(50, MENU_OPTION[i], C_WHITE,
                               (WINDOW_WIDTH / 2, 400 + 50 * i))
            self.menu_text(text_size=20, text='Luis Fernando dos Santos Junior, Ra:4637844', text_color=(C_WHITE),
                           text_center_pos=(150, 750))

            pygame.display.flip()
            # Chegando os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechando a Janela
                    quit()  # encerrando o pygame
    #Fonte
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



