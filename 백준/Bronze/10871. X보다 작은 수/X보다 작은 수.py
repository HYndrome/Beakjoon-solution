lst_output = []
i_n, i_x = map(int, input().split())
lst_n = list(map(int, input().split()))
for i_1 in lst_n:
    if i_1 < i_x:
        lst_output.append(i_1)
print(*lst_output)