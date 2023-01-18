i_t = int(input())
for i_1 in range(i_t):
    lst_input = input().split()
    for s_1 in lst_input:
        print(s_1[::-1], end= ' ')
    print()