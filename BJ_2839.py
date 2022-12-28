import sys
a = int(sys.stdin.readline())
#3 5 6 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
#안되는 수 1 2 4 7
lst_non = [1, 2, 4, 7]
num1 = a//5
num2 = a - 5*num1
if a in lst_non:
    print(-1)
else: 
    while True:
        if num2%3 == 0:
            print(num1 + num2//3)
            break
        else:
            num2 += 5
            num1 -= 1