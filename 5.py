a = 10
print ('guess a=what?')
b=int(input())
while a!=b:
    print ('please try again')
    if a<b:
        print ('big')
    if a>b:
        print ('small')
    b=int(input())

print ('BINGO')
