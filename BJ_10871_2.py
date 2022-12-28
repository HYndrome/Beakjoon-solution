import sys
n, x = map(int, sys.stdin.readline().split())
aa = sys.stdin.readline().split()
bb = []
for i in range(len(aa)):
    if int(aa[i]) < x:
       bb.append(aa[i])
print(*bb)