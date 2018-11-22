import pygame

class Bomba(pygame.sprite.Sprite):  # cria a classe
    def __init__(self, posicaoX, posicaoY):  # contrutor
        pygame.sprite.Sprite.__init__(self)  # chama o construtor da classe
        self.image = pygame.image.load('imagens/bala.png')  # coloca a imagem na classe

        self.rect = self.image.get_rect()  # cria a imagem
        self.velocidadeBomba = 5  # variavel velocidade comecando com 5
        self.rect.top = posicaoY  # posicao da bomba em y
        self.rect.left = posicaoX  # posicao da bomba em x

    def trajetoria(self):  # metodo para trajetoria da bomba
        self.rect.y -= self.velocidadeBomba  # bpmba vai percorrer o caminho dela mesmo menos a velociadade

    '''def colocar(self, superficie): #metodo para colocar a bomba na tela
        superficie.blit(self.ImagemBomba, self.rect) #posicao da bomba na tela
'''


