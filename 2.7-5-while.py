num=10
print 'Guess the number in my head.'
bingo=False

while bingo==False:
    answer=input()
    
    if answer<num:
        print'too small!'

    if answer>num:
        print'too big!'

    if answer==num:
        print'bingo!'
        bingo=True
