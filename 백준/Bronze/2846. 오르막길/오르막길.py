i_n = int(input())
lst_road = list(map(int, input().split()))
lst_uphill = [0]
i_hill = 0
for i_1 in range(1, i_n):
    if lst_road[i_1] > lst_road[i_1 - 1]:
        i_hill += lst_road[i_1] - lst_road[i_1 - 1]
        lst_uphill.append(i_hill)
    else:
        i_hill = 0
print(max(lst_uphill))