str_input = input()

ls_number = []
cnt_operator = 0
cnt_minus = 0
s_cnt = ''
for s_1 in str_input:
    if (s_1 == '+') or (s_1 == '-'):
        cnt_operator += 1
        if (s_1 == '-') and (cnt_minus ==0):
            cnt_minus = cnt_operator
        ls_number.append(int(s_cnt))
        s_cnt = ''  
    else:
        if s_cnt == '' and s_1 == '0':
            pass
        else:
            s_cnt += s_1

else:
    ls_number.append(int(s_cnt))

sum_max = 0
if cnt_minus == 0:
    for i_1 in range(len(ls_number)):
        sum_max += ls_number[i_1]

else:
    for i_2 in range(cnt_minus):
        sum_max += ls_number[i_2]

    for i_3 in range(cnt_minus, len(ls_number)):
        sum_max -= ls_number[i_3]

print(sum_max)