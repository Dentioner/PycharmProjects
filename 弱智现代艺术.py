# coding: utf-8
import pygame, random, sys
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])

# for i in range(100):
#     left = random.choice(range(250))
#     top = random.choice(range(100))
#     width = random.choice(range(400))
#     height = random.choice(range(500))
#     R = random.choice(range(255))
#     G = random.choice(range(255))
#     B = random.choice(range(255))
#     pygame.draw.rect(screen, [R, G, B], [left, top, width, height], 1)
#
# pygame.display.flip()

for i in range(100):
    left = random.choice(range(250))
    top = random.choice(range(100))
    width = random.choice(range(400))
    height = random.choice(range(500))
    color_name = random.choice(THECOLORS.keys())
    color = THECOLORS[color_name]
    line_width = random.choice(range(1, 3))
    pygame.draw.rect(screen, color, [left, top, width, height], line_width)

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
