i_max = 0
i_index = 0
for i_1 in range(9):
    i_input = int(input())
    if i_input >= i_max:
        i_max = i_input
        i_index = i_1 + 1
print(i_max)
print(i_index)