# 1.while循环
num = 0

while num < 10:
    num = num + 1
    print(num)


#while嵌套

num = 0
while num < 10 :

    num2 = 0
    while num2 < num:

        print("*", end='')
        num2 = num2 + 1

    print("")
    num = num + 1


a = 1

while a <= 9:
    b = 1

    while b <= a:

        print("%d * %d = %d  "%(a,b,a*b),end='')

        b += 1

    print('')
    a += 1
