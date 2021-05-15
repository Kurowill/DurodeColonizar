import pygame
from random import randrange

from obj import *



class Game:

    def __init__(self):
        
        self.todos_sprites = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.inimigos = pygame.sprite.Group()

        self.bg1 = Obj("assets/bg1.png", 0, 0, self.todos_sprites)
        self.bg2 = Obj("assets/bg2.png", 500, 0, self.todos_sprites)

        self.jacare = Inimigos("assets/jacare/jacare0.png", 300, 420, 130, 40, False, 2, self.todos_sprites, self.inimigos)

        self.hero = Player("assets/assets/idle0.png", 0, 350, self.todos_sprites, self.player)

        self.mudar_cenario = False


    def mover_bg(self):

        if self.hero.rect.right >= 450 and self.hero.mov_d:
            self.bg1.rect.x -= 20
            self.bg2.rect.x -= 20
            if self.bg1.rect[0] <= -500:
                self.bg1.rect[0] = 500
            if self.bg2.rect[0] <= -500:
                self.bg2.rect[0] = 500

        elif self.hero.rect.left <= 50 and self.hero.mov_e:
            self.bg1.rect.x += 20
            self.bg2.rect.x += 20           
            if self.bg1.rect[0] <= 500:
                self.bg1.rect[0] = -500
            if self.bg2.rect[0] <= 500:
                self.bg2.rect[0] = -500


    def desenhar(self, tela):
        self.todos_sprites.draw(tela)


    def HUD (self):
        pass


    def colisões(self):
        pass


    def update(self):
        self.todos_sprites.update()
        self.hero.update()
        self.jacare.anim("jacare/jacare", 5, 8)
        self.mover_bg()
        self.HUD()
        self.colisões()