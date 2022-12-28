import sys

s_i = sys.stdin.readline().rstrip()
lst_i = [int(i_1) for i_1 in s_i]
lst_i1 = [0 for i_2 in range(10)]
for i_3 in lst_i:
    lst_i1[i_3] += 1
i_o =""
for i_4 in range(9, -1, -1):
    i_o += lst_i1[i_4]*str(i_4)
print(i_o)