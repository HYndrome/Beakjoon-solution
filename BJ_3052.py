import sys
aa = []
for i in range(10):
    a = int(sys.stdin.readline())%42
    aa.append(a)
print(len(set(aa)))