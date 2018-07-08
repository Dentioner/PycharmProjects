# coding: utf-8
import pygame, sys
pygame.init()

screen = pygame.display.set_mode([640, 480])
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
clock = pygame.time.Clock()

class MyBall(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):

# self.rect = self.rect.move(self.speed)
#
# if self.rect.left < 0 or self.rect.right > width:
#     self.speed[0] = -self.speed[0]
#
# if self.rect.top < 0 or self.rect.bottom > height:
#     self.speed[1] = -self.speed[1]

        if self.rect.left <= screen.get_rect().left or \
            self.rect.right >= screen.get_rect().right:
            self.speed[0] = - self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos

my_ball = MyBall('beach_ball.png', [10, 0], [20, 20])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(30)
    screen.blit(background, (0, 0))
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
