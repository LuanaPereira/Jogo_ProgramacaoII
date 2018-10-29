import pygame, sys
from pygame.locals import*


class Inimigo(pygame.sprite.Sprite): #cria a classe
    def __init__(self, cor, largura, altura, x, y):
        super().__init__()
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def mover(self, x, y):
        self.rect.x = x
        self.rect.y = y
