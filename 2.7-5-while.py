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
<<<<<<< HEAD
        bingo=True#在输入值和num的设定值相等的时候，需要结束这个while循环，将True赋给bingo，此时while遇到False，结束程序
=======
        bingo=True
>>>>>>> parent of d5a1d72... Update 2.7-5-while.py
