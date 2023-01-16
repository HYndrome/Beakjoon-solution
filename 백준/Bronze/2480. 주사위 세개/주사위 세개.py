lst_count = [0 for _ in range(6)]
lst_input = list(map(int, input().split()))
for i_1 in lst_input:
    lst_count[i_1 - 1] += 1
if max(lst_count) == 3:
    print(10000 + 1000 * (lst_count.index(3) + 1))
elif max(lst_count) == 2:
    print(1000 + 100 * (lst_count.index(2) + 1))
else:
    print(100 * max(lst_input))