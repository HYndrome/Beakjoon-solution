import sys

n, x = map(int, sys.stdin.readline().split())
aa = [map(int, sys.stdin.readline().split())]
bb = []

for i in range(len(aa)):
    if aa[i] < x:
       bb.append(aa[i])

print(*bb)