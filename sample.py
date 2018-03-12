from random import randint
num= randint(5,10)
print('Guess what i think?')
bingo = False

while bingo == False :
    answer = input()
    if answer < num:
        print('%d is too small'%answer)

    if answer > num:
        print '%d is too big' %answer

    if answer == num:
        print('BINGO, %d is the right answer'%answer)
        bingo = True

