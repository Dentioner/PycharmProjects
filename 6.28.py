# coding: utf-8
import pygame, sys

class MyBall(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pic = 'beach_ball.png'
balls = []
for hang in range(3):
    for lie in range(3):
        location = [hang*180 + 10, lie*180 + 10]
        ball = MyBall(pic, location)
        balls.append(ball)

for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



