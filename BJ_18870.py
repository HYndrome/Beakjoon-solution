import sys

i_n = int(sys.stdin.readline())
lst_i = list(map(int, sys.stdin.readline().split()))

lst_0 = [0 for i_1 in range(2*10**9 + 1)]
for i_2 in range(lst_i):
    lst_0[i_2 - 10**9] = 1

lst_i1 = [i_3 - 10**9 for i_3 in range(2*10**9 + 1) if lst_0[i_3] != 0]
lst_c = [i_4 for i_4 in lst_0 if i_4 != 0]

print(lst_i1)
print(lst_c)