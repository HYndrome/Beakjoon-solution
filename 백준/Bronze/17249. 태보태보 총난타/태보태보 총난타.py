s_taebo = input()
i_middle = s_taebo.index('0')
i_taebo_left = 0
i_taebo_right = 0
for s_1 in s_taebo[:i_middle]:
    if s_1 == '@':
        i_taebo_left += 1
for s_2 in s_taebo[i_middle:]:
    if s_2 == '@':
        i_taebo_right += 1
print(i_taebo_left, i_taebo_right)