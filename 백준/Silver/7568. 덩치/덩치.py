import sys

i_n = int(sys.stdin.readline())
lst_input = []
for i_1 in range(i_n):
    i_weight, i_height = map(int, sys.stdin.readline().split())
    lst_input.append([i_weight, i_height])
for lst_1 in lst_input:
    i_cnt = 1
    for lst_2 in lst_input:
        if (lst_2[0] > lst_1[0]) * (lst_2[1] > lst_1[1]):
            i_cnt += 1
    lst_1.append(i_cnt)
print(*[lst_3[2] for lst_3 in lst_input])