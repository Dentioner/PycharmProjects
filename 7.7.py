# coding: utf-8
import pygame, sys
from random import *

class MyBall(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]


def animate(group):
    screen.fill([255, 255, 255])
    for a in group:
        a.move()
    for a in group:
        group.remove(a)
        if pygame.sprite.spritecollide(a, group, False):
            a.speed[0] = -a.speed[0]
            a.speed[1] = -a.speed[1]

        group.add(a)
        # a.move()
        screen.blit(a.image, a.rect)

    pygame.display.flip()


size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pic = 'beach_ball.png'
clock = pygame.time.Clock()
group = pygame.sprite.Group()


for hang in range(4):
    for lie in range(4):
        location = [hang*180 + 10, lie*180 + 10]
        speed = [choice([-2, 2]), choice([-2, 2])]
        ball = MyBall(pic, location, speed)

        group.add(ball)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fps = clock.get_fps()
            print 'fps = ',  fps
            sys.exit()

    animate(group)
    clock.tick(1000)