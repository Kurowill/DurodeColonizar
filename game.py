import pygame
from random import randrange

from obj import *



class Game:

    def __init__(self):
        
        self.todos_sprites = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.inimigos = pygame.sprite.Group()

        self.bg = Obj("assets/bg.png", 0, 0, self.todos_sprites)

        self.qtpiso = 2
        self.piso1 = []
        for i in range(self.qtpiso):
            piso = Obj("assets/chao.png", 698*i, 638, self.todos_sprites, self.plataformas)
            self.piso1.append(piso)

        self.agua = Obj("assets/agua.png", 698*2, 638, self.todos_sprites)

        self.plat1 = Obj("assets/plat1.png", 698*2, 518, self.todos_sprites, self.plataformas)

        self.piso2 = []
        for i in range(self.qtpiso):
            piso = Obj("assets/chao.png", self.agua.rect.right+(698*i), 638, self.todos_sprites, self.plataformas)
            self.piso2.append(piso)

        self.nuvem = []
        for i in range(4):
            nuvem = Obj("assets/nuvem.png", randrange(0,700,300), randrange(0,200,40), self.todos_sprites)
            self.nuvem.append(nuvem)


        self.jacare = Inimigos("assets/jacare/jacare0.png", 300, 598, 130, 40, False, 2, self.todos_sprites, self.inimigos)

        self.hero = Player("assets/indio/andar4.png", 0, 638-84, 25, 42, False, 2, self.todos_sprites, self.player)

        self.mudar_cenario = False


    def mover_bg(self):

        if self.hero.rect.right >= 450 and self.hero.mov_d:
            self.bg.rect.x -= 5
            if self.bg.rect.x <= -7000:
                self.bg.rect.x = -7000


        elif self.hero.rect.left <= 50 and self.hero.mov_e:
            self.bg.rect.x += 5
        
            if self.bg.rect.x >= 0:
                self.bg.rect.x = 0


    def mover_piso(self):

        
        if self.hero.rect.right >= 450 and self.hero.mov_d:
            
            for i in range(self.qtpiso):
                self.piso1[i].rect.x -= 10
                self.piso2[i].rect.x -= 10
            
            self.agua.rect.x -= 10
            self.plat1.rect.x -= 10
            
            if self.piso1[i].rect.x <= -7000:
                self.piso1[i].rect.x = -7000


        elif self.hero.rect.left <= 50 and self.hero.mov_e:
            for i in range(self.qtpiso):
                self.piso1[i].rect.x += 10
                self.piso2[i].rect.x += 10
            
                if self.piso1[0].rect.x >= 0:
                    self.piso1[i].rect.x = 698*i
                    self.piso2[i].rect.x = self.agua.rect.right+(698*i)

            self.agua.rect.x += 10
            self.plat1.rect.x += 10
            if self.piso1[0].rect.x >= 0:
                self.agua.rect.x = 698*2
                self.plat1.rect.x = 698*2           


    def mover_nuvem(self):
        
        for i in range(4):
  
            self.nuvem[i].ticks += 10

            if self.nuvem[i].rect.x < -200:
                self.nuvem[i].rect.x = randrange(700, 900, 100)
                self.nuvem[i].rect.y = randrange(0, 300, 50)
                
            if self.nuvem[i].ticks >= 10:
                self.nuvem[i].ticks = 0
                self.nuvem[i].rect.x -= 1

            


    def desenhar(self, tela):
        self.todos_sprites.draw(tela)


    def HUD (self):
        pass


    def colisões(self):
        pass


    def update(self, tela):
        self.todos_sprites.update(tela)
        self.hero.update(tela)
        self.jacare.anim("jacare/jacare", 5, 8)
        self.mover_bg()
        self.mover_piso()
        self.mover_nuvem()
        self.HUD()
        self.hero.colisões(self.plataformas,False, "Plataforma")
        self.hero.colisões(self.inimigos, False, "inimigo")