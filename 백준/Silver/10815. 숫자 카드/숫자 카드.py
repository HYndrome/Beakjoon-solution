i_n = int(input())
set_n = set(map(int, input().split()))
i_m = int(input())
lst_m = list(map(int, input().split()))

for i_1 in lst_m:
    if i_1 in set_n:
        print(1, end= ' ')
    else:
        print(0, end= ' ')