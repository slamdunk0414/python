import random

player = int(input('请输入1-3 1是石头 2是剪刀 3是布 '))

com = random.randint(1,3)

print("电脑输入的是%d"%com)

if (player == 1 and com == 2) or (player ==2 and com ==3) or (player == 3 and com == 1):
    print("你真厉害 赢了")
elif player == com:
    print("平手")
else:
    print("你输了")
