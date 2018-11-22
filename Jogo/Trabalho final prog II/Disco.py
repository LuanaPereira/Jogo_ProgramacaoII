import pygame

class Disco(pygame.sprite.Sprite):  # definindo a classe
    def __init__(self, x, y):  # metodo iniciador da classe
        pygame.sprite.Sprite.__init__(self)  # chama o construtor da classe
        self.image = pygame.image.load('imagens/disco.png')  # coloca a imagem na classe
        self.rect = self.image.get_rect()  # cria a imagem
        self.rect.x = x
        self.rect.y = y
