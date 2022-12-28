import sys

lst_member =[]
i_n = int(sys.stdin.readline())
for i_1 in range(i_n):
    s_age, s_name = sys.stdin.readline().split()
    i_age = int(s_age)
    lst_member.append([i_age, s_name, i_1])

lst_member.sort(key = lambda x: (x[0], x[2]))

for i_2 in lst_member:
    print(f'{i_2[0]} {i_2[1]}')
