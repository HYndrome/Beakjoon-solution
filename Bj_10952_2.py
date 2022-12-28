import sys
a = 1
b = 1
while a or b:
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
    