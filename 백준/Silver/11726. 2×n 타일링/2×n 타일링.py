i_n = int(input())
if i_n <= 2:
    ls_n = [0] * 3
else:
    ls_n = [0] * (i_n + 1)
ls_n[1] = 1
ls_n[2] = 2
for i in range(3, i_n + 1):
    ls_n[i] = ls_n[i - 2] + ls_n[i - 1]
print(ls_n[i_n] % 10007)
