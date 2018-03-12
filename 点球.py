from random import choice
print('Choose a direction to shoot')
print('left','right')
direction=['left','right']
you=raw_input()
dog=choice (direction)
print('dog tries to defend '+ dog)
if you!=dog:
    print('yooooooooooo')
else:
    print('sodayo')
