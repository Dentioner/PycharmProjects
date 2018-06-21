# coding: utf-8
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])

ball = pygame.image.load('beach_ball.png')
screen.blit(ball, [0, 0])
pygame.display.flip()
pygame.time.delay(2000)
screen.blit(ball, [100, 50])
pygame.draw.rect(screen, [255, 255, 255], [0, 0, 90, 90], 0)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
