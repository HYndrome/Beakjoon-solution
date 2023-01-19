i_sum = 0
i_min = 100
for i_1 in range(7):
    i_n = int(input())
    if i_n % 2 == 1:
        i_sum += i_n
        if i_n < i_min:
            i_min = i_n
if i_sum == 0:
    print(-1)
else:
    print(i_sum)
    print(i_min)