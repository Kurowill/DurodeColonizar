import pygame
from pygame.locals import *


class Obj(pygame.sprite.Sprite):

    def __init__(self, imagem, x, y, *groups,  escala = 1, dinx=None, diny=None):
        super().__init__(*groups)

        self.image = pygame.image.load(imagem)
        if escala != 1:
            self.image = pygame.transform.scale(self.image,(dinx*escala, diny*escala))
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        self.ticks = 0
       

class Player(pygame.sprite.Sprite):

    def __init__(self, imagem, x, y, dinx, diny, flip= False, scale = 1, *groups):
        super().__init__(*groups)

        self.dinx = dinx
        self.diny = diny
        self.scale = scale
        self.image = pygame.image.load(imagem) 
        self.image = pygame.transform.scale(self.image, ((self.dinx*self.scale), (self.diny*self.scale)))  
        self.rect = self.image.get_rect() 
        self.rect[0] = x
        self.rect[1] = y
        self.ticks = 0
        self.ticks2 = 0

        self.grupos = groups

        self.vel = 4
        self.grav = 1

        self.mov_d = False
        self.mov_e = False
        self.ataque = False
        self.mover_f = False

        self.img = 0

        self.colet = 0
        self.vidas = 3        

    def gravidade(self):
        self.vel += self.grav
        self.rect[1] += self.vel

        if self.vel >= 5:
            self.vel = 5

    def mover(self):
        if self.mov_d:
            self.rect[0] += 8          
            self.anim("indio/andar", 4, 4, False)
            self.image = pygame.transform.scale(self.image,(25*2, 42*2))
            if self.rect.right >= 450:
                self.rect.right = 450
            self.ticks2 = 0
        
        elif self.mov_e:
            self.rect[0] -= 8          
            self.anim("indio/andar", 4, 4, True)
            self.image = pygame.transform.scale(self.image,(25*2, 42*2))
            if self.rect.left <= 50:
                self.rect.left = 50
            self.ticks2 = 0

        else:
            self.ticks2 += 1
            if self.ticks2 > 240:        
                self.anim("indio/idle", 20, 7, False)
                self.image = pygame.transform.scale(self.image,(25*2, 42*2))


    def atacar(self, tela):

        if self.ataque and not self.mover_f:
            for i in range(30):
                self.anim("indio/atacar", 10, 3, False)
                self.image = pygame.transform.scale(self.image,(40*2, 42*2))
                self.grupos[0].draw(tela)
                pygame.display.update()
            self.flecha = Obj("assets/indio/flecha.png", self.rect.x+58, self.rect.y+29, self.grupos, escala=2, dinx=25, diny=5)
            self.ataque = False
            self.mover_f = True
            self.ticks2 = 0
            self.image = pygame.image.load("assets/indio/andar0.png")
            self.image = pygame.transform.scale(self.image,(25*2, 42*2))

        if self.mover_f:
            self.flecha.ticks += 0.25
            self.flecha.rect.x += 5
            self.flecha.rect.y += int(self.flecha.ticks)
            if self.flecha.rect.x > 700:
                self.flecha.kill()
                self.mover_f = False


            
    def eventos(self, evento):


        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                self.mov_d = True

            if evento.key == pygame.K_a:
                self.mov_e = True

            if evento.key == pygame.K_SPACE:
                self.vel *= -4

            if evento.key == pygame.K_RETURN:
                self.ataque = True


        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_d:
                self.mov_d = False

            if evento.key == pygame.K_a:
                self.mov_e = False




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


    def colisões(self, group, kill, name=None):

        col1 = pygame.sprite.spritecollide(self, group, kill)

        if col1 and name == "Plataforma":
            if self.rect.y + 38 < col1[0].rect.top:
                if self.rect.left <= col1[0].rect.right:
                    if self.rect.right - 4 >= col1[0].rect.left:
                        self.rect.bottom = col1[0].rect.top+3 

        if col1 and name == "colecionavel":
            self.colections += 1

        if col1 and name == "inimigo":
            if self.rect.y + 90 <= col1[0].rect.top:
                self.vel *= -1
                col1[0].kill()
            else: 
                self.vel *= -1
                self.vidas -= 1
                col1[0].kill()

        if self.mover_f:
            col2 = pygame.sprite.spritecollide(self.flecha, group, kill, pygame.sprite.collide_mask)

            if col2 and name == "inimigo":
                col2[0].kill() 
                self.flecha.kill()
                self.mover_f = False

            if col2 and name == "Plataforma":
                self.ticks = 0
                self.ticks += 1
                self.flecha.rect.y += 0
                self.flecha.rect.y += 0

                self.flecha.kill()
                self.mover_f = False



    def update(self, tela):

        self.gravidade()
        self.mover()
        self.atacar(tela)
        self.queda()

class Inimigos(pygame.sprite.Sprite):

    def __init__(self, imagem, x, y, dinx, diny, flip= False, scale = 1, *groups):
        super().__init__(*groups)

        self.dinx = dinx
        self.diny = diny
        self.scale = scale
        self.image = pygame.image.load(imagem) 
        self.image = pygame.transform.scale(self.image, ((self.dinx*self.scale), (self.diny*self.scale)))  
        self.rect = self.image.get_rect() 
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


