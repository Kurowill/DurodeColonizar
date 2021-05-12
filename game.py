import pygame
from random import randrange

from obj import Obj



class Game:

    def __init__(self):
        
        self.all_sprites = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.inimigos = pygame.sprite.Group()

        self.bg1 = Obj("assets/bg1.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/bg2.png", 500, 0, self.all_sprites)

        self.mudar_cenario = False


    def desenhar(self, tela):
        self.all_sprites.draw(tela)


    def HUD (self):
        pass


    def colisões(self):
        pass


    def update(self):
        self.all_sprites.update()
        self.HUD()
        self.colisões()