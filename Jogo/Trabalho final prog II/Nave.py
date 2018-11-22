import random
from Bomba import Bomba
import pygame, sys

LARGURA = 600
ALTURA = 400


class Nave(pygame.sprite.Sprite):  # definindo a classe
    def __init__(self):  # metodo iniciador da classe
        pygame.sprite.Sprite.__init__(self)  # chama o construtor da classe
        self.image = pygame.image.load('imagens/nave.png')  # coloca a imagem na classe

        self.rect = self.image.get_rect()  # cria a imagem
        self.rect.centerx = LARGURA / 2  # posiciona a imagemn o centro x, centerx objeto criado
        self.rect.centery = ALTURA - 30  # posiciona a imagem no centro y

        self.listaDisparo = []  # atributo disparo da nave para contar os disparos
        self.__vida = True  # atributo vida da nave
        self.velocidade = 20  # velocidade da nave

    def vidaGet(self):
        return self.__vida

    def vidaSet(self, vida):
        self.__vida = vida
        
    def movimento(self):  # funcao para limitar o movimento da nave
        if self.vida == True:  # verifica se a nave ainda esta com vida
            if self.rect.left <= 0:  # verifica se esta na posicao 0
                self.rect.left = 0  # atualiza com a posicao 0
            elif self.rect.right > 600:  # verifica se esta na ultima posica
                self.rect.right = 600  # atualiza com a ultima posicao

    def disparar(self, x, y):  # passa as posicoes da bala
        bala = Bomba(x, y)  # cria uma bala que recebe a classe disparo
        self.listaDisparo.append(bala)
        return bala

    '''def colocar(self, tela): #passa a tela e o objeto imagem
        tela.blit(self.image, self.rect) #para colocar objetos na tela
        '''
