import random 
import pygame, sys
from pygame.locals import*
from Disparo import Disparo
from Nave import Nave
from Inimigo import Inimigo

LARGURA = 600
ALTURA = 400
AMARELO = (255, 255,0)

pygame.font.init()
fonte = pygame.font.SysFont('calibri', 30)
def invasao():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))#criando a tela
    pygame.display.set_caption("Invasão") #titulo da tela

    jogador = Nave() #instancia do objeto nave
    ImagemFundo = pygame.image.load('image/espaço.jpg') #criando tela com a imagem do arquivo (instancia)
    jogando = True #jogador()nave comeca com true
    bomba = Disparo(LARGURA / 2, ALTURA - 70) #instancia a bomba

  
    grupo_inimigos = pygame.sprite.Group()  #blocos amarelos
    todos_inimigos = pygame.sprite.Group()  #todos blocos
    
    for i in range(20):
        x = random.randrange(LARGURA )
        y = random.randrange(ALTURA / 2)
        inimigo = Inimigo (AMARELO, 40, 20, x, y)
        grupo_inimigos.add(inimigo)
        todos_inimigos.add(grupo_inimigos)

    while True:
        
        jogador.movimento()
        bomba.trajetoria()
        
        for evento in pygame.event.get(): #verifica se tem algum evento acontecendo
            if evento.type == QUIT: #se o evento for sair 
                pygame.quit()#comando sair
                sys.exit()#garante que toda a aplicacao finalize
            if evento.type == pygame.KEYDOWN: #verifica se o evento foi feito a partir do teclado
                if evento.key == K_LEFT: #verifica se é o botaao esquerda que foi precionado                
                    jogador.rect.left -= jogador.velocidade #muda a posicao da nave para esquerda
                if evento.key == K_RIGHT:#verifica se o botao precionado foi a seta para direita
                    jogador.rect.right += jogador.velocidade #muda a posicao para a direita 
                if evento.key == K_SPACE: #verfica se a tecla precionada é o espaco
                    x,y = jogador.rect.center # variaveis que recebe a posicao do jogador
                    jogador.disparar(x,y)#chama a funcao disparar epassa a mesma posicao do jogador 


            if bomba.rect.colliderect(inimigo.rect):
                if todos_inimigos > 0:
                    todos_inimigos.remove() 
        
        
        tela.blit(ImagemFundo, (0,0)) #coloca a imagem de fundo na tela
        bomba.colocar(tela)#coloca a bomba na tela
        jogador.colocar(tela)#coloca a nave na tela
        todos_inimigos.draw(tela)
       
        if len(jogador.listaDisparo) > 0: #verifica se a lista de disparo é maior que 0
            for x in jogador.listaDisparo: #variavel que percorre a lista
                x.colocar(tela) #coloca a bala na tela 
                x.trajetoria() #faz percorrer a trajetoria
                if x.rect.top < -10: #verifica a bala ja passou da tela para remover
                    jogador.listaDisparo.remove(x) #remove a bala da tela
        pygame.display.update()#atualiza a tela 

invasao()
