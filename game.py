import pygame
from random import randrange

from obj import Obj



class Game:

    def __init__(self):
        
        self.todos_sprites = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.inimigos = pygame.sprite.Group()

        self.bg1 = Obj("imagem", 0, 0, self.todos_sprites)
        self.bg2 = Obj("imagem", 0, 0, self.todos_sprites)

        self.mudar_cenario = False


    def desenhar(self, tela):
        self.todos_sprites.draw(tela)


    def HUD (self):
        pass


    def colisões(self):
        pass


    def update(self):
        self.todos_sprites.update()
        self.HUD()
        self.colisões()