# coding: utf-8
import pygame, sys
pygame.init()
screen = pygame.display.set_caption('hello world!')
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
screen.set_at([150, 150], [255, 0, 0])  # 将150，150改为红色。
pygame.display.flip()
print screen.get_at([150, 150])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
