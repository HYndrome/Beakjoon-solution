import sys

i_n, i_m = map(int, sys.stdin.readline().split())
set_n = set()
set_m = set()
for i_1 in range(i_n):
    set_n.add(sys.stdin.readline().rstrip())
for i_2 in range(i_m):
    set_m.add(sys.stdin.readline().rstrip())
set_mn = set_n & set_m
print(len(set_mn))
lst_mn = sorted(set_mn)
for s_1 in lst_mn:
    print(s_1)