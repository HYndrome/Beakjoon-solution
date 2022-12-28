import sys
num1 = int(input())
for i in range(num1):
    num2, num3 = map(int,sys.stdin.readline().split())
    print(num2 + num3)