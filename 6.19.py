# coding: utf-8
import sys, pygame
pygame.init()
screen = pygame.display.set_mode([1024, 768])
screen.fill([255, 255, 255])

my_waifu = pygame.image.load('waifu2.png')
screen.blit(my_waifu, [0, 0])

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
