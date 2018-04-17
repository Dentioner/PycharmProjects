# coding :utf-8
class ball:
    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'


myball = ball()
myball.direction = 'down'
myball.color = 'red'
myball.size = 'small'

print 'I just created a ball'
print 'My ball is', myball.size
print 'My ball is', myball.color
print 'my ball\'s direction is', myball.direction
print 'Now I am going to bounce the ball'
myball.bounce()
print 'now the ball\'s direction is', myball.direction
