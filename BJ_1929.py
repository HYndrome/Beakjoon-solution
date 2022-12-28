import sys

i_m, i_n = map(int, sys.stdin.readline().split())

lst_num = [i_1 for i_1 in range(i_n+1)]
lst_num[1] = 0
for i_2 in lst_num:
    if i_2 == 0:
        continue
    else:
        for i_3 in range(i_2*2, i_n+1, i_2):
            lst_num[i_3] = 0
lst_prime = []
for i_4 in range(i_m, i_n+1):
    if lst_num[i_4] != 0:
        print(i_4)