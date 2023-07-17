# dp
i_n = int(input())
if i_n >= 3:
    ls_n = [0] * i_n
    ls_n[0] = 1
    ls_n[1] = 3
    for n in range(2, i_n):
        ls_n[n] = ls_n[n - 1] + 2 * ls_n[n-2]
    print(ls_n[i_n - 1] % 10007)
elif i_n == 2:
    print(3)
elif i_n == 1:
    print(1)