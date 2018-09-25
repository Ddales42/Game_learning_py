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
perso_x = 0
perso_y = 0


#collage des surface
win.blit(perso, (perso_x, perso_y))

#mise a jour de l'ecran
pygame.display.flip()

#boucle prinipale
continuer = 1

while continuer:
    for event in pygame.event.get():    #Attente des évènements
        if event.type == QUIT:
            continuer = 0
        if event.type == MOUSEBUTTONDOWN
            if event.button == 1 #si clic gauche
                perso_x = event.pos[0]
                perso_y = event.pos[1]

        win.blit(fond(0,0))
        win.blit(perso, (perso_x, perso_y))
        pygame.display.flip()
