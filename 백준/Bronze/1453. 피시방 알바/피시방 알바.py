lst_computer = [0 for i_1 in range(100)]
i_cnt = 0
i_n = int(input())
lst_n = list(map(int, input().split()))
for i_2 in lst_n:
    if lst_computer[i_2 - 1] == 0:
        lst_computer[i_2 - 1] = 1
    else:
        i_cnt += 1
print(i_cnt)