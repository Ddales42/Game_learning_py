#!/usr/bin/python
import sys, pygame
from pygame.locals import *
pygame.init()

size = width, height = 800, 800
speed = [10, 10]
black = 0, 0, 0
y = 0
x = 5
screen = pygame.display.set_mode(size)

ball = pygame.image.load("tennis.gif")
ballrect = ball.get_rect()

perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()

screen.blit(perso, position_perso)
screen.blit(screen,(800,800))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > 760:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > 760:
        speed[1] = -speed[1]
        
    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            position_perso = position_perso.move(0,6)
        if event.key == K_RIGHT:
            position_perso = position_perso.move(6,0)
        if event.key == K_UP:
            position_perso = position_perso.move(0,-6)
        if event.key == K_LEFT:
            position_perso = position_perso.move(-6, 0)
        if event.key == K_a:
            pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(perso, position_perso)
    pygame.display.flip()
