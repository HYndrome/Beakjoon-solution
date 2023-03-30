i_n = int(input())
ls_distance = list(map(int,input().split()))
ls_price = list(map(int, input().split()))

cost_sum = 0
for i_1 in range(len(ls_distance)):
    cost_sum += ls_distance[i_1] * min(ls_price[:i_1 + 1])

print(cost_sum)