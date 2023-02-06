s_input = input()
i_happy = 0
i_sad = 0
for i_1 in range(len(s_input)):
    try:
        if (s_input[i_1] == ':') * (s_input[i_1 + 1] == '-'):
            try:
                if s_input[i_1 + 2] == ')':
                    i_happy += 1
                elif s_input[i_1 + 2] == '(':
                    i_sad += 1
            except:
                pass
    except:
        pass
if (i_sad == 0) * (i_happy == 0):
    print('none')
elif i_sad == i_happy:
    print('unsure')
elif i_sad > i_happy:
    print('sad')
elif i_sad < i_happy:
    print('happy')