import pygame, sys,random
from random import *

pygame.init()
size=(800,450)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Felipe")
imagem=pygame.image.load("stars.jpg")
tiro=pygame.image.load("tiro1.png")
x=1
y=1
nave=pygame.image.load("nave1.png")
inimigo=pygame.image.load("inimigo.png")
screen.blit(imagem,(x,y))
shootSpeed=2
criar=True
x_inimigos=0
y_inimigos=0

clock=pygame.time.Clock()

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type==pygame.MOUSEMOTION:
            z = pygame.mouse.get_pos()[0]
            a = pygame.mouse.get_pos()[1]
            x=1
            y=1
            screen.blit(imagem,(x,y))
            screen.blit(inimigo,(x_inimigos,y_inimigos))
            screen.blit(nave,(z,a))
            pygame.mouse.set_visible(False)
                    
      
        if event.type==pygame.MOUSEBUTTONDOWN:
            z = pygame.mouse.get_pos()[0]
            a = pygame.mouse.get_pos()[1]
            x_shootPos=z
            y_shootPos=a
            while x_shootPos<=800:
                screen.blit(imagem,(1,1))
                screen.blit(nave,(z,a))
                screen.blit(tiro,(x_shootPos,y_shootPos+10))
                x_shootPos+=shootSpeed
                clock.tick(300)
                pygame.display.flip()
            screen.blit(imagem,(1,1))
            screen.blit(nave,(z,a))
            func()
            pygame.display.flip()

        #passa os parametros do inimigo
        if criar==True:
            x_inimigos=600
            y_inimigos=randint(20,400)
            criar=False
            

        #desenha os inimigos na tela

        screen.blit(inimigo,(x_inimigos,y_inimigos))
        
        y_inimigos+=2
            
    pygame.display.flip()
    clock.tick(1000)
