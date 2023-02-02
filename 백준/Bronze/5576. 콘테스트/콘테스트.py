lst_w = [int(input()) for i_1 in range(10)]
lst_k = [int(input()) for i_2 in range(10)]
i_w = sum(sorted(lst_w)[-3:])
i_k = sum(sorted(lst_k)[-3:])
print(i_w, i_k)