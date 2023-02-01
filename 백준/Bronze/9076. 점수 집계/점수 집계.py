i_t = int(input())
for i_1 in range(i_t):
    lst_score = list(map(int, input().split()))
    lst_middle = sorted(lst_score)[1:-1:1]
    if abs(lst_middle[0] - lst_middle[-1]) >= 4:
        print('KIN')
    else:
        print(sum(lst_middle))