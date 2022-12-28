import sys
a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
c = int(sys.stdin.readline())
d = 0
for i in range(len(b)):
    if b[i] == c:
        d += 1
print(d)
