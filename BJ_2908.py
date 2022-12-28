import sys
a,b = sys.stdin.readline().split()
a_r = int(a[::-1])
b_r = int(b[::-1])
if a_r > b_r:
    print(a_r)
else:
    print(b_r)