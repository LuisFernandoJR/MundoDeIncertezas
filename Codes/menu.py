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
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu2.mp3')
        pygame.mixer_music.play(-1)
        pygame.display.set_caption("Quebrando a Nostalgia")
        while True:
            self.window.blit(source=self.surf, dest=self.react)
            self.menu_text(text_size=70, text='Quebrando', text_color=(C_WHITE),
                           text_center_pos=(WINDOW_WIDTH / 2, 70))
            self.menu_text(text_size=70, text='a', text_color=(C_WHITE),
                           text_center_pos=(WINDOW_WIDTH / 2, 120))
            self.menu_text(text_size=70, text='Nostalgia', text_color=(C_WHITE),
                           text_center_pos=(WINDOW_WIDTH / 2, 170))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                 self.menu_text(50, MENU_OPTION[i], C_PURPLE,
                               (WINDOW_WIDTH / 2, 400 + 50 * i))
                else:
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]
    #Fonte
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



