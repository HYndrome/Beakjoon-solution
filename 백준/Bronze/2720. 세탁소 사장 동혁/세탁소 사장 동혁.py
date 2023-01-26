lst_coin = [25, 10, 5, 1]
i_t = int(input())
for i_1 in range(i_t):
    i_change = int(input())
    dict_change = {}
    for i_2 in lst_coin:
        i_cnt =  i_change // i_2
        i_change %= i_2
        dict_change[i_2] = i_cnt
    print(*dict_change.values())