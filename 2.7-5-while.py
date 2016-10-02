num=10
print 'Guess the number in my head.'
bingo=False#将False赋给bingo

while bingo==False:#这句话意思是判断bingo==False是否为真，判断的结果是bool为True，所以继续执行while内部的代码
    answer=input()#将待输入量赋给answer
    
    if answer<num:#假如输入的值小于num的值10，则执行if内部的代码，输出显示 too small！
        print'too small!'

    if answer>num:
        print'too big!'

    if answer==num:
        print'bingo!'
        bingo=True#在输入值和num的设定值相等的时候，需要结束这个while循环，将True赋给bingo，此时while遇到
