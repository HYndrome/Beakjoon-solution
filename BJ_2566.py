import sys
i_max = 0
i_r = 0
for i_1 in range(9):
    lst_i = list(map(int, sys.stdin.readline().split()))
    i_max1 = max(lst_i)
    if i_max1 > i_max:
        i_max = i_max1
        i_r = i_1 + 1
        i_c = lst_i.index(i_max1) + 1
print(i_max)
print(i_r, i_c)