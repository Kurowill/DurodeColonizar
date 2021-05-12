import pygame

class Obj(pygame.sprite.Sprite):
    def __init__(self, imagem, x, y, *groups):
        super().__init__(*groups)

        self.imagem = pygame.image.load(imagem)
        self.rect = self.imagem.get_rect()
        self.rect[0] = x
        self.rect[1] = y