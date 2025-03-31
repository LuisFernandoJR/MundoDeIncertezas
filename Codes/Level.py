
import pygame
from pygame import Rect, Surface
from pygame.font import Font

from Codes.Const import TAMANHO_BASE, TAMANHO_BOLA, NUMERO_BLOCOS, NUMERO_LINHAS, C_WHITE, C_BLACK, C_RED, \
    WINDOW_HEIGHT, WINDOW_WIDTH, MOVIMENTO_BOLA, PONTUACAO, NUMERO_TOTAL_BLOCOS
from Codes.Entity import Entity



class Level:



    def __init__(self, window, name, menu_return, entity):
        self.window = window
        self.name = name
        self.menu_return = menu_return
        self.surf = pygame.image.load('./asset/LevelBg.png')
        self.react = self.surf.get_rect(left=0, top=0)
        self.entity = entity
        self.jogador = pygame.Rect(100, 700, TAMANHO_BASE, 15)
        self.bola = pygame.Rect(200, 500, TAMANHO_BOLA, TAMANHO_BOLA)

    def criar_blocos(self, numero_blocos, numero_linhas):
        altura_tela = WINDOW_HEIGHT
        largura_tela = WINDOW_WIDTH
        largura_bloco = largura_tela / 8 - 4
        altura_bloco = 12
        distancia_entre_linhas = altura_bloco + 5
        blocos = []
        for l in range(NUMERO_LINHAS):
            for i in range(NUMERO_BLOCOS):
                bloco = pygame.Rect(i * (largura_bloco + 4), l * distancia_entre_linhas, largura_bloco, altura_bloco)
                blocos.append(bloco)
        return blocos

    def desenhar_blocos (self, blocos):
        for bloco in blocos:
            pygame.draw.rect(self.window, C_RED,bloco)

    def mover_jogador(self):
        # Movimentação do jogador
        keys = pygame.key.get_pressed()  # Obtém o estado das teclas
        if keys[pygame.K_RIGHT]:
            if (self.jogador.x + TAMANHO_BASE) < WINDOW_WIDTH:
                self.jogador.x += 3
        if keys[pygame.K_LEFT]:
            if self.jogador.x >= 0:
                self.jogador.x -= 3

    def mover_bola(self, blocos):
        movimento = MOVIMENTO_BOLA
        self.bola.x = self.bola.x + movimento[0]
        self.bola.y = self.bola.y + movimento[1]

        if self.bola.x <= 0:
            movimento[0] = - movimento[0]
        if self.bola.y <= 0:
            movimento[1] = - movimento[1]
        if self.bola.x + TAMANHO_BOLA >= WINDOW_WIDTH:
            movimento[0] = - movimento[0]
        if self.bola.y + TAMANHO_BOLA >= WINDOW_HEIGHT:
            movimento = None
        if self.jogador.collidepoint(self.bola.x, self.bola.y):
            movimento[1] = - movimento[1]
        for bloco in blocos:
            if bloco.collidepoint(self.bola.x, self.bola.y):
                blocos.remove(bloco)
                movimento[1] = - movimento[1]
        return movimento


    def run (self,):
        blocos = self.criar_blocos(NUMERO_BLOCOS, NUMERO_LINHAS)

        while True:
            self.window.fill(C_BLACK)
            self.window.blit(source=self.surf, dest=self.react)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechando a Janela
                    quit()  # encerrando o pygame
            self.mover_jogador()
            self.mover_bola(blocos)
            self.desenhar_blocos(blocos)
            pygame.draw.rect(self.window, C_WHITE, self.jogador)
            pygame.draw.rect(self.window, C_BLACK, self.bola)
            if not self.mover_bola(blocos):
                pygame.quit()
                quit()
            pygame.time.wait(5)
            pygame.display.flip()






