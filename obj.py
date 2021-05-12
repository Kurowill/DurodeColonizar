import pygame

class Obj(pygame.sprite.Sprite):
    def __init__(self, imagem, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        