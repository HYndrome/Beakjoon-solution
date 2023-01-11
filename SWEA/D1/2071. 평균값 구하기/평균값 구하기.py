i_t = int(input())
for i_1 in range(i_t):
    lst_input = list(map(int, input().split()))
    i_mean = round(sum(lst_input) / len(lst_input))
    print(f'#{i_1 + 1} {i_mean}')