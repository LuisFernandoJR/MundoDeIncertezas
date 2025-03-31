import pygame

from Codes.Const import C_BLACK, C_WHITE, NUMERO_BLOCOS, NUMERO_LINHAS, WINDOW_WIDTH, WINDOW_HEIGHT, TAMANHO_BOLA, \
    TAMANHO_BASE


class Entity:




    #Funcao de desenhar a bola e a base do jogador
    def entidades(self,):
        pygame.draw.rect(self.window, C_WHITE, self.jogador)
        pygame.draw.rect(self.window, C_BLACK, self.bola)
        pass

    def __init__(self, window):
        self.window = window
        self.jogador = pygame.Rect(100, 700, TAMANHO_BASE, 15)
        self.bola = pygame.Rect(200, 500, TAMANHO_BOLA, TAMANHO_BOLA)


    def move (self, ):
        pass


