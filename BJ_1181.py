import sys

lst_i =[]
i_n = int(sys.stdin.readline())
for i_1 in range(i_n):
    s_i = sys.stdin.readline().rstrip()
    if s_i not in lst_i:
        lst_i.append(s_i)

lst_i.sort(key = lambda x: (len(x), x))

for i_2 in lst_i:
    print(i_2)