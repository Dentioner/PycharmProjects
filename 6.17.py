# coding: utf-8
import pygame,math, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pointlist = []
for x in range(1, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi)*200 + 240)
    # pygame.draw.rect(screen, [0, 0, 0], [x, y, 1, 1], 1)
    pointlist.append([x, y])

pygame.draw.lines(screen, [0, 0, 0], False, pointlist, 2)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
