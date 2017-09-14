import pygame, sys
from random import *

pygame.init()
size=(800,450)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Felipe")
imagem=pygame.image.load("stars.jpg")
x=1
y=1
nave=pygame.image.load("nave1.png")
screen.blit(imagem,(x,y))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            z = pygame.mouse.get_pos()[0]
            a = pygame.mouse.get_pos()[1]
            colorRect=((200,0,130))
            x=1
            y=1
            screen.blit(imagem,(x,y))
            screen.blit(nave,(z,a))
            
            
    pygame.display.update()
