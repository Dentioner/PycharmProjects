# coding: utf-8
class HotDog:
    def __init__(self):
        self.cook_level = 0
        self.cook_condition = 'raw'
        self.condiments = []

    def __str__(self):
        msg = 'hot dog'
        if len(self.condiments) > 0:
            msg += ' with '
        for i in self.condiments:
            msg += i + ', '
        msg = msg.strip(', ')
        msg = self.cook_condition + ' ' + msg + '.'
        return msg

    def cook (self, time):
        self.cook_level += time
        if self.cook_level > 8:
            self.cook_condition = 'coal'

        elif self.cook_level > 5:
            self.cook_condition = 'perfect'

        elif self.cook_level >3 :
            self.cook_condition = 'so so'

        else:
            self.cook_condition = 'raw'

    def Add (self, contiments):
        self.condiments.append(contiments)


MyDog = HotDog()
print MyDog.cook_level
print MyDog.cook_condition
print MyDog.condiments

for i in range(100):
    print 'Now I am going to cook it.'
    MyDog.cook(int(raw_input('How long will you cook?')))
    print MyDog.cook_level
    print 'now the hot dog is ' + MyDog.cook_condition
    if MyDog.cook_level > 20:
        print 'Eh, it seems too awful.'
        break

print 'Now I am going to make it delicious.'

for i in range(100):
    add = raw_input('What kind of ingredients do you want?')
    MyDog.Add(add)
    a = raw_input('OK?')
    if a == 'yes':
        break

print MyDog
