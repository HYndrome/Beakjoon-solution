i_t = int(input())
for i_1 in range(i_t):
    lst_num = list(map(int, input().split()))
    print(f'#{i_1 + 1} {max(lst_num)}')