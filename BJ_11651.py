import sys

lst_i = []
i_n = int(sys.stdin.readline())
for i_1 in range(i_n):
    i_x, i_y = map(int, sys.stdin.readline().split())
    lst_i.append([i_x, i_y])

lst_i.sort(key = lambda x : (x[1], x[0]))
for i_2 in lst_i:
    print(*i_2)