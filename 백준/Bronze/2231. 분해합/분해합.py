s_n = input()
i_n = int(s_n)

if i_n < 19:
    i_min = 0
else:
    i_min = i_n - 9 * len(s_n)
lst_m = []
for i_1 in range(i_min, i_n):
    s_1 = str(i_1)
    i_1_revm = i_1
    for s_2 in s_1:
        i_1_revm += int(s_2)
    if i_1_revm == i_n:
        print(i_1)
        break
    if i_1 == i_n - 1:
        print(0)