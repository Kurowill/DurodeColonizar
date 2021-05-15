import pygame
from pygame.locals import *

from game import Game
from menu import Menu

class Main:

    def __init__(self, tamx, tamy, titulo, favicon):
        
        pygame.init()

        self.tela = pygame.display.set_mode([tamx, tamy])
        self.titulo = pygame.display.set_caption(titulo)
        self.favicon = pygame.image.load(favicon)
        self.icone = pygame.display.set_icon(self.favicon)

        self.loop = True
        self.fps = pygame.time.Clock()
        
        self.game = Game()
        self.menu = Menu()


    def desenhar(self):

#        if not self.menu.mudar_cenario:
#            self.menu.desenhar(self.tela)

        if not self.game.mudar_cenario:
            self.game.desenhar(self.tela)

        else:
            self.loop = False

    def eventos(self):

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.loop = False
            self.game.hero.eventos(evento)


    def update(self):

        while self.loop:
            self.desenhar()
            self.eventos()
            self.fps.tick(30)
            if not self.menu.mudar_cenario:
                self.menu.update()
            if not self.game.mudar_cenario:
                self.game.update()
            pygame.display.update()

Largura = 500
Altura = 500


Main = Main(Largura, Altura, "Duro de Colonizar", "assets/favicon.ico")

Main.update()