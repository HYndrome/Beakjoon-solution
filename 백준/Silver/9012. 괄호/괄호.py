i_t = int(input())
for i_1 in range(i_t):
    s_input = input()
    lst_PS = []
    bool_PS = True
    for s_1 in s_input:
        if s_1 == '(':
            lst_PS.append('(')
        elif s_1 ==')':
            try:
                lst_PS.pop()
            except IndexError:
                bool_PS = False
                break
    if (len(lst_PS) == 0) * (bool_PS == True):
        print('YES')
    else:
        print('NO')