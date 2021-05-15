import pygame
from pygame.locals import *


class Obj(pygame.sprite.Sprite):

    def __init__(self, imagem, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
       

class Player(Obj):

    def __init__(self, imagem, x, y, *groups):

        super().__init__(imagem, x, y, *groups)

        self.vel = 4
        self.grav = 1

        self.mov_d = False
        self.mov_e = False
        self.pular = False

        self.ticks = 0
        self.img = 0

        self.colet = 0
        self.vidas = 3        


    def mover(self):
        if self.mov_d:
            self.rect[0] += 8          
            self.anim("assets/walk", 4, 3, False)
            if self.rect.right >= 450:
                self.rect.right = 450
        
        elif self.mov_e:
            self.rect[0] -= 8          
            self.anim("assets/walk", 4, 3, True)
            if self.rect.left <= 50:
                self.rect.left = 50

        else:
            self.anim("assets/idle", 4, 3)


    def atacar(self):
        pass


    def pular(self):
        pass

    def gravidade(self):


        self.vel += self.grav
        self.rect.y += self.vel


        if self.vel >= 10:
            self.vel = 10



    def eventos(self, evento):


        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                self.mov_d = True

            if evento.key == pygame.K_a:
                self.mov_e = True

            if evento.key == pygame.K_SPACE:
                self.pular = True


        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_d:
                self.mov_d = False

            if evento.key == pygame.K_a:
                self.mov_e = False


    def colisoes(self):
        pass


    def queda(self):

        if self.vidas > 0:
            if self.rect.y > 720:
                self.rect.x = 100
                self.rect.y = 250
                self.vidas -= 1        


    def anim(self, name, ticks, limit, flip=False):
        
        self.ticks += 1

        if self.ticks >= ticks:
            self.ticks = 0
            self.img += 1
        if self.img > limit:
            self.img = 0
        
        self.image = pygame.image.load("assets/"+ name + str(self.img) + ".png")
        if flip:
            self.image = pygame.transform.flip(self.image,True,False)
        else:
            self.image = pygame.transform.flip(self.image,False,False)
        


    def update(self):

        self.mover()
        self.atacar()
        self.queda()

class Inimigos(pygame.sprite.Sprite):

    def __init__(self, imagem, x, y, dinx, diny, flip= False, scale = 1, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(imagem)   
        self.rect = self.image.get_rect()
        self.dinx = dinx
        self.diny = diny
        self.scale = scale
        self.image = pygame.transform.scale(self.image, ((self.dinx*self.scale), (self.diny*self.scale))) 
        self.rect[0] = x
        self.rect[1] = y


        self.ticks = 0
        self.img = 0


    def anim(self, name, ticks, limit, flip=False):
        
        self.ticks += 1

        if self.ticks >= ticks:
            self.ticks = 0
            self.img += 1
            self.rect.x -= 15
        if self.img > limit:
            self.img = 0
            self.rect.x = 300
        
        self.image = pygame.image.load("assets/"+ name + str(self.img) + ".png")
        self.image = pygame.transform.scale(self.image, ((self.dinx*self.scale), (self.diny*self.scale))) 

        if flip:
            self.image = pygame.transform.flip(self.image,True,False)
        else:
            self.image = pygame.transform.flip(self.image,False,False)
