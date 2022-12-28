import sys
a = int(sys.stdin.readline())
i = 0
penta = 1
while True:
    penta += 6*i
    i +=1
    if penta >= a:
        print(i)
        break