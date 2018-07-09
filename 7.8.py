# coding: utf-8
import pygame, sys
pygame.init()

screen = pygame.display.set_mode([640, 480])
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
clock = pygame.time.Clock()

class MyBall(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
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

my_ball = MyBall('beach_ball.png', [0, 0], [20, 20])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # print event.type
            # print type(event.type)
            # print pygame.QUIT
            # print type(pygame.QUIT)
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_ball.rect.top = my_ball.rect.top - 10
            elif event.key == pygame.K_DOWN:
                my_ball.rect.top = my_ball.rect.top + 10
            elif event.key == pygame.K_RIGHT:
                my_ball.rect.left = my_ball.rect.left + 10
            elif event.key == pygame.K_LEFT:
                my_ball.rect.left = my_ball.rect.left - 10

    clock.tick(30)
    screen.blit(background, (0, 0))
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
