import pygame
from obj import Obj

class Menu:

    def __init__(self):
        self.todos_sprites = pygame.sprite.Group()

        self.bg = Obj("imagem", 0, 0, self.todos_sprites)
        self.bg2 = Obj("imagem", 360, 0, self.todos_sprites)

        self.ground = Obj("imagem", 0, 480, self.todos_sprites)
        self.ground2 = Obj("imagem", 360, 480, self.todos_sprites)

        self.get_ready = Obj("imagem", 60, 100, self.todos_sprites)
        self.table_score = Obj("imagem", 20, 200, self.todos_sprites)
        self.button_go = Obj("imagem", 100, 420, self.todos_sprites)

        self.mudar_cenario = False

        self.text_score = Text(100, "0")
        

    def draw(self, tela):
        self.todos_sprites.draw(tela)
        self.text_score.draw(tela, 160, 250)

    def update(self, pts):
        self.todos_sprites.update()
        self.move_bg()
        self.move_ground()
        self.text_score.text_update(pts)

    def events(self, event):

        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_go.rect.collidepoint(pygame.mouse.get_pos()):
                self.change_scene = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.change_scene = True


    def move_bg(self):
        self.bg.rect[0] -= 1
        self.bg2.rect[0] -= 1

        if self.bg.rect[0] <= -360:
            self.bg.rect[0] = 0
        if self.bg2.rect[0] <= 0:
            self.bg2.rect[0] = 360


    def move_ground(self):
        self.ground.rect[0] -= 3
        self.ground2.rect[0] -= 3

        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 0
        if self.ground2.rect[0] <= 0:
            self.ground2.rect[0] = 360