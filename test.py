#!/usr/bin/python3
import pygame
from pygame.locals import *

#initialistaion pygame
pygame.init()

#creation des surfaces
win = pygame.display.set_mode((640,480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
win.blit(fond,(0,0))

#Chargement et collage du personnage, avant la boucle,
#je crée un Rect pour gérer la position de mon personnage.
#Et je colle le personnage à sa position initiale.
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()

#collage des surface
win.blit(perso, position_perso)

#mise a jour de l'ecran
pygame.display.flip()

#rester appuyer sur une touche
pygame.key.set_repeat(400, 30)

#boucle prinipale
continuer = 1

while continuer:
    for event in pygame.event.get():    #Attente des évènements
        if event.type == QUIT:
            continuer = 0
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
#Toujours dans la boucle, puisque ça doit arriver à chaque fois qu'on
#appuie sur la flèche, je recouvre la fenêtre avec le fond,
#je place mon personnage à sa nouvelle position et je rafraîchis l'écran !
    win.blit(fond,(0,0))
    win.blit(perso, position_perso)
    pygame.display.flip()
