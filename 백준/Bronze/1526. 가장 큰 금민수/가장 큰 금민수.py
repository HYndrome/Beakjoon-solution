s_n = input()
lst_minsu = [4, 7]
if int(s_n) >= int('4'*len(s_n)):
    i_digit = len(s_n)
else:
    i_digit = len(s_n) - 1
i_bi_digit = 2**i_digit
i_bi_maxdigit = len(bin(i_bi_digit)[2:]) - 1
lst_bi = []
for i_1 in range(i_bi_digit):
    str_append = '0'*(i_bi_maxdigit - len(bin(i_1)[2:])) + bin(i_1)[2:]
    lst_bi.append(str_append)
for s_1 in reversed(lst_bi):
    s_result = ''
    for s_2 in s_1:
        s_result += str(lst_minsu[int(s_2)])
    i_result = int(s_result)
    if i_result <= int(s_n):
        print(i_result)
        break