import pygame

from game import Game
from menu import Menu

class Main:

    def __init__(self, tamx, tamy, titulo, favicon):
        
        pygame.init()
        pygame

        self.tela = pygame.display.set_mode([tamx, tamy])
        self.titulo = pygame.display.set_caption(titulo)
        self.favicon = pygame.image.load(favicon)
        self.icone = pygame.display.set_icon(self.favicon)

        self.loop = True
        self.fps = pygame.time.Clock()
        
        self.game = Game()
        self.menu = Menu()


    def desenhar(self):
        if not self.menu.mudar_cenario:
            self.menu.desenhar(self.tela)

        elif not self.game.mudar_cenario:
            self.game.desenhar(self.tela)
            
        else:
            self.loop = False

    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.loop = False


    def update(self):
        while loop:
            self.desenhar()
            self.eventos()
            self.fps.tick(30)
            self.game.update()
            pygame.display.update()

Largura = 800
Altura = 600


Main = Main(Largura, Altura, "Duro de Colonizar", "assets/")