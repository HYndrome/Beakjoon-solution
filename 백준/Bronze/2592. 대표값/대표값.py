dict_n = {}
i_sum = 0
i_mode = 0
i_mode_count = 0
for i_1 in range(10):
    i_x = int(input())
    dict_n[i_x] = dict_n.get(i_x, 0) + 1
for key_1, value_1 in dict_n.items():
    i_sum += key_1 * value_1
    if value_1 > i_mode_count:
        i_mode_count = value_1
        i_mode = key_1
print(int(i_sum / sum((dict_n.values()))))
print(i_mode)