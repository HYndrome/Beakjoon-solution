import sys
a, b, v = map(int, sys.stdin.readline().split())
d = 0
while True:
    d += 1
    v -= a
    if v <= 0:
        break
    v += b
print(d)
