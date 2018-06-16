# coding: utf-8
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_rect = [320, 240, 100, 100]
pygame.draw.rect(screen, [114, 145, 190], my_rect, 100)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
