i_n = int(input())
lst_sg = list(map(int, input().split()))
dct_sg = {}
for i_1 in lst_sg:
    dct_sg[i_1] = dct_sg.get(i_1, 0) + 1
i_m = int(input())
lst_judge = list(map(int, input().split()))
for i_2 in lst_judge:
    try:
        print(dct_sg[i_2], end= ' ')
    except:
        print('0', end= ' ')