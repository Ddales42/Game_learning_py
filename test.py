#!/usr/bin/python3
import pygame, sys
from pygame.locals import *

#initialistaion pygame
pygame.init()
#creation des surfaces

size = width, height = 800, 800
speed = [10, 10]
black = 0, 0, 0
#Chargement et collage du fond
screen = pygame.display.set_mode(size)
#Chargement et collage du personnage, avant la boucle,
ball = pygame.image.load("golf.png")
ballrect = ball.get_rect()

perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()

screen.blit(perso, position_perso)
screen.blit(screen,(800,800))

#collage des surface


#mise a jour de l'ecran

#rester appuyer sur une touche
pygame.key.set_repeat(400, 30)
#boucle prinipacontinuer = 1

while 1:
    for event in pygame.event.get():    #Attente des évènements
        if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)

        if event.type == KEYDOWN:
            if event.key == K_DOWN: #attend un événement "flèche bas"
#Si je reçois l'événement, je déplace le Rect de 6px vers le bas.
                position_perso = position_perso.move(0,6)
            if event.key == K_RIGHT: #attend un événement "flèche droite"
#Si je reçois l'événement, je déplace le Rect de 6px vers la droite.
                position_perso = position_perso.move(6,0)
            if event.key == K_UP:
                position_perso = position_perso.move(0,-6)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-6, 0)


        if ballrect.left < 0 or ballrect.right > 800:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > 800:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
#Toujours dans la boucle, puisque ça doit arriver à chaque fois qu'on
#appuie sur la flèche, je recouvre la fenêtre avec le fond,
#je place mon personnage à sa nouvelle position et je rafraîchis l'écran !

    screen.blit(perso, position_perso)
    pygame.display.flip()
