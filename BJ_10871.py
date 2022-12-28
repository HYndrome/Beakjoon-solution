import sys

n, x = map(int, sys.stdin.readline().split())
aa = list(map(int, sys.stdin.readline().split()))
bb = []

for i in range(len(aa)):
    if aa[i] < x:
       bb.append(aa[i])

print(*bb)