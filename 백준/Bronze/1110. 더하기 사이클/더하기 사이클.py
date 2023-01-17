i_n = int(input())
i_cycle = i_n
i_count = 0
while (i_cycle != i_n) + (i_count == 0):
    i_cycle = (i_cycle % 10) * 10 + ((i_cycle // 10 + i_cycle % 10) % 10)
    i_count += 1
print(i_count)