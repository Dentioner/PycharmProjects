# coding: utf-8
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
x = 0
y = 0


ball = pygame.image.load('beach_ball.png')
screen.blit(ball, [x, y])
pygame.display.flip()
for i in range(100):
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    pygame.time.delay(20)
    x = x + 5
    screen.blit(ball, [x, y])
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
