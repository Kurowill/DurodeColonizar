import pygame
from obj import *

pygame.init()

tela = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

loop = True

player = Player("Jogo1Semestre/assets/teste/idle0.png", 100, 100)

while loop:
    clock.tick(30)

    player.update()
    pygame.display.update()


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop = False
        player.eventos(evento)    