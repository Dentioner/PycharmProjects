# coding: utf-8
import pygame, sys
pygame.init()
screen = pygame.display.set_mode([1080, 720])
screen.fill([255, 255, 255])
x = 0
y = 0
x_speed = 5
a = True

ball = pygame.image.load('beach_ball.png')
screen.blit(ball, [x, y])
pygame.display.flip()

# while not False:
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     pygame.time.delay(20)
#     x = x + x_speed
#     screen.blit(ball, [x, y])
#     if x < 0 or x > 550:
#         x_speed = -x_speed
#     pygame.display.flip()

while a == True:
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    pygame.time.delay(20)
    x = x + x_speed
    screen.blit(ball, [x, y])
    if x < 0 or x > screen.get_width() - 90:
        x_speed = -x_speed
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
