s_input = ''
i_problem = 0
while s_input != '고무오리 디버깅 끝':
    s_input = input()
    if s_input == '문제':
        i_problem += 1
    elif s_input == '고무오리':
        if i_problem <= 0:
            i_problem += 2
        else:
            i_problem -= 1
if i_problem == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')