import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline().rstrip()
c = 0
for i in b:
    c += int(i)
print(c)