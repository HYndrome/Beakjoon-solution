lst_init = list(map(int, input().split()))
def change_stone(a, b):
    i_temp = lst_init[a]
    lst_init[a] = lst_init[b]
    lst_init[b] = i_temp
    print(*lst_init)
while lst_init != [1, 2, 3, 4, 5]:
    if lst_init[0] > lst_init[1]:
        change_stone(0, 1)
    if lst_init[1] > lst_init[2]:
        change_stone(1, 2)
    if lst_init[2] > lst_init[3]:
        change_stone(2, 3)
    if lst_init[3] > lst_init[4]:
        change_stone(3, 4)