import sys
a = int(sys.stdin.readline())
b = a
c = 0
while True:
    if c != 0 and a == b:
        print(c)
        break
    else:
        if b//10 == 0:
            b = b*10 + b
            c += 1
        else:
            b = b%10*10 + (b%10 + b//10)%10
            c += 1