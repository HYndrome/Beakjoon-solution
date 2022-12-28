import sys

i_n = int(sys.stdin.readline())
lst_0 = [0 for i_1 in range(8001)]

for i_2 in range(i_n):
    i_n1 = int(sys.stdin.readline())
    lst_0[i_n1 + 4000] += 1

lst_i = [i_3 - 4000 for i_3 in range(8001) if lst_0[i_3] != 0]
lst_c = [i_4 for i_4 in lst_0 if i_4 != 0]

lst_multi = [i_6 * i_7 for (i_6, i_7) in zip(lst_i, lst_c)]
o_mean = round(sum(lst_multi) / i_n)

sum_c = 0
for i_5 in range(len(lst_c)):
    sum_c += lst_c[i_5]
    if sum_c >= (i_n + 1) / 2:
        o_middle = lst_i[i_5]
        break

if lst_c.count(max(lst_c)) == 1:
    o_common = lst_i[lst_c.index(max(lst_c))]
else:
    lst_c[lst_c.index(max(lst_c))] = 0
    o_common = lst_i[lst_c.index(max(lst_c))]

o_range = max(lst_i) - min(lst_i)


print(o_mean)
print(o_middle)
print(o_common) 
print(o_range)