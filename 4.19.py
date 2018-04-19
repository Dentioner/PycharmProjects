# coding :utf-8
class ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = 'hi, I am a ' + self.size+' ' + self.color + ' ball!'
        return msg

    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'


myball = ball('red', 'small', 'down')


print 'I just created a ball'
print 'My ball is', myball.size
print 'My ball is', myball.color
print 'my ball\'s direction is', myball.direction
print 'Now I am going to bounce the ball'
myball.bounce()
print 'now the ball\'s direction is', myball.direction
print myball
