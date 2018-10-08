#Jeu Donkey Kong Labyrinth
#Jeu dans lequel on doit déplacer DK travers un labyrinthe.
#Script Python
#!/usr/bin/python
# -*- coding: Utf-8 -*

import sys, pygame
from pygame.locals import *
from constantes import *

pygame.init()

win = pygame.display.set_mode((cote_fenetre, cote_fenetre))

icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

pygame.display.set_caption(titre_fenetre)

continuer = 1
while continuer:

    accueil = pygame.image.load(image_accueil).convert()
    win.blit(accueil, (0,0))
    pygame.display.flip()

    continuer_jeux = 1
    continuer_accueil = 1

    while continuer_accueil:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer = 0
                continuer_jeux = 0
                continuer_accueil = 0

                choix = 0

            elif event.type == KEYDOWN:
                if event.key == K_w:
                    choix = 'n1'
                    continuer_accueil = 0
                elif event.key == K_x:
                    choix = 'n2'
                    continuer_accueil = 0
    choix != 0
        fond = pygame.image.load(image_fond).convert
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(win)
    while continuer_jeux:
